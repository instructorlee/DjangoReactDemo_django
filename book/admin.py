from django.contrib import admin

from .models import Member, Book


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    pass


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass
