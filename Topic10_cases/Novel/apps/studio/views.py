from django.shortcuts import get_list_or_404, redirect
from novel_warehouse.views import show
from apps.novel.models import Novel, TagRelation, Tag, Volumn, Chapter
from apps.user.auth import login_and_redirect, get_user_data
from .form import NewNovelForm, NovelForm, VolumnForm, ChapterForm


@login_and_redirect
def work(request, user):
    novel_list = user.work.all

    context = {"novel_list": novel_list}
    return show(request, 'studio/work.html', context)


def novel(request, novel_id):
    user = get_user_data(request)
    if (user == None):
        return redirect('/login/')

    novel_obj = get_list_or_404(Novel, id=novel_id)[0]
    if novel_obj.author != user:
        redirect('/login/')

    context = {}

    if request.method == 'POST':
        form = NovelForm(request.POST, request.FILES)

        if form.is_valid():
            data = form.cleaned_data
            novel_obj.title = data['title']
            novel_obj.description = data['description']
            novel_obj.state = data['state']

            if data['cover']:
                novel_obj.cover = data['cover']
            novel_obj.save()

            tag_list = []
            if data['tags']:
                tag_list = data['tags'].split(' ')
            for tag in tag_list:
                if TagRelation.objects.filter(novel=novel_obj,
                                              tag__tagname=tag).count() == 0:
                    if Tag.objects.filter(tagname=tag).count() == 0:
                        newtag = Tag(tagname=tag)
                        newtag.save()

                    newtag = Tag.objects.filter(tagname=tag).first()
                    newrelation = TagRelation.objects.create(novel=novel_obj,
                                                             tag=newtag)
                    newrelation.save()

            old_relation = TagRelation.objects.filter(novel=novel_obj).all()
            for tag in old_relation:
                if not (tag.tag.tagname in tag_list):
                    tag.delete()

                    if TagRelation.objects.filter(tag=tag.tag).count() == 0:
                        tag.tag.delete()
            print("Removed")
        else:
            clear_errors = form.errors.get("__all__")
            context["form"] = form
            context["form_messages"] = clear_errors

    tagrelation_set = TagRelation.objects.filter(novel=novel_obj)
    tag_list = [relation.tag.tagname for relation in tagrelation_set]

    context["novel"] = novel_obj
    context["tags"] = ' '.join(tag_list)
    return show(request, 'studio/novel.html', context)


def new(request):
    user = get_user_data(request)
    if (user == None):
        return redirect('/login/')

    if request.method == 'GET':
        return show(request, 'studio/new.html')

    form = NewNovelForm(request.POST, request.FILES)

    if form.is_valid():
        data = form.cleaned_data
        novel_obj = Novel(title=data['title'],
                          description=data['description'],
                          state=data['state'],
                          cover=data['cover'],
                          author=user)
        novel_obj.save()

        tag_list = data['tags'].split(' ')
        for tag in tag_list:
            if TagRelation.objects.filter(novel=novel_obj,
                                          tag__tagname=tag).count() == 0:
                if Tag.objects.filter(tagname=tag).count() == 0:
                    newtag = Tag(tagname=tag)
                    newtag.save()

                newtag = Tag.objects.filter(tagname=tag).first()
                newrelation = TagRelation.objects.create(novel=novel_obj,
                                                         tag=newtag)
                newrelation.save()

        return redirect('/studio/novel/' + str(novel_obj.id))
    else:
        clear_errors = form.errors.get("__all__")
        return show(request, 'studio/new.html', {
            "form": form,
            "form_messages": clear_errors
        })


def catalog(request, novel_id):
    user = get_user_data(request)
    if (user == None):
        return redirect('/login/')

    novel_obj = get_list_or_404(Novel, id=novel_id)[0]
    if novel_obj.author != user:
        redirect('/login/')

    context = {}

    context["novel"] = novel_obj
    context["catalog"] = novel_obj.get_volumn_chapter_dict()
    return show(request, 'studio/catalog.html', context)


def volumn(request, novel_id):
    user = get_user_data(request)
    if (user == None):
        return redirect('/login/')

    novel_obj = get_list_or_404(Novel, id=novel_id)[0]
    if novel_obj.author != user:
        redirect('/login/')

    context = {}

    if request.method == 'POST':
        form = VolumnForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            new_volumn = Volumn(novel=novel_obj, title=data['title'])
            new_volumn.save()
        else:
            clear_errors = form.errors.get("__all__")
            context["form"] = form
            context["form_messages"] = clear_errors

    return redirect(f'/studio/catalog/{novel_id}')


def chapter(request, novel_id):
    user = get_user_data(request)
    if (user == None):
        return redirect('/login/')

    novel_obj = get_list_or_404(Novel, id=novel_id)[0]
    if novel_obj.author != user:
        redirect('/login/')

    context = {}

    if request.method == 'POST':
        form = ChapterForm(request.POST, request.FILES)

        if form.is_valid():
            data = form.cleaned_data
            new_chapter = Chapter(volumn=novel_obj.volumn_set.last(),
                                  title=data['title'],
                                  content=data['content'])
            new_chapter.save()
        else:
            clear_errors = form.errors.get("__all__")
            context["form"] = form
            context["form_messages"] = clear_errors

            # print(form.errors)

    return redirect(f'/studio/catalog/{novel_id}')
