from django.db import models
from django.utils.crypto import get_random_string

# Create your models here.
class Subject(models.Model):
    sub_id=models.CharField(max_length=64)
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name

def new_file_name(instance, filename):
    return 'media/{0}{1}'.format(get_random_string(length=10),filename)

class Register(models.Model):
    name = models.CharField(max_length=64)
    password = models.CharField(max_length=64)

class AdminRegister(models.Model):
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64)


class StudentReg(models.Model):
    firstName = models.CharField(max_length = 100)
    lastName = models.CharField(max_length = 100)
    date_of_birth = models.CharField(max_length=20, default=False)
    fatherName = models.CharField(max_length = 100)
    motherName = models.CharField(max_length = 100)
    board = models.CharField(max_length = 50)
    qualification = models.CharField(max_length = 30)
    schoolName = models.CharField(max_length = 30)
    schoolAddress = models.CharField(max_length = 200)
    homeAddress = models.CharField(max_length = 200)
    state = models.CharField(max_length = 30, default = False)
    examMode = models.CharField(max_length = 10)
    aadharNumber = models.CharField(max_length = 15)
    phoneNumber = models.CharField(max_length = 12)
    emailID = models.EmailField(max_length = 40)
    personPhoto = models.ImageField(upload_to = new_file_name,
                                        blank = True,
                                        null = True,)
    signaturePhoto = models.ImageField(upload_to = new_file_name,
                                        blank = True,
                                        null = True,)
    username = models.CharField(max_length = 30, default = False)
    #password = models.CharField(max_length = 50, default = False)


class Quiz(models.Model):
    question = models.CharField(max_length = 200)
    choice_one = models.CharField(max_length = 200)
    choice_two = models.CharField(max_length = 200)
    choice_three = models.CharField(max_length = 200)
    choice_four = models.CharField(max_length = 200)
    choice_five = models.CharField(max_length = 200)
    answer = models.CharField(max_length = 200)

    def __str__(self):
        return self.question


class LoginClass(models.Model):
    username = models.CharField(max_length = 30,primary_key=True)
    dob = models.CharField(max_length=20,default=False,null = False)

class ExamCode(models.Model):
    code = models.CharField(max_length = 15)

class SubjectCode(models.Model):
    code = models.CharField(max_length = 15)

class Questions(models.Model):
    question_no=models.IntegerField()
    question = models.CharField(max_length = 500)
    option1 = models.CharField(max_length = 50)
    option2 = models.CharField(max_length = 50)
    option3 = models.CharField(max_length = 50)
    option4 = models.CharField(max_length = 50)
    answer = models.CharField(max_length = 50)
    subject_code = models.CharField(max_length = 30)
    exam_code = models.CharField(max_length = 30)

