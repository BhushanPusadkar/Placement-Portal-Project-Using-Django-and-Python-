"""Recommendationsystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from . import index
from . import UploadDataset
from . import UserDashboard
from . import AdminDashboard
from django.urls.conf import include  
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',index.home),
    path('login',index.login),
    path('adminpage',index.adminpage),
    path('studentpage',index.studentpage),
    path('addStudent',AdminDashboard.addStudent),
    path('addTpo',AdminDashboard.addTpo),
    path('viewstudent',AdminDashboard.viewstudent),
    path('viewtpo',AdminDashboard.viewtpo),
    path('insertTpodata',UserDashboard.insertTpodata),
    path('insertstudentdata',UserDashboard.insertstudentdata),
    path('studreg',UserDashboard.studreg),
    path('tporeg',UserDashboard.tporeg),
    path('logout',index.logout),
    path('profile',UserDashboard.profile),
    path('SSC',UserDashboard.SSC),
    path('HSC',UserDashboard.HSC),
    path('insertHSCdata',UserDashboard.insertHSCdata),
    path('graduction',UserDashboard.graduction),
    path('graductiondata',UserDashboard.graductiondata),
    path('diploma',UserDashboard.diploma),
    path('diplomadata',UserDashboard.diplomadata),
    path('BE',UserDashboard.BE),
    path('BEdata',UserDashboard.BEdata),
    path('Traning',UserDashboard.Traning),
    path('Traningdata',UserDashboard.Traningdata),
    path('Place',UserDashboard.Place),
    path('Placementdata',UserDashboard.Placementdata),
    path('Backlog',UserDashboard.Backlog),
    path('Backlogdata',UserDashboard.Backlogdata),
    path('HSCorDiploma',UserDashboard.HSCorDiploma),
    path('ViewstudentDetails',UserDashboard.ViewstudentDetails),
    path('update',UserDashboard.update),
    path('updatestud',UserDashboard.updatestud),
    



]

