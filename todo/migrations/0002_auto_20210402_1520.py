# Generated by Django 3.1.7 on 2021-04-02 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='priority',
            field=models.CharField(choices=[('HIGH', 'H'), ('MEDIUM', 'M'), ('LOW', 'L')], max_length=6),
        ),
    ]