# Generated by Django 3.2.4 on 2021-07-04 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0018_answer_started_exam'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exam',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='exam',
            name='lastname',
        ),
        migrations.RemoveField(
            model_name='exam',
            name='number',
        ),
        migrations.AddField(
            model_name='exam',
            name='anonymize',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='exam',
            name='first_name',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='exam',
            name='last_name',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='exam',
            name='student_class',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='exam',
            name='student_id',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='exam',
            name='teacher_name',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='exam',
            name='email',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
