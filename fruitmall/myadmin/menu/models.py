from django.db import models

# Create your models here.
class Menumessage(models.Model):
    name=models.CharField(max_length=50)
    ismenu=models.BooleanField(default=False)
    isDelete = models.BooleanField(default=False)
    rank=models.IntegerField(default=0,blank=True)
    pid=models.ForeignKey('self', null=True, blank=True,on_delete=models.SET_NULL)

