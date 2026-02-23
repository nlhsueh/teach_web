from django.shortcuts import redirect
from novel_warehouse.views import show
from .auth import login_and_redirect
from .forms import LoginForm, SignupForm, ProfileForm
from .models import User

def login_view(request):
    # return the login form
    if request.method == "GET":
        return show(request, 'user/login.html')

    # "POST", submit the login form
    form = LoginForm(request.POST)

    # if all fields are valid
    if form.is_valid():
        user_obj = form.user_obj

        # set login session
        request.session['is_login'] = True
        request.session['account'] = user_obj.account

        print(request.GET.get("redirect"))
        path = request.GET.get("redirect") or "/feed/my/"
        return redirect(path)
    
    # return error message
    else:
        print(form.errors)
        clear_errors = form.errors.get("__all__")
        return show(request, "user/login.html", {"form": form, "form_messages": clear_errors})

def signup_view(request):
    if request.method == "GET":
        return show(request, "user/signup.html")

    else:
        form = SignupForm(request.POST, request.FILES)

        if form.is_valid():
            data = form.cleaned_data
            user = User(username=data['username'],
                        account=data['account'],
                        password=data['password'])
            user.save()

            return redirect('/login/')
        
        else:
            clear_errors = form.errors.get("__all__")

            return show(request, "user/signup.html", {
                "form": form,
                "form_messages": clear_errors
            })

def logout_view(request):
    request.session.flush()

    return redirect('/login/')

@login_and_redirect
def change_theme_view(request, user):
    user.change_theme()
    user.save()

    path = request.GET.get("redirect") or "/user/"
    return redirect(path)

@login_and_redirect
def profile_view(request, user):
    if request.method == 'GET':
        return show(request, "user/profile.html")
    else:
        form = ProfileForm(request.POST, request.FILES)

        if form.is_valid():
            data = form.cleaned_data
            user.username = data['username']
            user.password = data['password']
            user.description = data['description']
            if data['avatar']:
                user.avatar = data['avatar']
            user.save()

            return redirect('/profile/')
        else:
            clear_errors = form.errors.get("__all__")

            return show(request, "user/profile.html", {
                        "form": form,
                        "form_messages": clear_errors
                    })
