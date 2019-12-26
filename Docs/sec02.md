## section 02

# 2.0 프로젝트 시작하기

```js
django-admin startproject airbnb-clone 대신에
django-admin startproject config 을 실행한다.
그리고 config안의 파일들을 최상위 루트로 모두 뺀다.
django-admin startapp conversations | lists | reservatons | reviews | rooms |  users | core 를 만든다.

```

# 2.1 Linter(flake8) + formatter(black) == 프리 인터프리터/포멧터

- linter는 파이썬이 인터프리터이다보니, 코드를 읽다가 애러나 나면 터짐. Linter는 미리 코드를 읽고 애러가 생길부분을 미리 경고해준다.
- Python pep는 파이썬 스타일 규정이다. 이를 자동으로 만들어주는것이 linter이다.
- Linter으로 pylint랑 flake8이 있다. flake8를 쓴다. settings.json을 통해 확인.

```js
{
    "python.pythonPath": "C:\\Users\\Dos\\AppData\\Local\\Continuum\\anaconda3\\envs\\djangostack\\python.exe",
    "python.linting.pylintEnabled": false,
    "python.linting.flake8Enabled": true,
    "python.linting.enabled": true
}
```

- Formatter은 코드를 저장할때 예쁘게 바꿔주는것이다. black을 사용한다. settings.json 에 추가.

```js
pip install black

{
  "python.formatting.provider": "black"
}

```

- settings.py 를 보면 애러가 4개가 있는데, 코드줄이 너무 길다는 메시지다. 지금은 모니터로 다 보이므로 이런애러메시지는 제거하자. settings.json 에 추가.

```js
{
    "python.linting.flake8Args":["--max-line-length=88"]
}
```

# 2.2

- 폴더에 `__init__`.py는 파이썬파일들을 import해줄수있게 메타정보를 모은다.

# 2.3

```js
manage.py runserver
manage.py createsuperuser
manage.py makemigrations
manage.py migrate
```

# 2.4

- Django는 ORM덕분에 모델만 짜면, 알아서 여러종류의 DB들의 언어로 변환되어서 작동한다.

# 2.5

- Django 어플리케이션 = function group 이다. 함수들의 그룹, 관련있는 한문장으로 서술되는 함수들의 그룹
- 예를들어)|Room 방을 수정하기,보기,검색하기,삭제하기, 모든 방 검색, 업로드 하기 기능 |Megs 사용자를 검색하고 메시지 보내고, 응답하고 |

# 2.6

- manage.py startapp rooms|users|reviews|conversations|lists|reservations

# 2.7
