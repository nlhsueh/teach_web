import os
from django.shortcuts import get_list_or_404, redirect
from django.db.models import Sum
from novel_warehouse.views import show
from .models import Novel, Chapter
from apps.user.auth import get_user_data
from apps.feedback.models import HistoryRelation


def novel_view(request, novel_id):
    novel_obj = get_list_or_404(Novel, id=novel_id)[0]

    context = {
        "novel": novel_obj,
        "similar": novel_obj.get_similar_books(),
        "last_chapter": novel_obj.get_latest_chapter(),
        "word_count": Chapter.objects.filter(volumn__novel=novel_obj).aggregate(nums=Sum('word_count'))['nums'] or "0"
    }

    return show(request, 'novel/novel.html', context)


def catalog_view(request, novel_id):
    novel_obj = get_list_or_404(Novel, id=novel_id)[0]

    context = {
        'novel': novel_obj,
        'catalog': novel_obj.get_volumn_chapter_dict()
    }

    return show(request, 'novel/catalog.html', context)


def content_view(request, novel_id, chapter_id):
    chapter_obj = Chapter.objects.filter(id=chapter_id).first()
    novel_obj = chapter_obj.volumn.novel

    if novel_id != novel_obj.id:
        return redirect('/novel/' + str(novel_id))

    # record the reading history
    user = get_user_data(request)
    if user:
        HistoryRelation.objects.filter(user=user, novel=novel_obj).delete()
        history = HistoryRelation(user=user, novel=novel_obj)
        history.save()

    path = (os.path.join('media',
                         chapter_obj.content.name)).replace("\\", "//")
    f = open(path, "r", encoding="utf8")

    context = {
        'content': f.read(),
        'title': chapter_obj.title,
        'novel_id': novel_id,
    }

    previous_chapter = Chapter.objects.filter(volumn__novel=novel_obj,
                                              id__lt=chapter_id).first()
    if previous_chapter:
        context['previous_chapter'] = previous_chapter.id

    next_chapter = Chapter.objects.filter(volumn__novel=novel_obj,
                                          id__gt=chapter_id).first()
    if next_chapter:
        context['next_chapter'] = next_chapter.id

    return show(request, 'novel/content.html', context)
