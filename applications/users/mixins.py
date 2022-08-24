from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect

from .models import User


def check_rol_user(rol, user_rol):
    
    if (rol == User.SUPERUSUARIO or rol == user_rol):
        
        return True
    else:
        return False


class AdminPermisionMixin(LoginRequiredMixin):
    login_url = reverse_lazy('users_app:user-login')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        
        if not check_rol_user(request.user.rol, User.ADMIN):
            return HttpResponseRedirect(
                reverse('users_app:user-login')
            )

        return super().dispatch(request, *args, **kwargs)


class SuperUserPermisionMixin(LoginRequiredMixin):
    login_url = reverse_lazy('users_app:user-login')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        
        if not check_rol_user(request.user.rol, User.SUPERUSUARIO):
            return HttpResponseRedirect(
                reverse('users_app:user-login')
            )
        return super().dispatch(request, *args, **kwargs)
        
