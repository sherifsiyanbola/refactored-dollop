# Generated by Django 3.2.4 on 2021-07-05 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0019_auto_20210704_0118'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='time',
            field=models.IntegerField(blank=True, help_text='duration of exam in minutes', null=True),
        ),
    ]
