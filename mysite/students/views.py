from types import NoneType
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import django.http as http
# Create your views here.
def home(request):
    students = Student.objects.all()
    return render(request,'home.html',{'students':students})
    

def student(request,student_id):
    try:
        student = Student.objects.get(id=student_id)
    except Student.DoesNotExist:
        student = None
    return render(request,'student.html',{'student':student})