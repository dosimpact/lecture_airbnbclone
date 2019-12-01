# section 07

# 7.0 Managers and QuerySets (14:36)

- 장고가 설정된 모델들과 코드로 소통하기

```
manage.py shell
```

- dir 과 vars

```
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

# 7.2 Many to Many \_sets (2:50)

# 7.3 Finishing the Room Admin (4:41)
