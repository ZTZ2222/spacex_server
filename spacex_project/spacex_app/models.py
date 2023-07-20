from django.db import models

# Create your models here.


class MenuItem(models.Model):
    name = models.CharField(max_length=10, default="Link")
    title = models.CharField(max_length=20)
    href = models.CharField(max_length=20)

    def __str__(self) -> str:
        return str(self.name)


class StatsItem(models.Model):
    name = models.CharField(max_length=10, default="Block")
    top_text = models.CharField(max_length=50)
    center_text = models.CharField(max_length=50)
    bottom_text = models.CharField(max_length=50)
    direction = models.CharField(max_length=25)

    def __str__(self) -> str:
        return str(self.name)
