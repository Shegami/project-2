# Generated by Django 3.1.7 on 2021-04-08 16:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0012_todolist_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='UncompletedTask',
            fields=[
                ('model_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('priority', models.CharField(choices=[('H', 'High'), ('M', 'Medium'), ('L', 'Low')], default='High', max_length=6)),
                ('create_date', models.DateField(default=datetime.datetime.now)),
                ('status', models.CharField(default='uncompleted', max_length=11)),
            ],
        ),
        migrations.DeleteModel(
            name='ToDoList',
        ),
    ]