from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage
from django.views.generic import ListView
from django.urls import reverse
from django.http import Http404
from . import models


class HomeView(ListView):
    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    page_kwarg = "page"


def room_detail(request, pk):
    try:
        room = models.Room.objects.get(pk=pk)
        return render(request, "rooms/detail.html", context={"room": room})
    except models.Room.DoesNotExist:
        raise Http404()
        # return redirect(reverse("core:home"))


def all_rooms(request):

    page = request.GET.get("page", 1)
    room_list = models.Room.objects.all()
    paginator = Paginator(room_list, 10, orphans=5)
    try:
        rooms = paginator.page(int(page))
        return render(request, "rooms/home.html", {"page": rooms})
    except EmptyPage:
        return redirect("/")
    except ValueError:
        return redirect("/")
    except Exception:
        return redirect("/")

