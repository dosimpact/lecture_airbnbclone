# section 08

# 8.0 Rewiew Admin and Room Average (11:21)

- reviews : DB의 review의 평점을 구하는 함수를 작성 -> model에다가, 그리고 admin 패널에서 사용하기.

```
    # 모델에서 평균을 구하는 함수를 작성함. => 어드민패널,콘솔,프론트엔드 다 사용이 가능하다.
    def rating_average(self):
        avg = (
            self.accuracy
            + self.communication
            + self.cleanliness
            + self.location
            + self.check_in
            + self.value
        )
        return round(avg, 2)

    rating_average.short_description = ".AVG"
```

```
@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):

    """ Review Admin Definition """
    list_display = ("__str__", "rating_average") #원래 list_display를 override하는거기 떄문에 __str__도 적어준다. 모델에서 만든 함수 그대로 적어주면 display가 가능!!
```

- rooms: DB의 review의 평점을 구하는 함수를 작성 -> model에다가, 그리고 admin 패널에서 사용하기.

```
    def total_rating(self):
        all_reviews = self.reviews.all() #rooms에서는 모르지만, reviews는 외래키 = rooms | self.reviews 로 reverse 1:N | 객체 얻어옴
        all_ratings = []
        for review in all_reviews:
            all_ratings.append(review.rating_average()) | reviews(inst).rating_average를 모아서 평균 반환.
        return 0
```

```
class RoomAdmin(admin.ModelAdmin):
    ...
    list_display = (
        "name",
    ...
        "total_rating",
    )
```

- users: list filter 및 list display추가

```
    fieldsets = UserAdmin.fieldsets + (
        ("Custom profiles", {"fields": ("avatar", "gender", "bio")}),
    )
    list_filter = UserAdmin.list_filter + ("superhost",)
    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "language",
        "currency",
        "superhost",
        "is_staff",
        "is_superuser",
    )
```

# 8.1 Reservations Admin (9:02)

- reservation : model , django의 tiemzone을 이용하는 이유는, setting.에서 서버의 지역시간대를 이용할수있는데, 이것들이 반영되기 떄문.

```
from django.utils import timezone
```

- reservation 모델 작성

```
    def in_progress(self): #예약이 현재 진행중이면 true 반환
        now = timezone.now().date()
        return now > self.check_in and now < self.check_out

    in_progress.boolean = True #admin 패널에서 표시될 내용을 bool 로

    def is_finished(self): #예약이 끝나면 true 반환
        now = timezone.now().date()
        return now > self.check_out

    is_finished.boolean = True #admin 패널에서 표시될 내용을 bool 로
```

- reservation 관리자 패널 작성

```
@admin.register(models.Reservation)
class ReservationAdmin(admin.ModelAdmin):

    """ Reservation Admin Definition """

    list_display = (
        "room",
        "status",
        "check_in",
        "check_out",
        "guest",
        "in_progress",
        "is_finished",
    )
```

# 8.2 Conversations, Lists, Reservations Admin (13:10)

- ", ".join( 리스트 ) 함수를 써보자.

```
>>> list_sample = ['AA','BB','CC']
>>> ", ".join(list_sample)
'AA, BB, CC'

```

- conversatinos - model

```
    def __str__(self): #기본 __str__을 모든 참가자가 보이도록 정의했음.
        usernames = []
        for user in self.participants.all():
            usernames.append(user.username)
        return ", ".join(usernames)

    def count_messages(self): #단톡방의 메시지 수
        return self.messages.count()

    count_messages.short_description = "Number of Messages" # 제목 재정의

    def count_participants(self): # 단톡방의 참가자수
        return self.participants.count()

    count_participants.short_description = "Number of Participants" # 제목 제정의
```

- conversatinos - admin

```

@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):
    """ Message Admin Definition """

    list_display = ("__str__", "created")


@admin.register(models.Conversation)
class ConversationAdmin(admin.ModelAdmin):
    """ Conversation Admin Definition """

    list_display = ("__str__", "count_messages", "count_participants")
```

- lists - model

```
class List(core_models.TimeStampedModel):
    """ List Model Definition """

    name = models.CharField(max_length=80)
    user = models.ForeignKey(
        "users.User", related_name="lists", on_delete=models.CASCADE
    )
    rooms = models.ManyToManyField("rooms.Room", related_name="lists", blank=True)

    def __str__(self):
        return self.name

    def count_rooms(self): #위시 리스트에서는 총 방의 갯수를 리턴.
        return self.rooms.count()

    count_rooms.short_description = "Number of Rooms"
```

- lists - admin

```
@admin.register(models.List)
class ListAdmin(admin.ModelAdmin):
    list_display = ("name", "user", "count_rooms") #inst 보여주기

    search_fields = ("name",) #이름으로 검색 icontain

    filter_horizontal = ("rooms",) #위시 리스트 room 쉽게 고르게~
```

# 8.3 Configuring User Uploads part One (7:07)

[참조 MEDIA ROOT ](https://docs.djangoproject.com/en/2.2/ref/settings/#media-root)

- gitignore에 다음추가하기

```
uploads/
```

- MEDIA_ROOT를 통해 파일(이미지)들이 저장되는 기본위치 설정 , os.path.join은 두 인자를 붙여준다. uploads는 파일 명이라 생각하면 됨.

```
MEDIA_ROOT = os.path.join(BASE_DIR, "uploads")
```

- ImageField는 FileField를 상속받았고, upload_to를 통해, 파일이 지정되는 경로를 설정할수있다. ( 기본은 MEDIA ROOT 에서 )

```
class Photo(core_models.TimeStampedModel):
    """ Photo Model Definition """

    caption = models.CharField(max_length=80)
    file = models.ImageField(upload_to = "room_phptos")
    room = models.ForeignKey("Room", related_name="photos", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption
```

-

```
    avatar = models.ImageField(upload_to="avatars", blank=True)
```

# 8.4 Configuring User Uploads part Two (13:02)

- MEADIA ROOT 설정

```
#원래 파일의 경로는 이거다.
http://127.0.0.1:8000/admin/users/user/1/change/avatars/%EB%82%B4%EC%83%81%ED%8C%90.png

MEDIA_URL = "media/"  # 파일(사진)을 요청했을때, url에 media/ 접두 해준다. 상대경로로 ,기존 url에 붙여진다.
http://127.0.0.1:8000/admin/users/user/1/change/media/avatars/%EB%82%B4%EC%83%81%ED%8C%90.png

MEDIA_URL = "/media/"  # /로 시작해서 , 절대경로로 새롭게 routing된다, media
http://127.0.0.1:8000/media/avatars/%EB%82%B4%EC%83%81%ED%8C%90.png
```

- static호출에서 media에 접근하고 싶은데, 어디로 갈지

```
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [path("admin/", admin.site.urls)]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    #MEDIA_URL로 접근 media 파일로 접근을 하려함., static이 MEDIA_ROOT로 가라 알려준다.
```

- 반드시 static 폴더를 서버에서 처리하지 마라. 사용자가 많아질수록 디스크 공간을 많이 쓰기땨문에, 반드시 database 는 따로 둬라.

# 8.5 Photo Admin (9:07)

# 8.6 raw_ids and Inline Admin (7:59)

# 8.7 Explaining Python super() (8:48)

# 8.8 Intercepting Model save() and admin_save() (9:51)
