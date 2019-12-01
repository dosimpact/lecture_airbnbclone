from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("Custom profiles", {"fields": ("avatar", "gender", "bio")}),
    )
    list_filter = UserAdmin.list_filter + ("superhost",)
    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "language",
        "currency",
        "superhost",
        "is_staff",
        "is_superuser",
    )
    # 데코레이터라고 , 꼭 class위에 써 주어야 한다.
    # 아니면, admin.site.register(models.User,CustomUserAdmin)으로 등록해도 된다.
    # @admin.register(models.User)
    # class CustomUserAdmin(admin.ModelAdmin):
    """ Custom User Admin """

    # admin 페이지 꾸미기
    # list_display = ("username", "email", "gender", "language", "currency", "superhost")
    # list_filter = ("superhost", "currency", "superhost")
