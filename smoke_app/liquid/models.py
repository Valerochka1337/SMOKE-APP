from django.db import models



class Liquid(models.Model):
    title = models.CharField(max_length=40)
    score = models.SmallIntegerField()
    volume = models.FloatField()
    strength = models.FloatField()
    description = models.TextField()
    is_produced = models.BooleanField(default=True)


    def __str__(self):
        return self.title