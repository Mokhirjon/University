from rest_framework import serializers
from .models import AplicationModel

class Aplicationserializer(serializers.ModelSerializer):
    class Meta:
        model = AplicationModel
        fields = ('name','mail','diploma','student_passport','if_student_older_than_17','contact_with_admin')