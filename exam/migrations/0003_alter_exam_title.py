# Generated by Django 3.2.4 on 2021-06-16 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0002_auto_20210616_0919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='title',
            field=models.CharField(default='test', max_length=255),
        ),
    ]
