# Generated by Django 3.0.8 on 2022-02-14 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logtoday', '0004_auto_20200705_1553'),
    ]

    operations = [
        migrations.AddField(
            model_name='goaltasks',
            name='task_context',
            field=models.TextField(blank=True, null=True, verbose_name='Task Context'),
        ),
    ]
