from django.shortcuts import render
from apps.user.auth import get_user_data


def show(request, template_name: str, context={}):
    context['user'] = get_user_data(request)

    return render(request, template_name, context)


def handler404(request, *args, **argv):
    response = show(request, '404.html')
    response.status_code = 404
    return response
