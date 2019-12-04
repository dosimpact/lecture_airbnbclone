# section 12

# 12.0 URLs and Arguments (11:06)

```python
#config - urls
urlpatterns = [
    path("", include("core.urls", namespace="core")),
    path("rooms/", include("rooms.urls", namespace="rooms")), #rooms/로 시작하면 rooms -> urls로 라우팅
    path("admin/", admin.site.urls),
]

```

```python
#core - urls
from django.urls import path
from rooms import views as room_views
app_name = "core"
urlpatterns = [path("", room_views.HomeView.as_view(), name="home")]
```

- url구성시 : ?page = 1 쿼리를 주는경우 | 지금은 rooms/4, rooms/15 등등의 url를 받을때 사용함.

```python
#rooms - urls
from django.urls import path
from . import views
app_name = "rooms"
urlpatterns = [path("<int:pk>", views.room_detail, name="detail")] #
```

- 반드시 request와 pk도 받아야 한다.

```python
def room_detail(request, pk):
    print(pk)
    return render(request, "rooms/room_detail.html")
```

- href에 다음처럼, url 길을 직접 지정해 줘도 되지만, include의 namespace 와 path 의 name으로 namespace:name으로 url를 연결할수도 있음.!!

```
#room_list.html
    <a href ="rooms/{{room.pk}}"> <h4> {{room.name }} / {{room.price}} </h4> </a>
```

```
#room_list.html
    <a href ="{% url "rooms:detail" room.pk %}"> <h4> {{room.name }} / {{room.price}} </h4> </a>

```

```
#header.html
    <header>
      <a href="{% url "core:home" %}">Nbnb</a>
      <ul>
        <li><a href="#">Login</a></li>
      </ul>
    </header>
```

# 12.1 get_absolute_url (4:07)

# 12.2 room_detail FBV finished (8:03)

# 12.3 Http404() (4:33)

# 12.4 Using DetailView CBV (6:33)
