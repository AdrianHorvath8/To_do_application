# Generated by Django 4.0.1 on 2022-01-30 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='statement',
            field=models.BooleanField(default=False),
        ),
    ]