from django.shortcuts import render

from django.http import HttpResponse

from .models import Student


def index1(request):
    student = Student.objects.all()
    return render(request, 'App1\index1.html', {'Student': student})

