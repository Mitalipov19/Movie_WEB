from rest_framework import permissions
from .models import *


class CheckStatus(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.status_movie == 'simple':
            return True
        elif obj.status_movie == 'pro':
            return bool(
                Profile.status == 'pro'
            )

