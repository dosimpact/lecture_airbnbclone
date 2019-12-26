from django.db import models
from core.models import TimeStampedModel

# Create your models here.
class snippets(TimeStampedModel):
    GENDER_MALE = "male"
    GENDER_SHEMALE = "shmale"
    GENDER_OTHER = "other"
    GENDER_CHOICE = (
        (GENDER_MALE, "boys"),
        (GENDER_SHEMALE, "girls"),
        (GENDER_OTHER, "alien"),
    )
    name = models.TextField(default="", null=True, blank=True)
    gender = models.CharField(
        default="GENDER_MALE", choices=GENDER_CHOICE, max_length=10
    )

