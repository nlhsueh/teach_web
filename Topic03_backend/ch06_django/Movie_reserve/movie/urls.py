from django.urls import path
from .views import movie_list, movie_detail, seat_selection, confirm_seat
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from .views import signup
from .views import CustomLoginView

urlpatterns = [
    path('', login_required(movie_list), name='movie_list'),
    path('movies/<int:movie_id>/', movie_detail, name='movie_detail'),
    path('movies/<int:movie_id>/seat_selection/', seat_selection, name='seat_selection'),
    path('confirm_seat/', confirm_seat, name='confirm_seat'),
    path('login/', CustomLoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('signup/', signup, name='signup'),
    # 其他路徑
]
