from rest_framework import serializers
from .models import UniversityModel

class Universerializers(serializers.ModelSerializer):
    class Meta:
        model = UniversityModel
    fields = ('name','when_created','Who_created','photo','university_bio','location','contact_with_admin')