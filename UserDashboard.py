from django.http import HttpResponse
from django.shortcuts import render
from mysqlx import Column
from numpy import column_stack
import pymysql
from datetime import date

import requests
from pathlib import Path

import requests
from urllib import response
import requests

from urllib.request import urlopen

from django.test import TestCase
from urllib import response
import requests
import json
from urllib.request import urlopen

con=pymysql.connect(host="localhost",user="root",password="Bhushan@123",database="mitra")

def insertTpodata(request):
    return render(request,"addTpo.html")  

    

def tporeg(request):
    nm=request.POST.get('name')
    ct=request.POST.get('contact')
    em=request.POST.get('email')
    pa=request.POST.get('passw')
    cur=con.cursor()
    sql="insert into userdata(name,contact,email,passw,columnrole)values(%s,%s,%s,%s,%s)";
    values=(nm,ct,em,pa,'Tpo')
    cur.execute(sql,values)
    con.commit()
    print("done")
    
    return render(request,"addTpo.html")  

def insertstudentdata(request):
    return render(request,"addStudent.html")

def studreg(request):
    nm=request.POST.get('name')
    ct=request.POST.get('contact')
    em=request.POST.get('email')
    pa=request.POST.get('passw')
    cur=con.cursor()
    sql="insert into userdata(name,contact,email,passw,columnrole)values(%s,%s,%s,%s,%s)";
    values=(nm,ct,em,pa,'Student')
    cur.execute(sql,values)
    con.commit()
    print("done")

    return render(request,"addStudent.html")


def profile(request):
    return render(request,"profile.html")


def SSC(request):
    nm=request.POST.get('pass_year')
    ct=request.POST.get('name_board')
    em=request.POST.get('percent')
    pa=request.POST.get('cgpa')
    cur=con.cursor()
    sql="insert into SSC(pass_year,name_board,percent,cgpa)values(%s,%s,%s,%s)";
    values=(nm,ct,em,pa)
    cur.execute(sql,values)
    con.commit()
    
    
    return render(request,"HSCorDiploma.html")

def HSC(request):
    
    return render(request,"HSC.html")

def insertHSCdata(request):
    nm=request.POST.get('br_name')
    ct=request.POST.get('yer_pass')
    em=request.POST.get('spe_name')
    pa=request.POST.get('mark')
    cg=request.POST.get('cgpa')
    cur=con.cursor()
    sql="insert into HSC(br_name,yer_pass,spe_name,mark,cgpa)values(%s,%s,%s,%s,%s)";
    values=(nm,ct,em,pa,cg)
    cur.execute(sql,values)
    con.commit()
    return render(request,"Graduation.html")



def graduction(request):
    return render(request,"Graduation.html")

def graductiondata(request):
    nm=request.POST.get('yer_pass')
    ct=request.POST.get('un_name')
    em=request.POST.get('gr_percent')
    pa=request.POST.get('gr_cgpa')
    
    cur=con.cursor()
    sql="insert into Graduction(yer_pass,un_name,gr_percent,gr_cgpa)values(%s,%s,%s,%s)";
    values=(nm,ct,em,pa)
    cur.execute(sql,values)
    con.commit()
    print("done")
    return render(request,"BE.html")

def diploma(request):
    return render(request,"Diploma.html")

def diplomadata(request):
    nm=request.POST.get("year")
    bord=request.POST.get("board")
    branch=request.POST.get("branch")
    percent=request.POST.get("per")

    cur=con.cursor()
    sql="insert into diploma(year,board,branch,per)values(%s,%s,%s,%s)";
    values=(nm,bord,branch,percent)
    cur.execute(sql,values)
    con.commit()

    return render(request,"Graduation.html")

def BE(request):
    return render(request,"BE.html")


def BEdata(request):
    nm=request.POST.get("seme")
    
    percent=request.POST.get("par")
    cgpa=request.POST.get("cgpa")

    cur=con.cursor()
    sql="insert into BE(seme,par,cgpa)values(%s,%s,%s)";
    values=(nm,percent,cgpa)
    cur.execute(sql,values)
    con.commit()
    return render(request,"Traning.html")

def Traning(request):
    return render(request,"Traning.html")

def Traningdata(request):
    cm=request.POST.get("company_name")
    jt=request.POST.get("job_title")
    po=request.POST.get("section")
    st=request.POST.get("start_date")
    ed=request.POST.get("end_date")
    sp=request.POST.get("stipend")
    cur=con.cursor()
    sql="insert into Traning(company_name,job_title,section,start_date,end_date,stipend)values(%s,%s,%s,%s,%s,%s)";
    values=(cm,jt,po,st,ed,sp)
    cur.execute(sql,values)
    con.commit()

    return render(request,"Placenotplace.html")


def Place(request):
    return render(request,"Placenotplace.html")

def Placementdata(request):
    cm=request.POST.get("name_cmp")
    jt=request.POST.get("pack_offerd")
    po=request.POST.get("LOI")
    st=request.POST.get("date")
    cur=con.cursor()
    sql="insert into Placement(name_cmp,pack_offerd,LOI,date)values(%s,%s,%s,%s)";
    values=(cm,jt,po,st)
    cur.execute(sql,values)
    con.commit()
    return render(request,"Backlog.html")

def Backlog(request):
    return render(request,"Backlog.html")

def Backlogdata(request):
    cm=request.POST.get("Curbacklog")
    jt=request.POST.get("Total_backlog")
    po=request.POST.get("SSC_backlog")
    st=request.POST.get("HSC_backlog")
    be=request.POST.get("BE_gap")
    edu=request.POST.get("Educ_gap")
    dt=request.POST.get("Date")

    cur=con.cursor()
    sql="insert into backgap(Curbacklog,Total_backlog,SSC_backlog,HSC_backlog,BE_gap,Educ_gap,Date)values(%s,%s,%s,%s,%s,%s,%s)";
    values=(cm,jt,po,st,be,edu,dt)
    cur.execute(sql,values)
    con.commit()
    return render(request,"Backlog.html")

def HSCorDiploma(request):
    return render(request,"HSCorDiploma.html")

def ViewstudentDetails(request):
    sql="select * from ssc";
    cur1=con.cursor()
    cur1.execute(sql)
    result=cur1.fetchall()
    payload = []
    content={}
    
    for column in result:
        content = {'pass_year':column[1], 'name_board': column[2], 'percent': column[3],'cgpa':column[4]}
        payload.append(content)
        content = {}
    print(f"json: {json.dumps(payload)}")


    
    return render(request,"ViewstudentDetails.html")



def updatestud(request):
    return render(request,"update.html")

def update(request):
    return render(request,"update.html")