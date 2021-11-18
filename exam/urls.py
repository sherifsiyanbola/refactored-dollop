from django.urls import path
from . import views

urlpatterns =  [
    path('create-exam-group', views.create_exam_group, name = 'create_exam_group'),
    path('create-exam', views.create_exam, name='create_exam'),
    # path('view-exam/<int:id>', views.save_exam, name='save_exam'),
    path('view-exam/<int:id>', views.view_exam, name='view_exam'),
    path('resume-exam/<int:id>', views.view_exam, name='resume_exam'),
    path('exam/<int:id>/edit/', views.edit_exam, name='edit_exam'),
    path('', views.exam_list, name='exam_list'),
    path('exam-detail/<int:id>', views.exam_detail, name='exam_detail'),
    path('monitor-exam', views.monitor_exam, name='monitor_exam'),
    path('see-answers/<int:id>', views.see_answer, name='see_answer'),
    path('verify-exam', views.verify_exam, name='verify_exam'),
    path('take-exam', views.take_exam, name='take_exam'),
    path('surveilance', views.surveilance, name='surveilance'),
    path('surveilance/<int:id>', views.surveilanceDetail, name='surveilance_detail'),    
    path('student-answer/<int:id>', views.individualAnswer, name='student_answer'),
    path('student-answer/<int:id>/force-submit/', views.force_submit, name='force_submit'),
    
]