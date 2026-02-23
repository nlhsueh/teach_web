from django.urls import path
from . import views

urlpatterns = [
    path('studio/work/', views.work),
    path('studio/new/', views.new),
    path('studio/novel/<int:novel_id>', views.novel),
    path('studio/catalog/<int:novel_id>', views.catalog),
    path('studio/volumn/<int:novel_id>', views.volumn),
    path('studio/chapter/<int:novel_id>', views.chapter),
]
