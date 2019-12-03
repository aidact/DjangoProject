from django.contrib import admin

from users.models import MainUser, Profile


@admin.register(MainUser)
class MainUserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'username',
        'email',
        'age'
    )

    fields = ('first_name', 'last_name', 'username', 'email', 'age', 'gender', 'height', 'weight')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user'
    )

    fields = ('user', 'bio', 'avatar')
