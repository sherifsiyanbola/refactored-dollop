# Generated by Django 3.2.4 on 2021-07-01 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0016_auto_20210630_1139'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='submitted',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
