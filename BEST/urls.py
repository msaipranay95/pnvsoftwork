"""realproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from bestapp import views
from django.views.generic import TemplateView
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home),
    path('dash/', views.dashbord),
    path('sub/', views.subject),
    path('vsub/', views.viewsubject, name='viewsubject1'),
    path('login/', views.loginoptions),
    path('results/',views.results),
    path('index/', views.indexPage),
    path('saveapplication/', views.applicationForm),
    path('options/',views.adminstudent),
    path('adminlogin/',views.adminlogin),
    path('studentlogin/',views.studentlogin),
    path('studentselection/',views.studentselection),
    path('examcode/',views.examcode),
    path('contactus/' ,views.contactus),
    path('examdel/',views.examdelete),
    path('examedit/',views.examedit),
    path('examscreen/',views.examscreen),
    path('addexamcode/',views.addexamcode),
    path('delete/',views.delete),
    path('suball/' , views.subjectall),
    path('subcode/',views.addsubjectcode),
    path('subdelete/',views.subjectdelete),
    path('subedit/',views.subjectedit),
    path('addq/',views.addq),
    path('questionadd/',views.questionsadd),
    path('saveq/',views.saveq),
    path('qtnselect/',views.qtnselect),
    path('submit/',views.submit),


    # url(r'^update/(?P<pk>\d+)/$', views.AdminUpdate.as_view()),

]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)


