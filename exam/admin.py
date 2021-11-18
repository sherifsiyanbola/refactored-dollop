from django.contrib import admin
from .models import ExamGroup, Answer, Exam, ExamAccess, Student, StudentAnswerPicture
# from .forms import ExamForm


# @admin.register(ExamGroup)
# class ExamGroupAdmin(admin.ModelAdmin):
#     list_display = ('name', 'color', 'lecturer')

admin.site.register(Answer)

# @admin.register(Exam)
# class ExamForm(admin.ModelAdmin):
#     # form = ExamForm
#     list_display = ('title', 'lecturer', 'timestamp', 'group')

admin.site.register(Exam)
# @admin.register(ExamAccess)
# class ExamAccessAdmin(admin.ModelAdmin):
#     list_display = ('exam', 'lecturer', 'timestamp')


# class StudentAnswerPictureInline(admin.StackedInline):
#     model = StudentAnswerPicture
#     extra = 1


# @admin.register(Student)
# class StudentAdmin(admin.ModelAdmin):
#     list_display = ('started', 'student_id', 'student_submission_id', 'status', 'timestamp')
#     inline = [StudentAnswerPictureInline]