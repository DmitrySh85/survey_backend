from django.db import models
from employees.models import Employee


class Item(models.Model):
    name = models.CharField()
    description = models.TextField(max_length=500, null=True, blank=True)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ["price"]


class Order(models.Model):
    CHOICES = (
        ("ORDERED", "Заказан"),
        ("ISSUED", "Выдан")
    )
    item = models.ForeignKey(Item, on_delete=models.PROTECT)
    purchaser = models.ForeignKey(Employee, on_delete=models.CASCADE)
    status = models.CharField(choices=CHOICES, default="ORDERED")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.item} для {self.purchaser} от {self.created_at}"

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
        ordering = ["-created_at"]
