from django.db import models

class Question(models.Model):
    text = models.CharField(max_length=255)
    correct_option = models.IntegerField()

    def __str__(self):
        return self.text

class Score(models.Model):
    user = models.CharField(max_length=100)
    value = models.IntegerField()

    def __str__(self):
        return f"{self.user} - {self.value}"
