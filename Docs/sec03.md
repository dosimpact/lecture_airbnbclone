# section 03

# 3.0 Replacing Default User (11:23)

- 기본 User모델을 오버라이드해서 사용하기.  
  [참조 문서](https://docs.djangoproject.com/en/2.2/topics/auth/customizing/)

```python
Substituting a custom User model¶
Some kinds of projects may have authentication requirements for which Django’s built-in User model is not always appropriate. For instance, on some sites it makes more sense to use an email address as your identification token instead of a username.

Django allows you to override the default user model by providing a value for the AUTH_USER_MODEL setting that references a custom model:

AUTH_USER_MODEL = 'myapp.MyUser'
This dotted pair describes the name of the Django app (which must be in your INSTALLED_APPS), and the name of the Django model that you wish to use as your user model.
```

```python
#settings.py
AUTH_USER_MODEL = "users.User"

#users/models.py
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):

#users앱추가 및 기본앱과 분리하기.

```

# 3.1 Introduction to the User Model (8:02)

- 모델에 TextField추가하기

```
#admin 패널 등록
from . import models
@admin.register(models.User)
class CustomUserAdmin(admin.ModelAdmin)

#모델에 필드 추가
bio = models.TextField(default="") | .TextField(null = True)
DB에 들어가는데, 기본값을 설정해 주거나, 또는 null을 허용해 주어야 한다.
```

# 3.2 First Model Fields (11:49)

```
#모델에, 이미지 필드, charfield, text필드등을 넣어서,

#text필드에 choice 간단하게 넣어서 커스텀 하기.!
```

# 3.3 Finishing User Model (7:15)

- User모델의 항목들을 완성합니다.

```
avatar | gender | bio | birthdate | language | currency | superhost
```

# 3.4 Falling in Love with Admin Panel (9:12)

- 1. 만들 모델을 어드민 패널에 적용시키기 , decorator를 이용해서 나타내기

```
from django.contrib import admin
from .models import Author #내가 만든 모델을 임포트 해서

@admin.register(Author) #여기다가 등록시키기
class AuthorAdmin(admin.ModelAdmin): #이미 만들어진 admin 패널을 상속받아 클래스를 만들기.
    pass

```

- 2. admin패널에 나올 필터와, 디스플레이 속성들을 설정해 준다.

```
@admin.register(models.User)
class CustomUserAdmin(admin.ModelAdmin):
    """ Custom User Admin """

    list_display = ("username", "email", "gender", "language", "currency", "superhost")
    list_filter = ("language",)
```

- 3. UserAdmin 만들어진 패널을 가져와서 적용시킨다.

```
@admin.register(models.User)
class CustomUserAdmin(UserAdmin):  # class CustomUserAdmin(admin.ModelAdmin):
    """ Custom User Admin """
    # list_display = ("username", "email", "gender", "language", "currency", "superhost")
    # list_filter = ("language",)
    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                )
            },
        ),
    )
```

# 3.5 UserAdmin + CustomAdmin (6:15)

# 3.6 RECAP OMG! (11:02)
