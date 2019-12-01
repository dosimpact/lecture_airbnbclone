from django.contrib import admin
from . import models


@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("name", "used_by")

    def used_by(self, obj):
        return obj.rooms.count()


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
        "count_amenities",
        "count_photos",
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

    def count_amenities(self, obj):
        return obj.amenity.count()

    count_amenities.short_description = "count_amenities sexy"

    def count_photos(self, obj):
        return obj.photos.count()


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass
