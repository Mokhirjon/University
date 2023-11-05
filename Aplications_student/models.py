from django.db import models

# Create your models here.
class AplicationModel(models.Model):
    name = models.CharField(max_length=40,default='')
    mail = models.EmailField()
    if_student_older_than_17 = models.BooleanField()
    student_passport = models.ImageField(upload_to='Student_passport/')
    Diploma = models.ImageField(upload_to='students_diploma/')
    contact_with_admin = models.CharField(max_length=40,default='')
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'Aplication'