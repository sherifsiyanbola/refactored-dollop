# Generated by Django 3.2.4 on 2021-06-17 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0006_answer_answer_area'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='uploadpdf',
            field=models.FileField(default='test', upload_to='media/exams'),
        ),
    ]
