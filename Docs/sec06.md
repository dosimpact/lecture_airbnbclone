# section 06

# 6.0 Room Admin Panel

[참조 문서 ](https://docs.djangoproject.com/en/2.2/ref/contrib/admin/#django.contrib.admin.ModelAdmin.search_fields)

- list_display 인스턴스들 표시 | list_filter 인스턴스 필터 | search_fields 인스턴스 검색 | fields
- host--외래키 참조할때, model에서는 .으로 했는데, model.admin에서는 -- 로 참조.

```cs
    list_display = (
        "name",
        "country",
        "city",
        "price",
        "address",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
    )
    list_filter = ("instant_book", "city", "country")
    search_fields = ("=city", "^host__username") # 완전일치 | 외래키 참조 + 시작 일치.

```

```cs
Prefix	Lookup
^	startswith
=	iexact
@	search
None	icontains
```

# 6.1 Room Admin Panel part Two (11:29)

- 어드민 패널을 좀더 예쁘게 꾸밈니다.
  [filter docs](https://docs.djangoproject.com/en/2.2/ref/contrib/admin/#django.contrib.admin.ModelAdmin.filter_horizontal)

```
ModelAdmin.filter_horizontal¶
By default, a ManyToManyField is displayed in the admin site with a <select multiple>. However, multiple-select boxes can be difficult to use when selecting many items. Adding a ManyToManyField to this list will instead use a nifty unobtrusive JavaScript “filter” interface that allows searching within the options. The unselected and selected options appear in two boxes side by side. See filter_vertical to use a vertical interface.

```

- fieldsets admin패널의 속성값들을 정리 | list_display 미리보기속성값 | list_filter 필터로 해당 인스턴스만 | search_fields 인스턴스 검색 | filter_horizontal 속성값 선택 패널

```
@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    # admin 패널에서 보일 필드들을 적어준다.
    fieldsets = (
        (
            "Basic Info",
            {"fields": ("name", "description", "country", "price", "address")},
        ),
        ("Times", {"fields": ("check_in", "check_out", "instant_book")}),
        ("Spaces", {"fields": ("guests", "beds", "bedrooms", "baths")}),
        (
            "More About the Space",
            {
                "classes": ("collapse",),
                "fields": ("amenity", "facility", "house_rules"),
            },
        ),
    )
    list_display = (
        "name",
        "country",
        "city",
        "price",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
    )
    # 필드에 대한 필터
    list_filter = (
        "instant_book",
        "host__superhost",
        "room_type",
        "amenity",
        "facility",
        "house_rules",
        "city",
        "country",
    )
    # 검색에 대한 설정 , =city는 완전일치 | ^는 앞에서부터 일치 여부 | host__username 은 host 외래키 __ 외래키모델접근자 username 모델속성
    search_fields = ("=city", "^host__username")
    filter_horizontal = ("amenity", "facility", "house_rules")
```

# 6.2 Custom Admin Functions (6:08)

- list display에 커스텀 함수로 원하는 정보 표시하기.( amneities의 갯수 )

```
    list_display = (
        ...
        "count_amenities",
    )

    def count_amenities(self, obj):
        return obj.amenity.count()

    count_amenities.short_description = "count_amenities sexy"

```
