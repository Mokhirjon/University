from django.db import models
from datetime import datetime
# Create your models here.
class UniversityModel(models.Model):
    name = models.CharField(max_length=50,default='')
    when_created = models.DateField(default=datetime.now)
    Who_created = models.CharField(max_length=50,default='')
    photo = models.ImageField(upload_to='university_photos/')
    university_bio = models.TextField()
    location = models.CharField(max_length=50,default='')
    contact_with_admin = models.CharField(max_length=50,default='')

    def __str__(self):
        return self.name
    class Meta:
        db_table = "University"