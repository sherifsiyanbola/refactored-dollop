# Generated by Django 3.2.5 on 2021-09-28 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0042_auto_20210909_1252'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='anonymous_exam',
            field=models.BooleanField(default=False),
        ),
    ]