# 에어비엔비 클론 코딩

## section3

- Django의 기본 user모델을 커스터마이징 하여 사용합니다.
- 모델에서 텍스트필드에 3가지 선택권을 줍니다.
- admin에 DB 디스플레이를 설정합니다.

```
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    bio = models.TextField(default="")

AUTH_USER_MODEL = "users.User"

from django.contrib import admin
from . import models

@admin.register(models.User)
class CustomUserAdmin(admin.ModelAdmin):
    pass

```

- 데이터 베이스 모델에서는 디폴트값이나 null = true을 줘야 한다.

```
    bio = models.TextField(default="")
    #bio = models.TextField(null=True)
```

## section 4

- 4.1
- core라는 앱을 만들었고, 여기서 모든 앱에서 사용되는 공통된 추상모델을 정의할꺼임. room의 모델은 이를 상속받는다.
- django countries 라는 오픈소스를 통해서 나라관련 데이터필드를 만들어 줄것이다.

```
from django.db import models #1.장고 관련 된것을 모두 임포트
from core import models as core_models #2. 서드파티 패키지 임포트
from django_countries.fields import CountryField #3. 그다음 내가 만든것 임포트


class Room(core_models.TimeStampedModel):
    """ Room Models """

    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()


```

- rooms 모델 완성 및 admin site 등록 완료, host는 Foreign 키 이용
- 4.2
- 4.5
- verbose_name 메타 클래스에 추가해서, 자동으로 클래스 이름이 바뀌는것을 컨트롤 한다.
