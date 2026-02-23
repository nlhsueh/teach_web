from django.http import JsonResponse
from common.util.api_view import api_view
from .auth import login, get_user_data
from .models import User, Subscribe

def get_subscribe(result, reader, author):
    if reader and Subscribe.objects.filter(reader=reader, author=author).first():
        result["is_subscribe"] = True
    else:
        result["is_subscribe"] = False

@api_view(method="POST", checked=["author_id"])
@login
def subscribe(request, data, user):    
    author = User.objects.get(id=data['author_id'])
    Subscribe.objects.create(reader=user, author=author)

    result = {}
    result["status"] = "success"
    get_subscribe(result, user, author)

    return JsonResponse(result)

@api_view(method="GET", checked=["author_id"])
def getSubscribe(request, data):    
    author = User.objects.get(id=data['author_id'])
    reader = get_user_data(request)

    result = {}
    result["status"] = "success"
    get_subscribe(result, reader, author)

    return JsonResponse(result)
