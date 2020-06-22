from django.db import models


class djangoClasses(models.Model):
    Title = models.CharField(max_length=60, default="", blank=True, null=False)
    Course_Number = models.IntergerField(max_length=60, default="", blank=True, null=False)
    Instructor = models.CharField(max_length=60, default="", blank=True, null=False)
    Duration = models.CharField(max_length=60, default="", blank=True, null=False)

    object = models.Manager()

    def __str__(self):
        return self.name
