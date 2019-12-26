#13 SearchView

# 13.0 Template, Form, Url, Setup (7:59)

- airbnb사이트위에 항상떠있는 검색바를 만듭니다. base.html에 form으로 header에 넣으면, 모든 html에 검색바가 나오고, from의 get방식을통해 검색을하면,  
  새로운 url로 접속.

```
rooms/urls.py

app_name = "rooms"
urlpatterns = [
    path("<int:pk>", views.RoomDetail.as_view(), name="detail"),
    path("search/", views.search, name="search"),
]
```

```
rooms/views.py

def search(request):
    city = request.GET.get("city")
    city = str.capitalize(city)
    return render(request, "rooms/search.html", {"city": city})
```

```
templates/partials/header.html

<header>
    <a href="{% url "core:home" %}">Nbnb</a>
    <ul>
        <li><a href="#">Login</a></li>
    </ul>
    <form method="get" action="{% url "rooms:search" %}">
        <input name="city" placeholder="Search by City" />
    </form>
</header>
```

```
templates/rooms/search.html

{% extends "base.html" %}

{% block page_title %}
    Search
{% endblock page_title %}

{% block content %}

    <h2>Search!</h2>

    <h4>Searching by {{city}}</h4>

{% endblock content %}
```

# 13.1 Starting the Form (12:56)

- search.html에서 다양한 검색조건을 뿌려줍니다. city,counties 를 DB에서 불러와 <options>를 통해 뿌려주고, form을 통해 name 및 value를 받습니다.
- 문제는.. header에 모든 검색창을 뿌려주면, 막상 검색을 했을때, 검색 상세페이지에서는 검색바가 필요없습니다. 그러면, 간단한 트릭을 통해,  
  즉, block를 오버라이드하는 방법으로 검색바를 없앨수 있슴
- form에 하나의 button만 있으면 이는 submit의 버튼으로 인식한다.

```
rooms/views.py

from django_countries import countries

def search(request):
    city = request.GET.get("city")
    city = request.GET.get("city", "Anywhere")
    city = str.capitalize(city)
    room_types = models.RoomType.objects.all()
    return render(
        request,
        "rooms/search.html",
        {"city": city, "countries": countries, "room_types": room_types},
    )
```

```
templates/base.html : header를 base로 옮기고, block안에 값을 넣어 override 되도록 만듦

    <title>{% block page_title %}{% endblock page_title %}| Nbnb</title>
  </head>
  <body>
    {% include "partials/header.html" %}
    <header>
      {% include "partials/nav.html" %}
      {% block search-bar %}
        <form method="get" action="{% url "rooms:search" %}">
            <input name="city" placeholder="Search By City" />
        </form>
      {% endblock search-bar %}
    </header>

    {% block content %}{% endblock %}
```

```
templates/rooms/search.html 밑의 오버라이드

{% block search-bar %}
{% endblock search-bar %}

{% block content %}
    <h2>Search!</h2>
    <h4>Searching by {{city}}</h4>
    <form method="get" action="{% url "rooms:search" %}">
        <div>
            <label for="city">City</label>
            <input value="{{city}}" id="city" name="city" placeholder="Search By City" />
        </div>

        <div>
            <label for="country">Country</label>
            <select id="country" name="country" >
                {% for country in countries  %}
                    <option value="{{country.code}}">{{country.name}}</option>
                {% endfor %}
            </select>
        </div>

        <div>
            <label for="room_type">Room Type</label>
            <select id="room_type" name="room_type" >
                {% for room_type in room_types  %}
                    <option value="{{room_type.pk}}">{{room_type.name}}</option>
                {% endfor %}
            </select>
        </div>
        <button>Search</button>
    </form>
{% endblock content %}
```

# 13.2 Select Choices (6:48)

# 13.3 Amenities and Facilities Form (10:26)

# 13.4 Finishing the Form (8:04)

# 13.5 Filtering Like a Boss part One (10:10)

# 13.6 Filtering Like a Boss part Two (12:09)

# 13.7 Introduction to Django Forms (5:25)

# 13.8 I love Django Forms For Ever (8:15)

# 13.9 Forms are Awesome! (15:15)

# 13.10 Finishing Up! (5:39)
