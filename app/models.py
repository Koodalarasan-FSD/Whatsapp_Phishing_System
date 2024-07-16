from django.db import models

# Create your models here.
class DateTimeRecord(models.Model):
    id = models.IntegerField(primary_key=True)  # Primary key
    failed_click_datetime = models.DateTimeField(null=True, blank=True)
    failed_responded_datetime = models.DateTimeField(null=True, blank=True)  


