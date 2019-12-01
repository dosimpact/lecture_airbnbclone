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

- users:

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

# 8.2 Conversations, Lists, Reservations Admin (13:10)

# 8.3 Configuring User Uploads part One (7:07)

# 8.4 Configuring User Uploads part Two (13:02)

# 8.5 Photo Admin (9:07)

# 8.6 raw_ids and Inline Admin (7:59)

# 8.7 Explaining Python super() (8:48)

# 8.8 Intercepting Model save() and admin_save() (9:51)
