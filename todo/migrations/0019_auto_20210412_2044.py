# Generated by Django 3.1.7 on 2021-04-12 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0018_auto_20210408_2137'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notcompletedtasks',
            name='model_id',
        ),
        migrations.AddField(
            model_name='notcompletedtasks',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='notcompletedtasks',
            name='order',
            field=models.IntegerField(default=-1, unique=True),
        ),
    ]
