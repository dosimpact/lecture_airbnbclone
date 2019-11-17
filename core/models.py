from django.db import models

# Create your models here.
class TimeStampedModel(models.Model):
    """ Time Stampe Model """

    created = models.DateTimeField()
    updated = models.DateTimeField()

    # 추상 Ture라면 DB로 모델이 안들어간다.
    class Meta:
        abstract = True
