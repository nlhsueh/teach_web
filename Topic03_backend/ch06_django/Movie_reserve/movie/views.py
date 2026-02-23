# myapp/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import Movie, Seat
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy


@login_required
def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movie_list.html', {'movies': movies})

def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)

    return render(request, 'movie_detail.html', {'movie': movie})
# myapp/views.py

def seat_selection(request, movie_id):
    # Assuming a 10x10 seat layout
    rows = range(10)
    columns = range(10)

    # Retrieve the movie object
    movie = get_object_or_404(Movie, pk=movie_id)

    if request.method == 'POST':
        # Handle seat reservation
        selected_seat_ids = request.POST.get('selected_seats', '').split(',')
        for selected_seat_id in selected_seat_ids:
            seat = Seat.objects.get(pk=selected_seat_id)
            if not seat.is_booked:
                seat.is_booked = True
                seat.save()

        # Store selected seats in session
        request.session['selected_seats'] = selected_seat_ids

    else:
        # Retrieve selected seats from session
        selected_seat_ids = request.session.get('selected_seats', [])

    # Retrieve all seats for the movie
    seats = Seat.objects.filter(movie=movie)

    # Get the IDs of already booked seats
    booked_seat_ids = [seat.id for seat in seats if seat.is_booked]

    return render(request, 'seat_selection.html', {'seats': seats, 'rows': rows, 'columns': columns, 'movie': movie, 'booked_seat_ids': booked_seat_ids, 'selected_seat_ids': selected_seat_ids})

def confirm_seat(request):
    # 獲取查詢參數
    movie_title = request.GET.get('movieTitle', '')
    release_date = request.GET.get('releaseDate', '')
    time = request.GET.get('time', '')
    selected_seats = request.GET.get('selectedSeats', '').split(',')

    # 在這裡可以進行進一步的處理，例如檢查座位是否有效，從座位 ID 中解析行和列等

    # 傳遞信息到模板中
    context = {
        'movie_title': movie_title,
        'release_date': release_date,
        'time': time,
        'selected_seats': selected_seats,
    }

    return render(request, 'confirm_seat.html', context)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('movie_list')  # 修改這一行，使用你的首頁路徑名稱
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

class CustomLoginView(LoginView):
    success_url = reverse_lazy('movie_list')  # 將 'movie_list' 替換為你想要的URL