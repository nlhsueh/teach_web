from django.http import JsonResponse
from common.util.api_view import api_view
from apps.user.auth import login, get_user_data
from apps.novel.models import Novel
from .models import GoodRelation, BookcaseRelation, UserGradeRelation, Discussion

def get_novel(func):
    """decorator for getting the novel"""
    def handler(request, data, *args):
        novel = Novel.objects.get(id=data['novel_id'])
        if (novel == None):
            return JsonResponse({
                "status": "fail",
                "message": "novel not found"
            })
        return func(request, data, *args, novel)
    return handler


def get_good(result, user, novel):
    if user and GoodRelation.objects.filter(user=user, novel=novel).count() > 0:
        result["is_good"] = True
    else:
        result["is_good"] = False
    result["good_count"] = novel.goodrelation_set.count()

def get_bookmark(result, user, novel):
    if user and BookcaseRelation.objects.filter(user=user, novel=novel).count() > 0:
        result["is_in_bookcase"] = True
    else:
        result["is_in_bookcase"] = False

def get_grade(result, user, novel: Novel):
    if user:
        my_grade = UserGradeRelation.objects.filter(user=user, novel=novel).first()
        if my_grade:
            result["my_grade"] = my_grade.grade
        else:
            result["my_grade"] = 0
    else:
        result["my_grade"] = 0

    result["grade_chart"] = novel.get_grade_chart()

def get_discussion(result, novel: Novel, all=False):
    last_discussion = []
    if all:
        discussion_set = novel.get_discussion()
    else:
        discussion_set = novel.get_discussion()[0:3]

    for discussion in discussion_set:
        avatar = discussion.user.avatar
        if avatar:
            avatar = avatar.name
        else:
            avatar = None

        last_discussion.append({
            "avatar": avatar,
            "userid": discussion.user.id,
            "name": discussion.user.username,
            "date": discussion.datetime,
            "discussion": discussion.discuss
        })

    result["last_discussion"] = last_discussion


@api_view(method="POST", checked=["novel_id"])
@login
@get_novel
def set_good(request, data, user, novel):
    good = GoodRelation(user=user, novel=novel)
    good.save()

    result = {}
    result["status"] = "success"
    get_good(result, user, novel)

    return JsonResponse(result)

@api_view(method="POST", checked=["novel_id"])
@login
@get_novel
def set_bookcase(request, data, user, novel):
    bookcase = BookcaseRelation(user=user, novel=novel)
    bookcase.save()

    result = {}
    result["status"] = "success"
    get_bookmark(result, user, novel)

    return JsonResponse(result)

@api_view(method="POST", checked=["novel_id", "grade"])
@login
@get_novel
def update_grade(request, data, user, novel):
    grade = UserGradeRelation.objects.filter(user=user, novel=novel).first()
    if grade:
        grade.grade = data['grade']
    else:
        grade = UserGradeRelation(user=user, novel=novel, grade=data['grade'])
    grade.save()

    result = {}
    result["status"] = "success"
    get_grade(result, user, novel)
    
    return JsonResponse(result)

@api_view(method="POST", checked=["novel_id", "discuss"])
@login
@get_novel
def addDiscuss(request, data, user, novel):
    if data["discuss"]:
        discuss = Discussion(user=user, novel=novel, discuss=data["discuss"])
        discuss.save()

    result = {}
    result["status"] = "success"
    get_discussion(result, novel)
    
    return JsonResponse(result)

@api_view(method="GET", checked=["novel_id"])
@get_novel
def getDiscuss(request, data, novel):
    result = {}
    result["status"] = "success"
    get_discussion(result, novel, True)

    return JsonResponse(result)


@api_view(method="GET", checked=["novel_id"])
@get_novel
def get_novel_info(request, data, novel):
    user_data = get_user_data(request)
    
    result = {}
    result["status"] = "success"
    get_good(result, user_data, novel)
    get_bookmark(result, user_data, novel)
    get_grade(result, user_data, novel)
    get_discussion(result, novel)

    return JsonResponse(result)
