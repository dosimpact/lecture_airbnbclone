from django.db import models

# Create your models here.
class TimeStampedModel(models.Model):
    """ Time Stampe Model """

    created = models.DateTimeField(auto_now_add=True)  # 모델생성시 그때 날짜 저장
    updated = models.DateTimeField(auto_now=True)  # 모델save시 그때 날짜 저장

    # 추상 Ture라면 DB로 모델이 안들어간다.
    class Meta:
        abstract = True
