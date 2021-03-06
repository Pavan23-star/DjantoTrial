# Generated by Django 3.0.4 on 2020-03-20 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20200320_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='subjects',
            field=models.ManyToManyField(to='student.Subject'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='name',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
