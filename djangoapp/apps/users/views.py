from django.contrib import messages
from django.shortcuts import render
from django.shortcuts import redirect
from apps.users.forms import registerForm, loginForm
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model
# Create your views here.


def login_User(request):
    form = loginForm()
    if request.method == 'POST':
        form = loginForm(request.POST)
        if form.is_valid():
            store_email_login = form.cleaned_data['store_email_login']
            store_password_login = form.cleaned_data['store_password_login']
            user = auth.authenticate(request, email=store_email_login, password=store_password_login)
            if user is not None:
                auth.login(request, user),
                messages.success(request, 'You are now logged in!')
                return redirect('index')
            else:
                messages.error(request, 'Invalid email or password.'),
                return redirect('login_user')

    return render(request, 'users/login.html', {'form': form})


@csrf_exempt
def create_User(request):
    form = registerForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            name_register = form['store_name'].value()
            email_resgister = form['store_email'].value()
            password_register = form['store_password_confirmation'].value()
            if User.objects.filter(email=email_resgister).exists():
                messages.error(request, 'Email already registered.')
                return redirect('create_user')
            new_store = User.objects.create_user(
                username=name_register,
                email=email_resgister,
                password=password_register,
            )
            new_store.save()
            messages.success(request, 'Your account has been created.')
            return redirect('login_user')
    return render(request,
                  'users/register.html',
                  {'form': form}, )

@csrf_exempt
def logout_User(request):
    auth.logout(request)
    messages.success(request, 'Logout efetuado com sucesso!')
    return redirect("login_user")

