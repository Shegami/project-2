# Generated by Django 3.1.7 on 2021-04-12 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0019_auto_20210412_2044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notcompletedtasks',
            name='order',
            field=models.IntegerField(default=0, unique=True),
        ),
    ]
