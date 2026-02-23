from django.db.models import Q
from novel_warehouse.views import show
from apps.novel.models import Novel
from apps.user.models import User
from apps.novel.models import TagRelation

def search(request):
    context = {
        "question": "",
        "result": None
    }

    q = request.GET.get('q')
    field = request.GET.get('field')

    if field == 'tag':
        tag_relation = TagRelation.objects.filter(tag__tagname=q).all()
        result = [relation.novel for relation in tag_relation]

        context['question'] = f"You are searching for tag {q}"
        context['result'] = result
    elif field == 'user':
        author = User.objects.get(id=q)
        novels = Novel.objects.filter(author__id=q)

        if novels:
            context['question'] = f"You are searching for author {author.username}"
            context['result'] = novels
        else:
            context['question'] = f"You are searching for author with wrong id"
    else:
        novels = Novel.objects.filter(Q(title__contains=q) | Q(author__username__contains=q))
        tag_relation = TagRelation.objects.filter(tag__tagname__contains=q)

        result = list(set([novel for novel in novels] + [relation.novel for relation in tag_relation]))

        context['question'] = f"You are searching for {q}"
        context['result'] = result

    return show(request, 'search/search.html', context)
