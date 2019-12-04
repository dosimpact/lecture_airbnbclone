# section 11

# 11.0 HomeView Intro (2:09)

- room정보를 10개만 뿌리는 방법 3가지. | only python | djagno 조금 | djagno 마법

# 11.1 Pagination with Limit and Offset (10:55)

[쿼리셋 리미트 : DB에서 다 가져오는게 아니라 즉당히~](https://docs.djangoproject.com/en/3.0/topics/db/queries/#limiting-querysets)

[request 에 대한 정보를 얻고싶다. 특히 get 사용법](https://docs.djangoproject.com/en/3.0/ref/request-response/#django.http.HttpRequest.GET)

- request | vars,dir | GET 정보

```python
    print(request.GET)
    print(dir(print(request)) | request는 get, key...등등 많은정보를 가지고 있음.
```

- http://localhost:8000/?page=2 에서 get정보 받아서 방 10개만 뿌리기.

```python
def all_rooms(request):
    # page -> str | default = 1 | by GET -> dictionary
    page = int(request.GET.get("page", 1))
    page_size = 10
    limit = page_size * page
    offset = limit - page_size

    rooms = models.Room.objects.all()[offset:limit]
    return render(request, "rooms/home.html", context={"rooms": rooms})

```

# 11.2 Pages List Navigation (8:16)

```python
def all_rooms(request):
    ...
    page_count = ceil(models.Room.objects.count() / page_size) # Room.ojects.count() |
    rooms = models.Room.objects.all()[offset:limit]
    return render(
        request,
        "rooms/home.html",
        context={
            "rooms": rooms,
            "page": page,
            "page_count": page_count,
            "page_range": range(1, page_count + 1), # use range class to django template
        },
    )
```

```python
{% block content %}
...
  <h5> Page {{page}} of {{page_count}}</h5> #page from GET | page_count from objects.count()

  {% for page in page_range %}  # for in ~ endfor | {{page}} is not from GET
    <a href = "?page={{page}}">{{page}}</a>
  {% endfor %}

{% endblock content %}
```

# 11.3 Next Previous Page Navigation (6:49)

[django template filter ](https://docs.djangoproject.com/en/3.0/ref/templates/builtins/#add)

- 장고 템플릿안에서는 많은 문법을 허용하지 않는다. view에서 최대한 처리| 그럼에도 filter라는 기능을 제공 | 간단한 로직 구현 가능.

```python
  {% if page is not 1 %}
    <a href ="?page={{page|add:-1}}">Previous</a> #필터사용법은 | add:1
  {% endif %}

  {% for page in page_range %}
    <a href = "?page={{page}}">{{page}}</a>
  {% endfor %}

  {% if not page == page_count %}
    <a href ="?page={{page|add:1}}">Next</a>
  {% endif %}
```

# 11.4 Using Django Paginator (9:56)

- django의 parginator의 기능을 이용해서, 빠르게 페이지를 넘겨본다.

```python
from django.core.paginator import Paginator

def all_rooms(request):
    page = int(request.GET.get("page", 1) or 1)
    room_list = models.Room.objects.all()  # 아직은 DB에서 전부 가져오지않음. 쿼리셋만 만들어진다., 적당히 가져온다. 장고의 마법으로.
    paginator = Paginator(room_list, 10) #페이지네이터(room쿼리셋 , page단위)
    # paginator vars 결과 | 25개의 room쿼리셋 | number :1 | paginator 객체

    rooms = paginator.get_page(page) #원하는 page를 넣으면 딱 해당 쿼리셋만 나옴.
    return render(request, "rooms/home.html", context={"rooms": rooms})

```

[장고 paginator docs 참고할것. !](https://docs.djangoproject.com/en/3.0/ref/paginator/#page-class)

```
Paginator.get_page(number)[source]¶
Returns a Page object with the given 1-based index, while also handling out of range and invalid page numbers.
```

- Page object : object_list | number | paginator.num_pages

```python

{% extends "base.html" %}

{% block page_name %}
  Home
{% endblock page_name %}

{% block content %}
    #room 은 Paginator.get_page결과 | object_list
  {% for room in rooms.object_list  %}
    <h4> {{room.name }} / {{room.price}}</h4>
  {% endfor %}

  {% if rooms.has_previous %}
    <a href="?page={{rooms.number|add:-1}}">Previous</a>
  {% endif %}

  Page {{rooms.number}} of {{rooms.paginator.num_pages}}

  {% if rooms.has_next  %}
      <a href="?page={{rooms.number|add:1}}">Next</a>
  {% endif %}

{% endblock content %}


```

# 11.5 get_page vs page (9:58)

# 11.6 Handling Exceptions (5:01)

# 11.7 Class Based Views (11:25)

# 11.8 Class Based Views part Two (7:37)
