# Generated by Django 3.1.7 on 2021-04-07 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0007_auto_20210407_1331'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todolist',
            old_name='id',
            new_name='model_id',
        ),
    ]
