# Generated by Django 3.2.4 on 2021-06-10 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_todo_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='user_name',
            field=models.CharField(default='UNKNOWN', max_length=20),
        ),
    ]
