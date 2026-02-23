from django.http import JsonResponse
from django.shortcuts import redirect
from .models import User

def get_user_data(request):
    if (request.session.get('is_login')):
        account = request.session.get('account')
        user_obj = User.objects.filter(account=account).first()
        
        return user_obj
    return None

def login(func):
    """login decorator, checks if user is logged in, and returns user data"""
    def handler(request, *args):
        user = get_user_data(request)
        if (user == None):
            return JsonResponse({
                "status": "denied"
            })
        return func(request, *args, user)
    return handler

def login_and_redirect(func):
    """login decorator, checks if user is logged in, and returns user data"""
    def handler(request, *args):
        user = get_user_data(request)
        if (user == None):
            return redirect('/login/')
        return func(request, *args, user)
    return handler
