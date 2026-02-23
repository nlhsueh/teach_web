from apps.user.auth import login_and_redirect
from novel_warehouse.views import show
from .models import BookcaseRelation, HistoryRelation
from apps.user.models import Subscribe

@login_and_redirect
def bookcase(request, user):
    book_list = BookcaseRelation.objects.filter(user=user).all()
    novel_list = [relation.novel for relation in book_list]
    
    context = {
       "novel_list": novel_list
    }
    return show(request, 'feedback/bookcase.html', context)

@login_and_redirect
def subscribe(request, user):
    subscribe_list = Subscribe.objects.filter(reader=user)

    context = {
       "subscribe_list": subscribe_list
    }
    return show(request, 'feedback/subscribe.html', context)

@login_and_redirect
def history(request, user):
    history_list = HistoryRelation.objects.filter(user=user).order_by('-datetime')
    novel_list = [relation.novel for relation in history_list]
    
    context = {
       "novel_list": novel_list
    }
    return show(request, 'feedback/history.html', context)

@login_and_redirect
def my(request, user):
    novel_list = HistoryRelation.objects.filter(user=user).order_by('-datetime')
    history_list = [relation.novel for relation in novel_list]

    novel_list = BookcaseRelation.objects.filter(user=user).all()
    bookcase_list = [relation.novel for relation in novel_list]

    subscribe = Subscribe.objects.filter(reader=user)
    subscribe_list = []
    for author in subscribe:
        work_set = author.author.work
        subscribe_list = subscribe_list + [novel for novel in work_set.all()]

    context = {
        "history_list": history_list,
        "bookcase_list": bookcase_list,
        "subscibe_list": subscribe_list,
    }

    return show(request, 'feedback/my.html', context)
