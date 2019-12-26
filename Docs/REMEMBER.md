유저모델 오버라이드 : 세팅에 대처모델 알려주기 / 추상유저모델 받기 / 어드민 등록 (유저앱 등록 / 앱등록 나누기)

#settings.py
AUTH_USER_MODEL = "users.User"

#users/models.py
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
