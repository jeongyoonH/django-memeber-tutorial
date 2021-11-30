from django.db import models

class Token(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField(auto_now_add=True)
    JWT = models.TextField()
