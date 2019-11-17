# 에어비엔비 클론 코딩

## 환경설치

- 아나콘다 + VS code

```
conda create djangostack python==3.7
conda activate djangostack
pip install Django
pip list
```

```
vs code -> 컨트롤 쉬프트 P => select python interpretor djangostack ~
```

## Django VS

- Flask vs Django  
  Flask나 Pyrmaid 매우 간단하고 쉽게 웹 어플리케이션을 만들 수 있다. Flask는 웹서버 만드는 것을 많이 도와준다.  
  하지만 reinvent the wheel 데이터베이스 유저인증 form 로그인 로그아웃, 관리자 패널 등등  
  다시 직접 만들어야 하는 많은 부분이 있다.

  Django는 거대한 프레임 워크라서 공통적으로 필요한것들을 전부 넣었다. 그래서 처음부터 많은것들이 포함되어 있다.  
  컨텐츠관리기능, 이미 관리자 패널이 있다. 사용자 인증도 사이트맵도. 이미 만들어진 form들을 가지고 쉽게 메일인증도 할 수 있다.  
  배워야하는 큰 박스이다. 한번 배운순간 생산성이 급격히 올라간다. 장고의 매력적인 부분이다.

airbnb에 사용하는 수많은 기능들을 django가 많이 지원하기 때문에 좋다.  
메가 프레임워크 vs 마이크로 프레임 워크  
메가 프레음워크(장고)는 내부에 많은 결정들이 있다. 반면 마이크로 프레임워크는 내가 많은 주도권을 가지고 있지만 직접 건드려야되서 시간이 많이 걸릴것이다.

- React vs Django  
  django를 쓰는사람: 인스타그램 only API, 핀터레스트 only API, 에어비엔비 콘텐츠 위주, API제공에 있어 django를 많이 쓴다.  
  react를 쓰는 사람: 인스타그램, 핀터레스트 - 페이지 새로고침없이 많은 인터렉트가 필요하다.

## section 01

- pipenv 이용해 가상환경 만들고 Django 설치하기.

- gitignore python 만듬.

## section 02

-

```
django-admin startproject airbnb-clone 대신에
django-admin startproject config
 createapp 으로 conversations,lists,reservatons,reviews,rooms, users 를 만든다.

```

- flake8 + black == 프리인터프리터/포멧터

- linter는 파이썬이 인터프리터이다보니, 코드를 읽다가 애러나 나면 터짐. Linter는 미리 코드를 읽고 애러가 생길부분을 미리 경고해준다.
- pep는 파이썬 스타일 규정이다.
- Linter으로 pylint랑 flake8이 있다. flake8를 쓴다. settings.json을 통해 확인.

```
{
    "python.pythonPath": "C:\\Users\\Dos\\AppData\\Local\\Continuum\\anaconda3\\envs\\djangostack\\python.exe",
    "python.linting.pylintEnabled": false,
    "python.linting.flake8Enabled": true,
    "python.linting.enabled": true
}
```

- Formatter은 코드를 저장할때 예쁘게 바꿔주는것이다. black을 사용한다. settings.json 에 추가.

```
pip install black
```

```
{
  "python.formatting.provider": "black"
}

```

- settings.py 를 보면 애러가 4개가 있는데, 코드줄이 너무 길다는 메시지다. 지금은 모니터로 다 보이므로 이런애러메시지는 제거하자. settings.json 에 추가.

```
{
    "python.linting.flake8Args":["--max-line-length=88"]
}
```

- 폴더에 `__init__`.py는 파이썬파일들을 import해줄수있게 메타정보를 모은다.

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
