from django.db import models
from core import models as core_models


class Conversation(core_models.TimeStampedModel):
    """ Conversation models Definition """

    participants = models.ManyToManyField(
        "users.User", related_name="conversations", blank=True
    )

    def __str__(self):
        return str(self.created)


class Message(core_models.TimeStampedModel):
    """ Message models Definition """

    message = models.TextField()
    user = models.ForeignKey(
        "users.User", related_name="messages", on_delete=models.CASCADE
    )
    conversation = models.ForeignKey(
        "Conversation", related_name="messages", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.user} say : {self.text}"
