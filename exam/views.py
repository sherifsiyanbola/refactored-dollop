from django.contrib.messages.api import success
from django.http import HttpResponseRedirect
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
import json
import secrets
from django.contrib.auth.decorators import login_required
from .models import Answer, ExamGroup, Exam, ExamAccess
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt




# def index(request):
#     return render(request, 'account/login.html')

def create_exam_group(request):
    json_data = json.loads(request.body)
    body = json_data['body']
    name = body['name']
    color = body['color']
    lecturer = request.user
    ExamGroup.objects.create(
        name = name,
        color= color,
        lecturer=lecturer
    )
    return redirect('exam_list')

@csrf_exempt
def create_exam(request):
    if request.method == 'POST':  
        Exam.objects.create(
            exam_key = secrets.token_hex(3),
            title = request.POST.get('title'),
            nodigital =True if request.POST.get('nodigital') else False,
            uploadpdf = request.FILES.get('uploadpdf'),
            editor = request.POST.get('editor'),
            first_name =True if request.POST.get('first_name') else False,
            last_name =True if request.POST.get('last_name') else False,
            email =True if request.POST.get('email') else False,
            student_class =True if request.POST.get('student_class') else False,
            teacher_name =True if request.POST.get('teacher_name') else False,
            student_id =True if request.POST.get('student_id') else False,
            calc =True if request.POST.get('calc') else False,
            desmos_calc =True if request.POST.get('desmos_calc') else False,
            any_browser =True if request.POST.get('any_browser') else False,
            require_high_security =True if request.POST.get('require_high_security') else False,
            anonymous_exam = True if request.POST.get('anonymous_exam') else False,
            resume_exam_key = secrets.token_hex(4),
            lecturer = request.user,
            
        )
        
        messages.success(request, 'Exam successfully created')
        # return redirect('exam_list')
        return JsonResponse({'sucess':'success'})
    else:
        return render(request, 'exam/create_exam.html')

        

        

# def _create_exam(request):
#     if request.method == 'POST':
#         json_data = json.loads(request.body)
#         body = json_data['body']
#         Exam.objects.create(
#             title = body['title'],
#             pdf_file = '',
#             questions = body['questions'],
#             options = body['options'],
#             security_level = body['security_level'],
#             lecturer= request.user,
#             group = ExamGroup.objects.get(id= int(body['group'])) or None
#         )
#     return redirect('exam_list')

