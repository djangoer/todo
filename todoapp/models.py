from django.db import models

# Create your models here.
class todo(models.Model):
    task=models.CharField(max_length=200)
    time=models.DateTimeField()
    def __unicode__(self):
        return self.task