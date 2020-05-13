from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin

# Register your models here.

# Models
from django.contrib.auth.models import User
from posts.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'profile', 'title', 'photo')
    list_display_links = ('pk', 'user')

    search_fields = ('user__username', 'title',)
    list_filter = (
        'created',
        'modified',
        'user__is_active',
        'user__is_staff'
        )
    readonly_fields = ('created', 'modified', 'user')

    fieldsets = (
        ('Post', {
            'fields': (('title', 'photo'),)
        }),

        ('Metadata', {
            'fields': (
                ('user',),
                ('created', 'modified'),
            )
        })
    )