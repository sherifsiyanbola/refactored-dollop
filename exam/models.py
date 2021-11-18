from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE
# from django.contrib.auth.models import User

class ExamGroup(models.Model):
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    lecturer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Exam(models.Model):
    exam_key = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, default="test")
    nodigital = models.BooleanField(blank=True, null=True)
    uploadpdf = models.FileField(upload_to='exams/', blank=True, null=True)
    editor = models.TextField(blank=True, null=True)
    time = models.DateTimeField(help_text="duration of exam in minutes", blank=True, null=True)
    first_name = models.BooleanField(default=False)
    last_name = models.BooleanField(default=False)
    email = models.BooleanField(default=False)
    student_class = models.BooleanField(default=False)
    teacher_name = models.BooleanField(default=False)
    student_id = models.BooleanField(default=False)
    calc = models.BooleanField(blank=True, null=True)
    desmos_calc = models.BooleanField(blank=True, null=True)
    anonymize = models.BooleanField(default=False)
    exam_open = models.BooleanField(default=False, verbose_name='Open/Close')
    lecturer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    group = models.ForeignKey(ExamGroup, on_delete=models.CASCADE, blank=True, null=True)
    resume_exam_key = models.CharField(max_length=255, blank=True, null=True)
    require_high_security = models.BooleanField(default=False)
    anonymous_exam = models.BooleanField(default=False)
    prefer_high_security = models.BooleanField(default=False)
    any_browser = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Answer(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, blank=True, null=True, default="N/A")
    last_name = models.CharField(max_length=255, blank=True, null=True, default="N/A")
    email = models.EmailField(blank=True, null=True)
    student_class = models.CharField(max_length=255, blank=True, null=True)
    teacher_name = models.CharField(max_length=255, blank=True, null=True, default="N/A")
    student_id = models.CharField(max_length=255, blank=True, null=True)
    answer_area = models.TextField(blank=True, null=True)
    submitted = models.BooleanField(blank=True, null=True, default=False)
    browser_type = models.CharField(max_length=255, blank=True, null=True)
    started_exam = models.BooleanField(blank=True, null=True)
    date = models.DateTimeField(auto_now=True)
    student_secrete_key = models.CharField(max_length=255, blank=True, null=True)
    reveal_details = models.BooleanField(blank=True, null=True, default=False)

    class Meta:
        ordering = ['-date',]

    def __str__(self):
        return str(self.exam)

class ExamAccess(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    lecturer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    access_level = models.CharField(max_length=255, choices=(
        ('owner', 'owner'),
        ('viewer', 'viewer')
    ))
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.exam)

    class Meta:
        verbose_name_plural = 'Exam Access'
    

class Student(models.Model):
    exam_key = models.CharField(max_length=255)
    started = models.BooleanField(default=False)
    bio_data = models.TextField()
    answer = models.TextField()
    student_id = models.CharField(max_length=255)
    student_submission_id = models.CharField(max_length=255, blank=True, null=True)  
    status = models.CharField(max_length=255, choices=(
        ('submitted', 'submitted'),
        ('logged out', 'logged out'),
    ))
    
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.student_id
    
class StudentAnswerPicture(models.Model):
    picture = models.ImageField(upload_to='media/answers')
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.student)
    