from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        messages.error(request, 'You are not logged in!')
        return redirect('login_user')
    return render(request, 'stock/index.html')