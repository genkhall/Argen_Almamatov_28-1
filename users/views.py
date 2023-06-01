from django.shortcuts import render,redirect

# Create your views here.
from users.forms import LoginForm,RegisterForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User


def auth_view(request):
    if request.method == "GET":
        context = {
            'form': LoginForm
        }

        return render(request, 'users/auth.html', context=context
                      )
    if request.method == "POST":
        data = request.POST
        form =LoginForm(data=data)

        if form.is_valid():
            user = authenticate(username=form.cleaned_data.get("username"),
                                password=form.cleaned_data.get('password'))
            if user:
                login(request,user)
                return redirect('/products/')
            else:
                form.add_error('username','incorrect data')

        return render(request,'users/auth.html',context={
            'form':form
        })

def register_view(request):
    if request.method == "GET":
        context = {
            'form': RegisterForm
        }

        return render(request,'users/register.html',context=context)

    if request.method == "POST":
        data = request.POST
        form = RegisterForm(data=data)

        if form.is_valid():
            if form.cleaned_data.get('password1') == form.cleaned_data.get('password2'):
                user = User.objects.create_user(
                    username=form.cleaned_data.get('username'),
                    password=form.cleaned_data.get('password1')
                )

                login(request, user)
                return redirect('/products/')
            else:
                form.add_error('password1', 'password1 != password2')

        return render(request, "users/register.html", context={
            'form': form
        })

def logout_view(request):
    logout(request)
    return redirect('/products/')