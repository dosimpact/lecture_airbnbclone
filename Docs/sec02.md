## section 02

- #2.0 프로젝트 시작하기

```
django-admin startproject airbnb-clone 대신에
django-admin startproject config 을 실행한다.
그리고 config안의 파일들을 최상위 루트로 모두 뺀다.
 createapp 으로 conversations,lists,reservatons,reviews,rooms, users 를 만든다.

```

- #2.1 Linter(flake8) + formatter(black) == 프리 인터프리터/포멧터

- linter는 파이썬이 인터프리터이다보니, 코드를 읽다가 애러나 나면 터짐. Linter는 미리 코드를 읽고 애러가 생길부분을 미리 경고해준다.
- Python pep는 파이썬 스타일 규정이다. 이를 자동으로 만들어주는것이 linter이다.
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

- #2.2

- 폴더에 `__init__`.py는 파이썬파일들을 import해줄수있게 메타정보를 모은다.
