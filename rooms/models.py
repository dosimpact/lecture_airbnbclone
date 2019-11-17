from django.db import models  # 1.장고 관련 된것을 모두 임포트
from core import models as core_models  # 2. 서드파티 패키지 임포트
from django_countries.fields import CountryField  # 3. 그다음 내가 만든것 임포트
from users import models as user_models


class Room(core_models.TimeStampedModel):
    """ Room Models """

    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)

    guests = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()

    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    # 다른 모델과 연결. Foreignkey
    host = models.ForeignKey(user_models.User, on_delete=models.CASCADE)

