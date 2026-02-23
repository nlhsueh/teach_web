from django.urls import path
from . import views

urlpatterns = [
    path('novel/<int:novel_id>', views.novel_view),
    path('novel/<int:novel_id>/<int:chapter_id>', views.content_view),
    path('novel/<int:novel_id>/catalog', views.catalog_view),
]
