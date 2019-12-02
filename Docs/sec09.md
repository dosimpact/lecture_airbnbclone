# section 09

# 9.0 Custom manage.py commands (12:00)

- commands 커스터마이징해서, loveyou --times 5 하면 I love you 5번 출력하기.

```
#앱안에 다음의 명명규칙으로 작성해야한다.
rooms | management
rooms | management __init__.py
rooms | management | commands
rooms | management | commands __init__.py
rooms | management | commands loveyou.py <- 명령어
```

[참조](https://docs.djangoproject.com/en/2.2/howto/custom-management-commands/#module-django.core.management)

```
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand): #이 클래스에서 명령어 인자와 로직 구현
    help = "This commnad tells you that I love you" #loveyou 도움말

    def add_arguments(self, parser):
        parser.add_argument( #parser를 이용
            "--times", #인자명
            type=int, #int로 받는다 | 기본 str
            help="How many times do you want me to tell you that I love you?", #--tims인자에 대한 도움말
        )

    def handle(self, *args, **options):
        times = options.get("times") #딕셔너리에서 key로 value얻을때
        for t in range(0, times): #반복
            self.stdout.write(self.style.SUCCESS("I love you")) #표준출력을통해 초록색으로 출력함.
```

# 9.1 seed_amenities command (7:05)

- 실제 에어비엔비에서 데이터 가져와서 시드 데이터 주기. objects.create(name = a)

```
from django.core.management.base import BaseCommand, CommandError
from rooms.models import Amenity


class Command(BaseCommand):
    help = "This seed amenities in airbnb site"
    def handle(self, *args, **options):
        amenities = [
            "Air conditioning",
            ...
            "TV",
        ]
        for a in amenities:
            Amenity.objects.create(name=a)
        self.stdout.write(self.style.SUCCESS("Amenities created!!"))

```

# 9.2 seed_everything and seed_users (14:12)

- facilities 도 앞에서 똑같이 시드 주면 된다.

```python
from django.core.management.base import BaseCommand, CommandError
from rooms.models import Facility


class Command(BaseCommand):
    help = "This seed facilities in airbnb site"

    def handle(self, *args, **options):
        facilities = [
            "Private entrance",
            "Paid parking on premises",
            "Paid parking off premises",
            "Elevator",
            "Parking",
            "Gym",
        ]
        for f in facilities:
            Facility.objects.create(name=f)
        self.stdout.write(self.style.SUCCESS(f"{len(facilities)} facilities created!"))
```

- django_seed 서드파트 설치 | setting에 추가.
  [django_seed](https://github.com/Brobin/django-seed)

```python
from django.core.management.base import BaseCommand, CommandError
from django_seed import Seed
from users.models import User


class Command(BaseCommand):
    help = "This commnad creates Users"
    #number인자를 | type = int | default = 2 |
    def add_arguments(self, parser):
        parser.add_argument("--number", default=2, type=int, help="create seed user")
    #option = dictionary => | get("number") | seed doc참고해 작성함.
    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()

        seeder.add_entity(User, number, {"is_staff": False, "is_superuser": False})
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} users created! "))


```

# 9.3 seed_rooms part One (11:13)

# 9.4 seed_rooms part Two (10:30)

# 9.5 seed_rooms part Three (5:49)

# 9.6 seed_reviews (5:34)

# 9.7 seed_lists (6:55)

# 9.8 seed_reservations (10:19)
