import uuid

from django.db import models


class Employee(models.Model):

    ROLES = (
        ("ADMIN", "Admin"),
        ("MASTER", "Master")
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tg_id = models.BigIntegerField(unique=True)
    name = models.CharField(max_length=50)
    role = models.CharField(max_length=100, choices=ROLES, default="MASTER")
    created_at = models.DateTimeField(auto_now_add=True)
    points = models.IntegerField(default=0)
    is_blocked = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["created_at"]
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"
