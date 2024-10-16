from django.shortcuts import render
from .models import Student

# Create your views here.
def student_dashboard(request):
     return render(request, "dash/indexmain.html")

def student_list(request):
     students = Student.objects.all()
     return render(request,'dash/indexmain.html',{'students': students})
