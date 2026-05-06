from django.db import models


class Course(models.Model):
    coursecode = models.CharField(max_length=10)
    coursename = models.CharField(max_length=50)
    credits = models.IntegerField()

    def __str__(self):
        return f"{self.coursecode} - {self.coursename}"