# section 04

# 4.0 TimeStampedModel (7:16)\

- 1. Core모델만들어서, 데이터가 만들어진 시점 / 데이터가 업데이터된 시점 기록하기.

```
DJANGO_APPS = [
    "users.apps.UsersConfig",
    "core.apps.CoreConfig",
    "rooms.apps.RoomsConfig",
]

class TimeStampModel(models.Model):
    """ Tiem stamped Model """

    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        abstract = True
```

- 2. Core모델을 상속받아 room 모델 만들기

```
from core import models as core_models


class Room(core_models):
    """ Room Model Definition """

    pass

@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    pass

```

# 4.1 Room Model part One (12:24)

- import 순서 : 파이썬 관련(os) | django 관련 임포트 | 서드파티 입포트 | 내가 만든것들 임포트 하기

```
    THIRD_PARTY_APPS = ["django_countries"]

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    guests = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey(user_models.User, on_delete=models.CASCADE)

```

# 4.2 Foreing Keys like a Boss (6:24)

- model.ForeignKey 관계는 , 사용자와 인스타그램 post관계. 1(user):N(poster) 와 같은 관계이다. 인스턴스들이 맺고있는 관계를 생각해보면 된다.

# 4.3 ManyToMany like a Boss (11:31)

- model.ManyToMany 관계는, 하나의 방 Room1과 방의 타입 호텔,쉐어룸,원룸 등등, N(room_n) : N(room_type_n) 의 관계이다.

```
@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    pass

class AbstractItem(core_models.TimeStampModel):
    """ AbstractItem"""

    name = models.charField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstractItem):
    pass

class Room(core_models):
    """ Room Model Definition """

...
    room_type = models.ManyToManyField(RoomType, blank=True)

    def __str__(self):
        return self.name
```

# 4.4 on_delete, Amenity, Faciliy, HouseRule Models (12:57)

```python
@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):
    pass
```

```python
class RoomType(AbstractItem):

    """ RoomType Model Definition """

    pass

class Amenity(AbstractItem):

    """ Amenity Model Definition """

    pass

class Facility(AbstractItem):

    """ Facility Model Definition """

    pass

class HouseRule(AbstractItem):

    """ HouseRule Model Definition """

    pass

```

```cs

    room_type = models.ForeignKey(RoomType, on_delete=models.SET_NULL, null=True)
    amenities = models.ManyToManyField(Amenity)
    facilities = models.ManyToManyField(Facility)
    house_rules = models.ManyToManyField(HouseRule)

```

# 4.5 Meta Class and Photos Model (9:43)

- admin패널에서 표시되는 모델이름은, 원래이름 + s가 붙고, CamelCase로 변환된다. 이를 메타클래스를 통해서 바꿀 수 있다.

```
class RoomType(AbstractItem):
    """ RoomType Model Definition"""

    class Meta:
        verbose_name = "Room Type" # CamelCase변경, 이 이름에서 s가 붙는다.
        ordering = ["created"] # 다음 필드값으로 정렬

class Amenity(AbstractItem):
    """ Amenity model Definition """

    class Meta:
        verbose_name_plural = "Amenities" # 다음 이름으로 모델을 표기한다. s는 여기서 더이상 붙지 않는다.
```

- model은 다음과 같이 string형태로 써서, 구지 다른 어플리케이션을 임포트하고, 또 모델의 순서를 따를 필요가 없다.

```
   # host = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    host = models.ForeignKey("users.User", on_delete=models.CASCADE)
```
