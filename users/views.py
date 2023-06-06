from django.shortcuts import render,redirect

# Create your views here.
from users.forms import LoginForm,RegisterForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.views.generic import FormView, View


# def auth_view(request):
#     if request.method == "GET":
#         context = {
#             'form': LoginForm
#         }
#
#         return render(request, 'users/auth.html', context=context
#                       )
#     if request.method == "POST":
#         data = request.POST
#         form =LoginForm(data=data)
#
#         if form.is_valid():
#             user = authenticate(username=form.cleaned_data.get("username"),
#                                 password=form.cleaned_data.get('password'))
#             if user:
#                 login(request,user)
#                 return redirect('/products/')
#             else:
#                 form.add_error('username','incorrect data')
#
#         return render(request,'users/auth.html',context={
#             'form':form
#         })


class AuthView(FormView):
    form_class = LoginForm
    template_name = 'users/auth.html'
    success_url = '/products/'

    def form_valid(self, form):
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)

        if user:
            login(self.request, user)
            return super().form_valid(form)
        else:
            form.add_error('username', 'Incorrect data')
            return self.form_invalid(form)


# def register_view(request):
#     if request.method == "GET":
#         context = {
#             'form': RegisterForm
#         }
#
#         return render(request,'users/register.html',context=context)
#
#     if request.method == "POST":
#         data = request.POST
#         form = RegisterForm(data=data)
#
#         if form.is_valid():
#             if form.cleaned_data.get('password1') == form.cleaned_data.get('password2'):
#                 user = User.objects.create_user(
#                     username=form.cleaned_data.get('username'),
#                     password=form.cleaned_data.get('password1')
#                 )
#
#                 login(request, user)
#                 return redirect('/products/')
#             else:
#                 form.add_error('password1', 'password1 != password2')
#
#         return render(request, "users/register.html", context={
#             'form': form
#         })


class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'users/register.html'
    success_url = '/products/'

    def form_valid(self, form):
        if form.cleaned_data.get('password1') == form.cleaned_data.get('password2'):
            user = User.objects.create_user(
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password1')
            )

            login(self.request, user)
            return super().form_valid(form)
        else:
            form.add_error('password1', 'Passwords do not match')
            return self.form_invalid(form)




# def logout_view(request):
#     logout(request)
#     return redirect('/products/')



class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('/products/')