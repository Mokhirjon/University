# Generated by Django 4.2.6 on 2023-10-29 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AplicationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=40)),
                ('mail', models.EmailField(max_length=254)),
                ('if_student_older_than_17', models.BooleanField()),
                ('student_passport', models.ImageField(upload_to='Student_passport/')),
                ('Diploma', models.ImageField(upload_to='students_passport/')),
                ('contact_with_admin', models.CharField(default='', max_length=40)),
            ],
            options={
                'db_table': 'Aplication',
            },
        ),
    ]