def create_exam_access(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        body = json_data['body']
        ExamAccess.objects.create(
            exam = Exam.objects.get(id =  int(body['exam'])),
            lecturer = request.user,
            access_level= body['access_level']
        )
        return redirect('exam_list')

@login_required
def exam_list(request):
    current_user = request.user
    exams = Exam.objects.filter(lecturer=current_user)
    return render(request, 'exam/exam_list.html', context={"exams": exams})


# # save view
# def save_exam(request, id):
#     exam = Exam.objects.get(id=id)
#     answers = Answer.objects.filter(exam=exam)
    
#     # for student_answer in answers: 
#     #     if student_answer.submitted == True:
#     #         return render(request, 'exam/exam_list.html')
#         # if request.method == 'GET':
#             # answer_id = int(request.GET.get('answer'))
#             # answer = Answer.objects.filter(id=answer_id)
#     if request.method == 'POST':
#         answer_id = int(request.GET.get('answer'))
#         answer = Answer.objects.filter(id=answer_id)
#         answer.update(
#             answer_area = request.POST['editor'],
#         )
        
#         # answer.save()
#         messages.success(request, 'Exam saved successfully')
#         # return redirect('exam_list')
#     else:
#         return render(request, 'exam/view_exam.html', context={"exam": exam})


# def view_exam(request, id):
#     user_agent = request.META['HTTP_USER_AGENT']
#     exam = Exam.objects.get(id=id)
#     # answers = Answer.objects.filter(exam=exam)
    
#     # for student_answer in answers: 
#     #     if student_answer.submitted == True:
#     #         return render(request, 'exam/exam_list.html')
#         # if request.method == 'GET':
#             # answer_id = int(request.GET.get('answer'))
#             # answer = Answer.objects.filter(id=answer_id)
#     if request.method == 'POST':
#         answer_id = int(request.GET.get('answer'))
#         answer = Answer.objects.filter(id=answer_id)
#         answer.update(
#             answer_area = request.POST['editor'],
#             # submitted = True,
#         )
        
#         return render(request, 'exam/view_exam.html', context={"exam": exam, "user_agent": user_agent})
#     else:
#         return render(request, 'exam/view_exam.html', context={"exam": exam, "user_agent": user_agent})




def view_exam(request, id):
    user_agent = request.META['HTTP_USER_AGENT']
    exam = Exam.objects.get(id=id)
    answers = Answer.objects.filter(exam=exam)
    # my_answer = Answer.objects.filter(exam=exam)
    
    for student_answer in answers: 
        if student_answer.submitted == True:
            messages.error(request, 'This exam is no more available')
            return render(request, 'account/login.html')
        # if request.method == 'GET':
            # answer_id = int(request.GET.get('answer'))
            # answer = Answer.objects.filter(id=answer_id)
        # elif  request.method == 'POST' and student_answer.submitted == False:
        elif 'save' in request.POST and student_answer.submitted == False:
            answer_id = int(request.GET.get('answer'))
            answer = Answer.objects.filter(id=answer_id)
            answer.update(
                answer_area = request.POST['editor'],
                # submitted = True,
            )
            
            # answer.save()
            # messages.success(request, 'Exam submitted successfully')
            return render(request, 'exam/view_exam.html', 
                          context={"exam": exam, "student_answer": student_answer})
            # return redirect('/')
        elif 'submit' in request.POST:
            answer_id = int(request.GET.get('answer'))
            answer = Answer.objects.filter(id=answer_id)
            answer.update(
                answer_area = request.POST['editor'],
                submitted = True,
            )
            
            messages.success(request, 'Exam submitted successfully')
            return redirect('/')
        else:
            return render(request, 'exam/view_exam.html', context={"exam": exam, "user_agent": user_agent})



# def timer_view(request, id):
#     exam = Exam.objects.get(id=id)

#     return JsonResponse({
#         'time': exam.time,
#     })

def exam_detail(request, id):
    exam = Exam.objects.get(id=id)
    return render(request, 'exam/exam_detail.html', context={"exam": exam})

def edit_exam(request, id):
    exams = Exam.objects.all()
    exam_group = ExamGroup.objects.all()
    exam = Exam.objects.get(id=id)
    examUpdate = Exam.objects.filter(id=id) 
    time = exam.time

    if request.POST:
        examUpdate.update(
            # title = request.POST['title'],
            # editor = request.POST['editor'],
            exam_open = request.POST.get('exam_open', False),
            # group = ExamGroup.objects.get(id=int(request.POST['examgroup'])),
            # uploadpdf = request.Files.get('uploadpdf')
            time = request.POST.get('time')
            # if request.FILES.get('image'):
            #     image = request.FILES.get('image')
            # else:
            #     image = exam.image
        )
        messages.success(request, 'Exam updated successfully')
        return HttpResponseRedirect(f'/exam-detail/{id}')
    return render(request, 'exam/edit_exam.html', context={"exam": exam, "exams": exams, "exam_group": exam_group})


def monitor_exam(request):
    current_user = request.user
    exams = Exam.objects.filter(lecturer=current_user)
    return render(request, 'exam/monitor_exam.html', context = {
        "exams": exams
    })


def surveilance(request):
    current_user = request.user
    exams = Exam.objects.filter(lecturer=current_user)
    return render(request, 'exam/surveilance.html', context={
        "exams": exams
    })


def surveilanceDetail(request, id):
    exam = Exam.objects.get(id=id)
    all_answers = Answer.objects.filter(exam=exam)
    answer = Answer.objects.filter(exam=exam).filter(submitted=True).count()
    started_exam = Answer.objects.filter(exam=exam).filter(started_exam=True).count()
    ongoing_exam = int(started_exam) - int(answer) 
    return render(request, 'exam/surveilance_detail.html', context={
        "exam": exam, "answer": answer, "started_exam": started_exam, "ongoing_exam": ongoing_exam, "all_answers": all_answers
    })


def individualAnswer(request, id):
    client_ip = request.META['REMOTE_ADDR']
    user_agent = request.META['HTTP_USER_AGENT']
    student_answer = Answer.objects.get(id=id)
    return render(request, 'exam/student_answer.html', context={
        "student_answer": student_answer, "client_ip": client_ip, "user_agent": user_agent
    })



def monitor_student(request):
    return render(request, 'exam/monitor_student.html')


def student_workspace(request):
    return render(request, 'exam/student_workspace.html')



def verify_exam(request):  
    user_agent = request.META['HTTP_USER_AGENT']  
    exam = Exam.objects.filter(exam_key=request.POST['key'])
    resume_exam_key = Exam.objects.filter(resume_exam_key=request.POST['key'])
    
    # if (exam.require_high_security and 'SEB' not in user_agent):
    #     messages.warning(request, 'You are not using Safe Exam Browser')
    # else:
    #     pass

    if exam:
        return render(request, 'exam/student_details.html', {"exam": exam[0], "user_agent": user_agent})
    else:
        messages.warning(request, 'Invalid exam key, please check and try again')
        return HttpResponseRedirect(f"/")


def take_exam(request):
    user_agent = request.META['HTTP_USER_AGENT']
    exam = Exam.objects.filter(exam_key=request.POST['key'])
    # student_check = Answer.objects.filter(student_id=request.POST['student_id'])
    answer = Answer.objects.create(
        exam = exam[0],
            first_name = request.POST.get('first_name'),
            last_name = request.POST.get('last_name'),
            email = request.POST.get('email'),
            student_class = request.POST.get('student_class'),
            teacher_name = request.POST.get('teacher_name'),
            student_id = request.POST.get('student_id'),
            started_exam = True,
            browser_type = request.META['HTTP_USER_AGENT'],
            student_secrete_key = secrets.token_hex(6),

        )
    answer.save()
    return HttpResponseRedirect(f"view-exam/{exam[0].id}?answer={answer.id}", {
        "exam": exam, "user_agent": user_agent
    })


# force submission
def force_submit(request, id):
    exam = Exam.objects.get(id=id)
    answers = Answer.objects.filter(exam=exam, submitted=False).order_by('-date')
    for each_answer in answers:
        if request.method == 'POST':
            # answer_id = int(request.GET.get('answer'))
            each_answer = Answer.objects.filter(id=each_answer.id)
            each_answer.update(
                # answer_area = request.POST['editor'],
                submitted = True,
            )
    return render(request, 'exam/see_unsubmitted.html', context={"answers": answers, "exam":exam})


    # if request.method == 'POST':
    #     answer_id = int(request.GET.get('answer'))
    #     answer = Answer.objects.filter(id=answer_id)
    #     answer.update(
    #         answer_area = request.POST['editor'],
    #         submitted = True,
    #     )
# def take_exam(request):
#     # print(request.POST['key'])
#     # if request.method == 'POST':  
#     #     Answer.objects.create(

#     #     )
#     exam = Exam.objects.filter(exam_key=request.POST['key'])
#     resume_exam_key = Exam.objects.filter(resume_exam_key=request.POST['key'])
#     answer_list = Answer.objects.filter(student_id=request.POST['student_id'])
#     print(resume_exam_key)
#     if exam:
#         if answer_list:
#             messages.warning(request, "You've already taken this exam")
#             return HttpResponseRedirect(f"/")
#         else:
#     # student_check = Answer.objects.filter(student_id=request.POST['student_id'])
#             answer = Answer.objects.create(
#                 exam = exam[0],
#                 firstname = request.POST['firstname'],
#                 lastname = request.POST['lastname'],
#                 email = request.POST['email'],
#                 student_class = request.POST['studentclass'],
#                 student_id = request.POST['student_id'],
#                 started_exam = True

#             )
#             answer.save()
        
#             return HttpResponseRedirect(f"view-exam/{exam[0].id}?answer={answer.id}")
#     else:
#         # return HttpResponse('exam key is invalid')
#         messages.warning(request, 'Invalid exam key, please check and try again')
#         return HttpResponseRedirect(f"/")
    

    # if exam:
    #     return redirect('exam_list')

# print("This is it ", secrets.token_hex(3))

def see_answer(request, id):
    exam = Exam.objects.get(id=id)
    answers = Answer.objects.filter(exam=exam).order_by('-date')

    return render(request, 'exam/see_results.html', context={"answers": answers, "exam":exam})
