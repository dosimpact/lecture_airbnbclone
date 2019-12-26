# section 07

# 7.0 Managers and QuerySets (14:36)

- 장고가 설정된 모델들과 코드로 소통하기

```js
manage.py shell
```

- dir 과 vars

```js
dir(User) list형태로, 클래스의 모든 정보를 뿌려준다. ['인자명','함수명'....] 변수의 이름들만 알려줌. 좀더 간편하게 보임
vars(User) dictionary 형태로, 클래스의 모든 정보를 뿌려준다. {"key":"value",}형태로 변수와 변수들의 값까지 알려줘서, 복잡하지만 다 보임.
```

- 모델 매니저(DB객체를 자유자제로 다룬다. 덕분에 외래키에 접근해서, 해당 외래키의 인스턴스 뿐아니라 모든 inst접근가능),

```
>>> from users.models import User # shell에서 모델 임포트하기
>>> User
<class 'users.models.User'> #모델 클래스
>>> dir(User) #[]리스트 형식(간단표기) 로 보여준다.
['CURRENCY_CHOICES', 'CURRENCY_KRW', 'CURRENCY_USD', 'DoesNotExist', 'EMAIL_FIELD', 'GENDER_CHOICE', 'GENDER_FEMALE', 'GENDER_MALE', 'GENDER_OTHER', 'LANGUAGE_CHOICES',
...
 'user_permissions', 'username', 'username_validator', 'validate_unique']
```

```
>>> vars(User) # { 키:값} 복잡한 형태로 보여준다.
mappingproxy({'__module__': 'users.models', '__doc__': ' Custom User Model ', 'GENDER_MALE': 'male', 'GENDER_FEMALE': 'female', 'GENDER_OTHER': 'other', 'GENDER_CHOICE': (('male', 'Male'), ('female', 'Female'), ('other', 'Other')), 'LANGUAGE_ENGLISH': 'en', 'LANGUAGE_KOREA': 'kr', 'LANGUAGE_CHOICES': (('en', 'English'), ('kr', 'Korea')), 'CURRENCY_USD': 'usd', 'CURRENCY_KRW': 'krw', 'CURRENCY_CHOICES': (('usd', 'USD'), ('krw', 'KRW')), '__str__': <function User.__str__ at 0x000001DF7E3758B8>, '_meta': <Options for User>, 'DoesNotExist': ...
...
<django.db.models.fields.related_descriptors.ReverseManyToOneDescriptor object at 0x000001DF7E7F9408>, 'list_set':
0x000001DF7E809088>, 'message_set': <django.db.models.fields.related_descriptors.ReverseManyToOneDescriptor object at 0x000001DF7E80D5C8>})
```

```
>>> User.objects #클래스의 objects에는 매니저가 있다 . 이 덕분에, 모델들을 엄청 자유롭게 다루는 것이다.
<django.contrib.auth.models.UserManager object at 0x000001DF7E39BA88>
>>> User.objects.all() #User모델이 가지고 있는 모든 인스턴스들을 반환한다.
<QuerySet [<User: happy>]>
>>> User.objects.filter(username = "happy") #필터를 통해 가져올 수 도있다.
<QuerySet [<User: happy>]>
```

- orm 모델 매니저에는 엄청난기능. room은 방주인으로 user를 외래키 사용함.( room -> user ) | ! user에서는 room으로 외래키인지 모름 | ! user에서 역으로 room(역 외래키)에 접근가능!! | room의 모든inst에 접근 가능!!

```
>>> happy = User.objects.get(username = "happy") # happy로 변수로 받아서
>>> happy
<User: happy>

>>> happy.room_set #모델이름은 Room이고 lower case로 room으로 작성한다. | 그리고 room_set으로 reverse_외래키 접근 가능 |
<django.db.models.fields.related_descriptors.create_reverse_many_to_one_manager.<locals>.RelatedManager object at 0x000001DF7E8A3E08>
>>> happy.room_set.all() #매니저를 통해 역외래키 접근후 , 객체 얻어오기. 역외래키 결과 없으면 빈 쿼리셋이다.!!
<QuerySet [<Room: Cottage by the sea Walk to beach>]>
>>>
```

# 7.1 Practicing the Django ORM (11:15)

- 리버스 1:N

```
>>> from users.models import User
>>> happy = User.objects.get(username = "happy")
>>> happy.review_set.all() # 외래키 접근 by 리버스 1:N
<QuerySet [<Review: i love it - Cottage by the sea Walk to beach>]>
>>> happy.room_set.all() # 외래키 접근 by 리버스 1:N
<QuerySet [<Room: Cottage by the sea Walk to beach>]>
```

- related_name="rooms"

```
    host = models.ForeignKey(
        "users.User", related_name="rooms", on_delete=models.CASCADE # related_name으로 User에서 접근할때 접근자를 지정해준다. 이 통로로만 접근이 가능!!
    )
```

```

>>> from users.models import User
>>> happy = User.objects.get(username = "happy")
>>> happy.room_set.all()  # 외래키 접근 by 리버스 1:N 기본 통로 페쇄
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: 'User' object has no attribute 'room_set'
>>> happy.rooms.all() # 외래키 접근 by 리버스 1:N
<QuerySet [<Room: Cottage by the sea Walk to beach>]>
>>>
```

- forward N:N

```
>>> from rooms.models import Room
>>> inst1 = Room.objects.get(pk = 1)
>>> inst1
<Room: Cottage by the sea Walk to beach>
>>> inst1.facility #그냥 속성을 통해서 접근
<django.db.models.fields.related_descriptors.create_forward_many_to_many_manager.<locals>.ManyRelatedManager object at 0x00000256CA440748>
```

# 7.2 Many to Many \_sets (2:50)

- 모든 1:N, N:N 에 related_name 의 항목을 추가했다.
- N:N 관계에서 forward N:N은 그냥 속성값으로 접근 가능.

```python
class Review(core_models.TimeStampedModel):
    """ Review Model Definition """

    review = models.TextField()
    accuracy = models.IntegerField()
    communication = models.IntegerField()
    cleanliness = models.IntegerField()
    location = models.IntegerField()
    check_in = models.IntegerField()
    value = models.IntegerField()
    user = models.ForeignKey(
        "users.User", related_name="reviews", on_delete=models.CASCADE
    )
    room = models.ForeignKey(
        "rooms.Room", related_name="reviews", on_delete=models.CASCADE
    )

    def __str__(self):
        # 장고 파이썬 3 str문법으로 다음이 가능하다.
        return f"{self.review} - {self.room}"
```

# 7.3 Finishing the Room Admin (4:41)

```
@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("name", "used_by") #used_by라는 display속성을 추가하고

    def used_by(self, obj):
        return obj.rooms.count() #해당 내용을 정의한다. 해당 방타입,편의시설 등등 .. 을 참조하는 room들을 알아낸다.
```

```
    def count_photos(self, obj):
        return obj.photos.count() #obj에서 혹시나 있을수 있는 photos를 참조해 보았고, 그 수를 반환한다.

```
