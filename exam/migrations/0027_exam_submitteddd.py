# Generated by Django 3.2.4 on 2021-07-13 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0026_auto_20210712_2357'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='submitteddd',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
