# Generated by Django 4.2.6 on 2023-11-05 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aplications_student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aplicationmodel',
            name='Diploma',
            field=models.ImageField(upload_to='students_diploma/'),
        ),
    ]
