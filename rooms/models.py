from django.db import models

class Room(models.Model:
    name = models.CharField(max_length=200)
    description = models.TextField()
    length = models.IntegerField()
    width = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title