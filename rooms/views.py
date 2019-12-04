from math import ceil
from django.shortcuts import render
from django.core.paginator import Paginator
from . import models


def all_rooms(request):
    # page -> str | default = 1 | by GET -> dictionary
    page = int(request.GET.get("page", 1) or 1)
    room_list = models.Room.objects.all()  # 아직은 DB에서 전부 가져오지않음. 쿼리셋만 만들어진다.
    paginator = Paginator(room_list, 10)
    # vars 결과 | 25개의 room쿼리셋 | number :1 | paginator 객체
    rooms = paginator.get_page(page)
    return render(request, "rooms/home.html", context={"rooms": rooms})
