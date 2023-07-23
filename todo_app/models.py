from django.db import models

# Create your models here.

class todo_app(models.Model):
    message_id = models.AutoField(primary_key=True)
    date = models.DateField( auto_now=False, auto_now_add=True)
    head = models.CharField(max_length=100)
    message = models.CharField(max_length= 400)
    status = models.BooleanField(default=False)