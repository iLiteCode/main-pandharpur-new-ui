from django.contrib import admin
from django.core.exceptions import PermissionDenied
from .models import Image, Advertisement

class ImageAdmin(admin.ModelAdmin):
    list_display = ('heading', 'description')
    search_fields = ('heading', 'description')

    def has_change_permission(self, request, obj=None):
        if not request.user.is_superuser or not request.user.is_verified:
            raise PermissionDenied("You are not verified or you don't have authority to make this change.")
        return super().has_change_permission(request, obj)

    def has_add_permission(self, request):
        if not request.user.is_superuser or not request.user.is_verified:
            raise PermissionDenied("You are not verified or you don't have authority to add this entry.")
        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        if not request.user.is_superuser or not request.user.is_verified:
            raise PermissionDenied("You are not verified or you don't have authority to delete this entry.")
        return super().has_delete_permission(request, obj)

class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'is_google_adsense', 'position', 'status')
    list_filter = ('is_google_adsense', 'position', 'status')
    search_fields = ('title',)

    def has_change_permission(self, request, obj=None):
        if not request.user.is_superuser or not request.user.is_verified:
            raise PermissionDenied("You are not verified or you don't have authority to make this change.")
        return super().has_change_permission(request, obj)

    def has_add_permission(self, request):
        if not request.user.is_superuser or not request.user.is_verified:
            raise PermissionDenied("You are not verified or you don't have authority to add this entry.")
        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        if not request.user.is_superuser or not request.user.is_verified:
            raise PermissionDenied("You are not verified or you don't have authority to delete this entry.")
        return super().has_delete_permission(request, obj)

# Register models with custom permissions check
admin.site.register(Image, ImageAdmin)
admin.site.register(Advertisement, AdvertisementAdmin)
