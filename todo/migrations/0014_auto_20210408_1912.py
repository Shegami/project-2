# Generated by Django 3.1.7 on 2021-04-08 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0013_auto_20210408_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uncompletedtask',
            name='model_id',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
    ]
