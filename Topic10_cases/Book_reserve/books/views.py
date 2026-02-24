from django.http import HttpResponse
from django.template import loader
from .models import Book
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def books(request):
  mybooks = Book.objects.all().values()
  template = loader.get_template('all_books.html')
  context = {
    'mybooks': mybooks,
  }
  return HttpResponse(template.render(context, request))

def details(request, id):
  mybook = Book.objects.get(id=id)
  template = loader.get_template('book_details.html')
  context = {
    'mybook': mybook,
  }
  return HttpResponse(template.render(context, request))

def main(request):
  book1 = Book.objects.get(bookname="遊戲人生 01")
  book2 = Book.objects.get(bookname="射鵰英雄傳(一)")
  book3 = Book.objects.get(bookname="系統程式設計(上册)")
  book4 = Book.objects.get(bookname="系統程式設計(下册)")
  template = loader.get_template('main.html')
  context = {
    'book1': book1,
    'book2': book2,
    'book3': book3,
    'book4': book4,
  }
  return HttpResponse(template.render(context))

@login_required
def borrow(request):
  if request.method == 'POST':
    isbn = request.POST.get('ISBN', '')

    try:
      book = Book.objects.get(ISBN=isbn)
      b_title = book.bookname

      if book.lastQuantity > 0:
        book.lastQuantity -= 1
        book.save()

        message = f'已借出《{b_title}》'
        return render(request, 'borrow.html', {'success': message})
      else:
        return render(request, 'borrow.html', {'error': '架上數量不足'})

    except Book.DoesNotExist:
      return render(request, 'borrow.html', {'error': '書籍不存在'})

  return render(request,'borrow.html')

@login_required
def return_book(request):
  if request.method == 'POST':
    isbn = request.POST.get('ISBN', '')

    try:
      book = Book.objects.get(ISBN=isbn)
      b_title = book.bookname

      if book.lastQuantity < book.maxQuantity:
        book.lastQuantity += 1
        book.save()

        message = f'已歸還《{b_title}》'
        return render(request, 'return_book.html', {'success': message})
      else:
         return render(request, 'return_book.html', {'error': '本館所持有的此書已全數歸還'})

    except Book.DoesNotExist:
      return render(request, 'return_book.html', {'error': '書籍不存在'})

  return render(request,'return_book.html')