# Generated by Django 3.2.4 on 2021-06-17 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0008_alter_exam_uploadpdf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='uploadpdf',
            field=models.FileField(blank=True, null=True, upload_to='media'),
        ),
    ]
