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

- room - model 애러 픽스

```
    def total_rating(self):
        all_reviews = self.reviews.all()
        all_ratings = 0
        if len(all_reviews) != 0: #그 방에 리뷰가 없는경우는? 0으로 나누게 되는데?
            for review in all_reviews:
                all_ratings += review.rating_average()
            return all_ratings / len(all_reviews)
        return 0
```

- room 시드

```
import random #랜덤함수 | random.choice(쿼리셋) | random.randint(1,5)
from django.core.management.base import BaseCommand, CommandError
from django_seed import Seed
#외래키는 django_seed가 저절로 못하기 떄문에, 지금 수동으로 작업함.
from rooms import models as room_models
from users import models as user_models


class Command(BaseCommand):
    help = "This commnad creates room"

    def add_arguments(self, parser):
        parser.add_argument("--number", default=2, type=int, help="create seed room")

    def handle(self, *args, **options):
        number = options.get("number")
        all_users = user_models.User.objects.all()
        room_types = room_models.RoomType.objects.all()

        seeder = Seed.seeder()
        seeder.add_entity(
            room_models.Room,
            number,
            {
                #lambda x | x는 Room을 의미..
                "name": lambda x: seeder.faker.address(),
                "host": lambda x: random.choice(all_users),
                "room_type": lambda x: random.choice(room_types),
                "guests": lambda x: random.randint(1, 20),
                "price": lambda x: random.randint(1, 300),
                "beds": lambda x: random.randint(1, 5),
                "bedrooms": lambda x: random.randint(1, 5),
                "baths": lambda x: random.randint(1, 5),
            },
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} users created! "))
```

# 9.4 seed_rooms part Two (10:30)

- faker를 이용해서, 랜덤 문장을 출력하는 함수 알아냄 | faker.sentence()
  [참조 faker](https://faker.readthedocs.io/en/master/index.html)

- flatten은 여러겹 쌓인 리스트를 하나의 리스트로 리턴한다.

```
from django.contrib.admin.utils import flatten
```

```
        created_photos = seeder.execute() #방에 시드를 준결과, id들이 반환됨.

        print(created_photos)  # {<class 'rooms.models.Room'>: [5]} # 딕셔너리형태 | 모델1 : [id list], 모델2....
        print(created_photos.values())  # dict_values([[5]]) #value만 뽑으면 list안 list
        print(list(created_photos.values()))  # [[5]] #
        print(flatten(list(created_photos.values())))  # [5] #flatten 이용

        created_clean = flatten(list(created_photos.values()))
        for pk in created_clean:
            room = room_models.Room.objects.get(pk=pk) #방의 id로 순회하면서
            for i in range(3, random.randint(10, 17)): #다음의 사진을 만들면서, 방을 연결시켜준다.
                room_models.Photo.objects.create(
                    caption=seeder.faker.sentence(),
                    room=room,
                    file=f"room_photos/{random.randint(1, 31)}.webp", #파일 이름은 uploads안의 폴더 이름.
                )
        self.stdout.write(self.style.SUCCESS(f"{number} users created! "))
```

# 9.5 seed_rooms part Three (5:49)

- room - seed | amenities , facilities , rules 추가

```
        for pk in created_clean:
            room = room_models.Room.objects.get(pk=pk)
            for i in range(3, random.randint(10, 30)):
                room_models.Photo.objects.create(
                    caption=seeder.faker.sentence(),
                    room=room,
                    file=f"room_photos/{random.randint(1, 31)}.webp",
                )
            for a in amenities:
                magic_number = random.randint(0, 15)
                if magic_number % 2 == 0:
                    room.amenity.add(a)
            for f in facilities:
                magic_number = random.randint(0, 15)
                if magic_number % 2 == 0:
                    room.facility.add(f)
            for r in rules:
                magic_number = random.randint(0, 15)
                if magic_number % 2 == 0:
                    room.house_rules.add(r)
        self.stdout.write(self.style.SUCCESS(f"{number} users created! "))
```

# 9.6 seed_reviews (5:34)

```
import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from reviews import models as review_models
from rooms import models as room_models
from users import models as user_models


class Command(BaseCommand):
    help = "This commnad creates reviews"

    def add_arguments(self, parser):
        parser.add_argument("--number", default=2, type=int, help="create seed reviews")

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()

        users = user_models.User.objects.all()
        rooms = room_models.Room.objects.all()
        seeder.add_entity(
            review_models.Review,
            number,
            {
                "accuracy": lambda x: random.randint(0, 6),
                "communication": lambda x: random.randint(0, 6),
                "cleanliness": lambda x: random.randint(0, 6),
                "location": lambda x: random.randint(0, 6),
                "check_in": lambda x: random.randint(0, 6),
                "value": lambda x: random.randint(0, 6),
                "room": lambda x: random.choice(rooms),
                "user": lambda x: random.choice(users),
            },
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} reviews created!"))
```

# 9.7 seed_lists (6:55)

```
import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from lists import models as list_models
from users import models as user_models
from rooms import models as room_models


NAME = "lists"


class Command(BaseCommand):

    help = f"This command creates {NAME}"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=2, type=int, help=f"How many {NAME} you want to create"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        users = user_models.User.objects.all()
        rooms = room_models.Room.objects.all()
        seeder.add_entity(
            list_models.List, number, {"user": lambda x: random.choice(users)}
        )

        created = seeder.execute()
        cleaned = flatten(list(created.values()))
        for pk in cleaned:
            list_model = list_models.List.objects.get(pk=pk)
            to_add = rooms[random.randint(0, 5) : random.randint(6, 30)]
            list_model.rooms.add(*to_add)

        self.stdout.write(self.style.SUCCESS(f"{number} {NAME} created!"))

```

# 9.8 seed_reservations (10:19)

```
import random
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from django_seed import Seed
from reservations import models as reservation_models
from rooms import models as room_models
from users import models as user_models

NAME = "reservations"


class Command(BaseCommand):
    help = f"This commnad creates {NAME}"

    def add_arguments(self, parser):
        parser.add_argument("--number", default=2, type=int, help=f"create seed {NAME}")

    def handle(self, *args, **options):
        number = options.get("number")
        users = user_models.User.objects.all()
        rooms = room_models.Room.objects.all()

        seeder = Seed.seeder()
        seeder.add_entity(
            reservation_models.Reservation,
            number,
            {
                "guest": lambda x: random.choice(users),
                "room": lambda x: random.choice(rooms),
                "check_in": lambda x: datetime.now(),
                "check_out": lambda x: datetime.now()
                + timedelta(days=random.randint(3, 25)),
            },
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} {NAME} created! "))


```
