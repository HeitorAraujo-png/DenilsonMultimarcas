from functools import wraps
from django.shortcuts import redirect
def admin_required(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        if not (request.user.is_superuser or request.user.is_staff or request.user.is_active or request.user.is_authenticated):
            return redirect('home')
        return func(request, *args, **kwargs)
    return wrapper