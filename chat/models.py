from django.db import models
from django.conf import settings
# from django.contrib.auth.models import User 
from exam.models import Student

class Conversation(models.Model):
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.timestamp)
    

class Message(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    lecturer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message =  models.TextField()
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.message)
    
    
