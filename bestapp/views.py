from django.shortcuts import render, redirect
from .models import Subject, Register, Quiz, AdminRegister, StudentReg, LoginClass, ExamCode, Questions, SubjectCode
from django.views.generic import UpdateView, CreateView
import random
# import  matplotlib.pyplot as plt
import sys
from django.core.mail import send_mail
from django.http import HttpResponse, JsonResponse
from pymongo import MongoClient
# from more_itertools import one
from django.db.models import Q
from django.contrib.auth.hashers import check_password, make_password

# Create your views here.

client = MongoClient()
db = client['bestproject']
name = ''
pas = ' '


def home(request):
    return render(request, 'home.html')


def dashbord(request):
    return render(request, 'dash.html')


def subject(request):
    if request.method == 'POST':
        id = request.POST['id1']
        name = request.POST['name']
        sub = Subject.objects.create(sub_id=id, name=name)
        sub.save()
        return redirect('/vsub')
    return render(request, 'subject.html')


def viewsubject(request):
    form = Subject.objects.all()
    return render(request, 'viewsubject.html', {'form': form})


def adminlogin(request):
    if request.method == 'POST':
        name = request.POST['t1']
        pas = request.POST['t2']
        dbadmin = AdminRegister.objects.filter(username=name, password=pas)
        if dbadmin:
            return redirect('/dash')
        else:
            return HttpResponse('login fail')


# def quiz(request):
#     return render(request,'quiz.html')

def addSuper(request):
    add = AdminRegister(username='admin', password='admin123')
    add.save()
    return HttpResponse("<h2>Admin added</h2>")


def results(request):
    result = {}
    result['exam_code'] = 'sb062019'
    result['exam_date'] = '15/12/2019'
    result['result_date'] = '20/12/2019'
    result['HighestMarks'] = 120
    result['AverageMarks'] = 89
    result['LowestMarks'] = 70

    list = [{'student_name': 'ggdgv', 'student_id': '154324145', 'board': 'state', 'marks': 120}]

    return render(request, 'results.html', {'res': result})


def applicationForm(request):
    if request.method=='POST':
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        dob = request.POST.get('dob')
        board = request.POST.get('board')
        father = request.POST.get("father")
        mother = request.POST.get("mother")
        qualification = request.POST.get('qualification')
        sname = request.POST.get('sname')
        saddress = request.POST.get('saddress')
        haddress = request.POST.get('haddress')
        anum = request.POST.get('aadharnum')
        phonenum = request.POST.get('phonenum')
        email = request.POST.get('email')
        personphoto = request.FILES.get('personphoto')
        signaturephoto = request.FILES.get('signaturephoto')
        state = request.POST.get('state')
        number = '19' + '{:03d}'.format(random.randrange(1, 999))
        username = (state + board + qualification + number)
        # password = dob
        af = StudentReg(firstName=fname, lastName=lname, date_of_birth=dob, board=board, fatherName=father,
                        motherName=mother, qualification=qualification, schoolName=sname, schoolAddress=saddress,
                        homeAddress=haddress, aadharNumber=anum, phoneNumber=phonenum, emailID=email,
                        personPhoto=personphoto, signaturePhoto=signaturephoto, state=state, username=username)
        af.save()
        sub = "Email From Best Scholarship"
        msg = "Hello Mr/Ms." + fname + "." + "\n" + "\n" + "Your Application for Best Scholarship has been submitted successfully" + "\n" + "Username:" + username + "\n" + "Password:" + dob + "\n" + "Please use the above Username and Dob to login" + "\n" + "Good Luck" + "\n" + "-Team Best Scholarship"
        send_mail(sub, msg, 'best.scholarstest@gmail.com', [email])
        return HttpResponse('mail sent successfully')
    return render(request,'application.html')


def studentlogin(request):
    username = request.POST.get('username')
    dob = request.POST.get('dob')
    afc = StudentReg.objects.filter(username=username, date_of_birth=dob)
    if afc:
        return render(request, "studentscreen.html", {'username': username, 'date_of_birth': dob})
    else:
        return HttpResponse("<h3>Invalid login credentials</h3>")


def logout(request):
    return render(request, "login.html", {"msgl": "Sucessfully Logout"})


def indexPage(request):
    return render(request, "index.html")


def application(request):
    return render(request, 'application.html')


def loginoptions(request):
    return render(request, 'logoptions.html')


def adminstudent(request):
    option = request.POST.get('option')
    if option == 'admin':
        return render(request, 'login.html')
    else:
        return render(request, 'studentlogin.html')


