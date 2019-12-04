# section 10

# 10.0 Introduction to Urls and Views (8:02)

- url 과 view , 많은 url request가 올텐데, 라우팅을 잘 해야됨 | include(url 라우팅 !)

```
#config - urls
from django.contrib import admin
from django.urls import path, include #include를 통해, url를 라우팅 한다.

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", include("core.urls")), # " 빈 url요청시, core.urls로 가라,
    path("admin/", admin.site.urls)
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

```
#core - urls
from django.urls import path
from rooms import views as room_views #실질적인 뷰 클래스르 가져와서

app_name = "core"

urlpatterns = [path("", room_views.all_rooms, name="home")] # 클래스.함수 로 view 연결!!
```

```
#rooms - views
from django.shortcuts import render
def all_rooms(request):
    pass
```

# 10.1 HttpResponse and render (6:30)

# 10.2 Introduction to Django Templates (9:14)

- BASE_DIR | templates | conversatinos,emails ... base.html, 404.html | all_room.html 이런식으로, 템플릿을 모아둔 폴덜르 지정

```cs
TEMPLATES = [
    {
    ....
        "DIRS": [os.path.join(BASE_DIR, "templates")],
         #원래 내가 알던지식으로는 각 application마다 template를 보관했는데, 너무 불편하니까 | 이렇게 새로운 폴더를 지정하는거지.
```

- httpResponse를 통해 내용을 전달해도됨 | render는 (request | html | context... )를 통해 html를 만들어 제공한다.

```python
from datetime import datetime
from django.shortcuts import render

def all_rooms(request):
    now = datetime.now()
    hungry = True
    return render(request, "all_rooms.html", context={"now": now, "hungry": hungry})
```

- html 템플릿 내용~

```cs
<h1>hellow !~</h1>
<h4>NOW TIME : {{now}}</h4>
<h3>
  {% if hungry %} I m hungry ~ {% else %} im ok~{% endif %}
</h3>

```

# 10.3 Extending Templates part One (8:46)

- extension django template 설치해서 html 자동완성 쓸것. vs code아래 보면 html 을 django html template로 인식 | template 문법 자동완성기능 쓰기!!

```
#- 파일구조 :
 templates | base.html
 templates | rooms | home.html
def all_rooms(request):
    rooms = models.Room.objects.all()
    return render(request, "rooms/home.html", context={"rooms": rooms})

```

```

{% extends "base.html" %}


{% for room in rooms  %}
  <h4> {{room.name }}</h4>
{% endfor %}

```

# 10.4 Extending Templates part Two and Includes (8:59)

- templates파일 구조

templates | base.html
templates | partials | footer.html , header.html
templates | rooms | home.html

- footer.html + header.html ===> base로 include ===> home로 extends

```html
footer.html
<footer>&copy; Nomad airbnb</footer>
```

```html
header.html
<header>
  <a href="/">Nbnb</a>
  <ul>
    <li><a href="#">Login</a></li>
  </ul>
</header>
```

- {% black var %} {% endblock var %} | {% include "partials/footer.html" %} : 경로를 적어둔다.

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta http-equiv="X-UA-Compatible" content="ie=edge" />
    <title>{% block page_name %} {% endblock page_name %} | air bnb</title>
  </head>
  <body>
    {% include "partials/header.html" %} {% block content %} {% endblock content
    %} {% include "partials/footer.html" %}
  </body>
</html>
```

- {% extends "base.html" %} : 경로를 적어주고 +> {% block var %} {% endblock var %}

```

{% extends "base.html" %}

{% block page_name %}
  Home
{% endblock page_name %}

{% block content %}
  {% for room in rooms  %}
    <h4> {{room.name }}</h4>
  {% endfor %}
{% endblock content %}


```
