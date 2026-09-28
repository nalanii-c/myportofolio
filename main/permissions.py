from functools import wraps
from django.contrib.auth.views import redirect_to_login
from django.core.exceptions import PermissionDenied


def perm_required(perm):
    """Anonim -> redirect ke login. Sudah login tapi tidak berhak -> 403."""
    def decorator(view):
        @wraps(view)
        def wrapper(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return redirect_to_login(request.get_full_path())
            if not request.user.has_perm(perm):
                raise PermissionDenied
            return view(request, *args, **kwargs)
        return wrapper
    return decorator