from ast import Return
from django.http import HttpResponse
from django.shortcuts import render
from flask import request
import pymysql
from datetime import date
import json
import requests
import urllib.request
from datetime import datetime
from urllib.request import Request, urlopen

import requests
con=pymysql.connect(host="localhost",user="root",password="Bhushan@123",database="mitra")

def addStudent(request):
    return render(request,"viewstudent.html")

def addTpo(request):
    return render(request,"viewtpo.html")


def viewtpo(request):

    sql="select * from userdata";
    cur1=con.cursor()
    cur1.execute(sql)
    result=cur1.fetchall()
    payload = []
    content={}
    
    for row in result:
        content = {'name': row[1], 'contact': row[3], 'email': row[2]}
        payload.append(content)
        content = {}
    print(f"json: {json.dumps(payload)}")
   
    return render(request,"viewtpo.html", {'list': {'items':payload}})


def viewstudent(request):
    sql="select * from userdata";
    cur1=con.cursor()
    cur1.execute(sql)
    result=cur1.fetchall()
    payload = []
    content={}
    
    for row in result:
        content = {'name': row[1], 'contact': row[3], 'email': row[2]}
        payload.append(content)
        content = {}
    print(f"json: {json.dumps(payload)}")
   
    return render(request,"viewstudent.html", {'list': {'items':payload}})




