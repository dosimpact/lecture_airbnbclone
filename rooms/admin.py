from django.contrib import admin
from . import models


@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    #admin 패널에서 보일 필드들을 적어준다.
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
    #필드에 대한 필터
    list_filter = ("instant_book", "city", "country")
    #검색에 대한 설정 , =city는 완전일치 | ^는 앞에서부터 일치 여부 | host__username 은 host 외래키 __ 외래키모델접근자 username 모델속성 
    search_fields = ("=city", "^host__username")

@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass