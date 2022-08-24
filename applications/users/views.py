from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect

from django.views.generic import(
    View, 
    ListView,
    UpdateView,
    DeleteView
    )

from django.views.generic.edit import(FormView)

from .serializers import UserSerializer

from .forms import(
    LoginForm, 
    UpdatePasswordForm, 
    UserRegisterForm,
    ) 

from rest_framework.generics import(
    ListAPIView,
    )

from .models import User

# Create your views here.


class UsersListView(ListView):
    template_name = "users/list_users.html"
    context_object_name = 'usuarios' 
       
    def get_queryset(self):
        lista = User.objects.all()
        return lista
    
    def get_context_data(self, **kwargs):
        context = super(UsersListView, self).get_context_data(**kwargs)
        context["users"] = User.objects.all()
        return context

class UsersListApiView(ListAPIView):

    serializer_class = UserSerializer
    
    def get_queryset(self):
        return User.objects.all()

class UserRegisterView(FormView):
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('home_app:home')

    def form_valid(self, form):
        
        usuario = User.objects.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['email'],
            form.cleaned_data['password1'],
            name = form.cleaned_data['name'],
            last_name = form.cleaned_data['last_name'],
            phone = form.cleaned_data['phone'],
        )

        return HttpResponseRedirect(
            reverse('home_app:home'),
            kwargs={'pk': usuario.id}
        )
                
        
class Login(FormView):
    template_name = 'users/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home_app:home')
    
    def form_valid(self, form):
        
        user = authenticate(
            username= form.cleaned_data['username'],
            password= form.cleaned_data['password'],
        )
        login(self.request, user)
        return super(Login, self).form_valid(form)


class LoguotView(View):
    
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(
            reverse('users_app:user-login')
        )
        
class UpdatePasswordView(LoginRequiredMixin, FormView):
    template_name = 'users/update_pass.html'
    form_class = UpdatePasswordForm
    success_url = reverse_lazy('users_app:user-login')
    login_url = reverse_lazy('users_app:user-login')
    
    def form_valid(self, form):
        usuario = self.request.user
        
        user = authenticate(
            username = usuario.username,
            password = form.cleaned_data['password1']
        )
        
        if user:
            new_password = form.cleaned_data['password2']
            usuario.set_password(new_password)
            usuario.save()
            
        logout(self.request)
        return super(UpdatePasswordView, self).form_valid(form)
    
    
class UserUpdateView(UpdateView):
    template_name = "users/update.html"
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('home_app:home')


class UserDeleteView(DeleteView):
    template_name = "users/delete.html"
    model = User
    success_url = reverse_lazy('users_app:user-register')