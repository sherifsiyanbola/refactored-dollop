# Generated by Django 3.2.4 on 2021-06-16 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0005_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='answer_area',
            field=models.TextField(blank=True, null=True),
        ),
    ]