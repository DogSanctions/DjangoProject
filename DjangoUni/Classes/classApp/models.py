from django.db import models


class djangoClasses(models.Model):
    Title = models.CharField(max_length=60, default="", blank=True, null=False)
    Course = models.IntegerField(default="", blank=True, null=False)
    Instructor = models.CharField(max_length=60, default="", blank=True, null=False)
    Duration = models.FloatField(max_length=40, default="", blank=True, null=False)

    object = models.Manager()
