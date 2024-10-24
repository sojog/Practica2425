# Generated by Django 5.1.2 on 2024-10-24 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_answer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='question',
        ),
        migrations.AddField(
            model_name='question',
            name='questions',
            field=models.ManyToManyField(to='courses.answer'),
        ),
    ]