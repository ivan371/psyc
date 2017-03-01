from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from core.models import User, Psycologist, Client, Subscription


@admin.register(User)
class UserAdmin(BaseUserAdmin):

    fieldsets = (
        ('User info', {'fields': ('username', 'password', 'first_name', 'last_name', 'email', 'rating', 'avatar', 'city')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'email', 'first_name', 'last_name', 'is_staff', 'is_superuser', 'avatar', 'rating', 'city'),
        }),
    )
    def admin_avatar(self, instance):
        return instance.avatar and u'<img src="self.avatar" width="100px" />'.format(
            instance.avatar.url
        )
    admin_avatar.allow_tags = True

admin.site.register(Psycologist)
admin.site.register(Client)
admin.site.register(Subscription)
