from django.contrib import admin
from .models import AplicationModel
# Register your models here.
class Aplicationadmin(admin.ModelAdmin):
    search_fields = ['contact_with_admin','name']
    list_display = ('name','Diploma','student_passport','contact_with_admin','if_student_older_than_17','mail')

admin.site.register(AplicationModel,Aplicationadmin)