from django.urls import path
from . import views, api

urlpatterns = [
    path('login/', views.login_view),
    path('signup/', views.signup_view),
    path('logout/', views.logout_view),
    path('profile/', views.profile_view),
    path('theme/', views.change_theme_view),

    path('api/user/getSubscribe', api.getSubscribe),
    path('api/user/subscribe', api.subscribe),
]
