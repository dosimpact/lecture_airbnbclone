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
- django template에서는 함수를() 라고 호출을 안해도 된다. 매직

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

[참조](https://docs.djangoproject.com/en/3.0/ref/paginator/#django.core.paginator.InvalidPage)

- get_page는 모든 애러를 잡아주는대신, 페이지범위를 벗어나면 다른페이지를 보여주거나 등의 기능은 추가를 못한다.
- 반면 page는 예외처리로 더 많이 가능하다.

```
    rooms = paginator.get_page(page) vs  rooms = paginator.page(page)
```

```
Paginator.get_page(number)[source]¶
Returns a Page object with the given 1-based index, while also handling out of range and invalid page numbers.
If the page isn’t a number, it returns the first page. If the page number is negative or greater than the number of pages, it returns the last page.
Raises an EmptyPage exception only if you specify Paginator(..., allow_empty_first_page=False) and the object_list is empty.

Paginator.page(number)[source]¶
Returns a Page object with the given 1-based index. Raises InvalidPage if the given page number doesn’t exist.
```

- page에서 나올수 있는 3가지 애러 => 핸들링으로 리다이렉트

```
exception InvalidPage
A base class for exceptions raised when a paginator is passed an invalid page number.

The Paginator.page() method raises an exception if the requested page is invalid (i.e. not an integer) or contains no objects. Generally, it’s enough to catch the InvalidPage exception, but if you’d like more granularity, you can catch either of the following exceptions:

exception PageNotAnInteger
Raised when page() is given a value that isn’t an integer.

exception EmptyPage
Raised when page() is given a valid value but no objects exist on that page.

Both of the exceptions are subclasses of InvalidPage, so you can handle them both with except InvalidPage.
```

- 고아 = 남는 inst | if page 단위 10, 총 32개, -> 3페이지 + 2 고아 , 마지막페이지에 12개 아이템을 다 보여준다 | orphans =5 면 15개까지 ~

```
    paginator = Paginator(room_list, 10, orphans=5)
```

# 11.6 Handling Exceptions (5:01)

```
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage
from . import models

def all_rooms(request):

    page = request.GET.get("page", 1)
    room_list = models.Room.objects.all()
    paginator = Paginator(room_list, 10, orphans=5)
    try:
        rooms = paginator.page(int(page)) #얻어온 page정보로 | 숫자,문자,"", 뭐든 올수 있는데,
        return render(request, "rooms/home.html", {"page": rooms}) #잘왔으면 페이지 보여주기
    except EmptyPage:
        return redirect("/") #범위를 벗어난 페이지면 HOME으로 리다이렉트
    except ValueError:
        return redirect("/") #문자를 넣으면 ->  HOME으로 리다이렉트
    except Exception:
        return redirect("/") #그외 애러 ->  HOME으로 리다이렉트
```

# 11.7 Class Based Views (11:25)

[참조 문서](https://docs.djangoproject.com/en/3.0/ref/class-based-views/generic-display/#listview)
[참조 문서2](https://ccbv.co.uk/projects/Django/2.2/django.views.generic.list/ListView/)

- 클래스 기반 뷰 장점은 이미 만들어진 뷰에 몇가지 설정만하면 사용가능 | 지금까지는 def함수기반으로 render를 리턴했음 |
  class based vies --> list view,( django는 많은 abstract를 가지고 있다. model도 그렇고 view 도 그렇다. )

아니잇, ListView에 model을 Room을 넣었더니, templates폴더에서 알아서 room_list.html을 찾아본다.
단순히 설정만 했는데, 다 있어, paginator는 page_obj 라는 이름으로 이미 있어!!

```
#클래스 기반의 뷰를 사용하려면, .as_view()라고 연결
urlpatterns = [path("", room_views.HomeView.as_view(), name="home")]
```

```
from django.views.generic import ListView

class HomeView(ListView):
    model = models.Room #모델연결
    paginate_by = 10 #페이지네이트 설정
    paginate_orphans = 5 #고아
    ordering = "created" #정렬 by 모델명
    page_kwarg = "page" #page=1 -> 페이지네이트
```

```

{% extends "base.html" %}

{% block page_name %}
  Home
{% endblock page_name %}

{% block content %}

  {% for room in object_list  %}
    <h4> {{room.name }} / {{room.price}}</h4>
  {% endfor %}


  {% if page_obj.has_previous %}
    <a href="?page={{page_obj.number|add:-1}}">Previous</a>
  {% endif %}

  Page {{page_obj.number}} of {{page_obj.paginator.num_pages}}

  {% if page_obj.has_next  %}
      <a href="?page={{page_obj.number|add:1}}">Next</a>
  {% endif %}

{% endblock content %}


```

# 11.8 Class Based Views part Two (7:37)
