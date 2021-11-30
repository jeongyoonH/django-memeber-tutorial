from django.contrib import admin
from .models import Test, Token

@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ("date","title", "content")

@admin.register(Token)
class TokenAdmin(admin.ModelAdmin):
    list_display = ("id", "JWT")