def studentselection(request):
    stdslc = request.POST.get('t1')
    user = request.POST.get('username')
    dob = request.POST.get('dob')
    collection1 = db['bestapp_studentreg']
    if stdslc == 'My Profile':
        data1 = list(collection1.find({'username': user, 'date_of_birth': dob}))
        for info in data1:
            info.pop('_id')
        # return JsonResponse(data1, safe = False)
        return render(request, 'profile.html', {'db': data1})
    elif stdslc == 'Mock Test':
        questions = db['bestapp_questions']
        qtndata = list(questions.find({}))
        for info in qtndata:
            info.pop('_id')
        return render(request, 'mocktest.html', {'qtn': qtndata})


def examcode(request):
    return render(request, 'examcode.html')


def examdelete(request):
    collection = db['bestapp_examcode']
    data = list(collection.find({}))
    for info in data:
        info.pop('_id')
    return render(request, 'examdel.html', {'data': data})


def examedit(request):
    collection = db['bestapp_examcode']
    data = list(collection.find({}))
    for info in data:
        info.pop('_id')
    return render(request, 'examedit.html', {'data': data})


def examscreen(request):
    return render(request, 'examall.html')


def addexamcode(request):
    cls = request.POST.get('t1')
    board = request.POST.get('t2')
    year = request.POST.get('t3')
    str = ''
    code = str + cls[:2] + board[:2] + year[:4]
    ExamCode(code=code).save()
    return HttpResponse("<h4>New Exam Code Created</h4>")


def delete(request):
    option = request.POST.get('option')
    collection = db['bestapp_examcode']
    cursor = collection.delete_one({'code': option})
    msg = 'deleted'
    return JsonResponse(msg, safe=False)


def subjectall(request):
    collection = db['bestapp_subjectcode']
    data = list(collection.find({}))
    for info in data:
        info.pop('_id')
    return render(request,'suball.html',{'data':data})






def subjectcode(request):
    return render(request, 'subcode.html')


def subjectdelete(request):
    collection = db['bestapp_subjectcode']
    data = list(collection.find({}))
    for info in data:
        info.pop('_id')
    return render(request, 'subdelete.html', {'data': data})


def subjectedit(request):
    collection = db['bestapp_subjectcode']
    data = list(collection.find({}))
    for info in data:
        info.pop('_id')
    return render(request, 'subedit.html', {'data': data})

def addsubjectcode(request):
    sub = request.POST.get('t1')
    cls = request.POST.get('t2')
    brd = request.POST.get('t3')
    str = ''
    code = str + sub + cls + brd
    SubjectCode(code=code).save()
    return HttpResponse('<h4>New Subject Code Added</h4>')



def addq(request):
    subcode = request.POST.get('ec')

    return render(request, 'addq.html', {'subcode': subcode})


def questionsadd(request):
    sub = request.POST.get('subcode')
    collection = db['bestapp_examcode']
    data = list(collection.find({}))
    for info in data:
        info.pop('_id')
    return render(request, 'questionadd.html', {'data': data, 'sub': sub})


def saveq(request):
    qtn_no = request.POST.get('no')
    question = request.POST.get('question')
    subcode = request.POST.get('subcode')
    examcode = request.POST.get('ecode')
    option1 = request.POST.get('option1')
    option2 = request.POST.get('option2')
    option3 = request.POST.get('option3')
    option4 = request.POST.get('option4')
    answer = request.POST.get('c')
    if answer == 'ans1':
        ans = option1
    elif answer == 'ans2':
        ans = option2
    elif answer == 'ans3':
        ans = option3
    elif answer == 'ans4':
        ans = option4
    else:
        return HttpResponse("<h4>Please select Answer</h4>")
    Questions(question_no=qtn_no, question=question, option1=option1, option2=option2, option3=option3, option4=option4,
              answer=ans, subject_code=subcode, exam_code=examcode).save()
    return HttpResponse('<h3>New Question Added</h3>')


def qtnselect(request):
    question_no = request.POST.get('question_no')
    collection = db['bestapp_questions']
    qtn = Questions.objects.filter(question_no=question_no)
    return render(request, 'display.html', {'qtn': qtn})


def submit(request):
    question_no = request.POST.get('question_no')
    option = request.POST.get('option')
    collection = db['bestapp_questions']
    qtn = Questions.objects.filter(question_no=question_no)
    if qtn['answer'] == option:
        return JsonResponse(option, safe=False)
    else:
        return HttpResponse('<h4>Wrong Answer</h4>')


def contactus(request):
    return render(request, 'contactus.html')