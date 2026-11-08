from functools import wraps

from django.contrib.auth.views import redirect_to_login
from django.core.exceptions import PermissionDenied
from rest_framework.permissions import BasePermission, SAFE_METHODS


def perm_required(perm):
    """Anonim diarahkan ke login; pengguna tanpa izin mendapat 403."""
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


class IsPortfolioOwnerOrEditorOrReadOnly(BasePermission):
    message = "You do not have permission to perform this action."

    def has_permission(self, request, view):
        user = request.user

        # Semua pengguna boleh membaca.
        if request.method in SAFE_METHODS:
            return True

        # Pengguna anonim tidak boleh menulis.
        if not user.is_authenticated:
            return False

        # Owner (superuser) boleh melakukan semua operasi.
        if user.is_superuser:
            return True

        # Editor dengan change_project hanya boleh PATCH.
        if request.method == "PATCH":
            return user.has_perm("main.change_project")

        return False
