# Generated by Django 4.2.6 on 2023-11-05 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('University', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='universitymodel',
            name='photo',
            field=models.ImageField(upload_to='university_photos/'),
        ),
    ]