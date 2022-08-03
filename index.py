from ast import Return
from django.http import HttpResponse
from django.shortcuts import render
import pymysql
from django.test import TestCase
from difflib import SequenceMatcher


con=pymysql.connect(host="localhost",user="root",password="Bhushan@123",database="mitra")

def login(request):
    return render(request,"log.html")

def adminpage(request):
    sql="select * from userdata";
    cur=con.cursor()
    cur.execute(sql)
    data=cur.fetchall()
    email=request.POST.get('email')
    password=request.POST.get('passw')
    print(email)
    print(password)
    uname="";
    uid="";
    role="";
    
    
    if(email=="admin" and password=="admin"):
        print("print")
        return render(request,"adminpage.html")
        
    
    else:
        for x in data:
            if(x[2]==email and x[4]==password):
                uname=x[2]
                uid=x[4]
                role=x[5]
                
             
    if(role=="Student"):
        request.session['email']=uname
        request.session['pass']=uid
       
        return render(request,"studentpage.html" )
    
    if(role=="Tpo"):
        request.session['email']=uname
        request.session['pass']=uid
       
        return render(request,"tpopage.html" )
    else:
        result="Invalid Username or Password"
        return render(request,"log.html",{'data':result})

    
   #return render(request,"adminpage.html")

def home(request):
    return render(request,"home.html")


def studentpage(request):
    return render(request,"studentpage.html")

def logout(request):
    return render(request,"log.html")


