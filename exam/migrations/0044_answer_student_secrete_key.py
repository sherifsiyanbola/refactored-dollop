# Generated by Django 3.2.5 on 2021-09-29 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0043_exam_anonymous_exam'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='student_secrete_key',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
