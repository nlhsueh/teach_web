from django.urls import path
from . import api, views

urlpatterns = [
    path('feed/bookcase/', views.bookcase),
    path('feed/subscribe/', views.subscribe),
    path('feed/history/', views.history),
    path('feed/my/', views.my),

    path('api/novel/info', api.get_novel_info),
    path('api/novel/setGood', api.set_good),
    path('api/novel/setBookcase', api.set_bookcase),
    path('api/novel/updateGrade', api.update_grade),
    path('api/novel/addDiscuss', api.addDiscuss),
    path('api/novel/getDiscuss', api.getDiscuss),
]
