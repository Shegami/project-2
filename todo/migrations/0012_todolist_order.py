# Generated by Django 3.1.7 on 2021-04-08 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0011_auto_20210408_1827'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='order',
            field=models.IntegerField(default=0),
        ),
    ]
