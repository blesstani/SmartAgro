
from django.shortcuts import render, get_object_or_404, redirect
from .models import News
from .models import Employee , Customer , Supplier, Transaction, Department,Task, Role
from .forms import DocumentForm
from .models import Document
from django.http import HttpResponse


# Create your views here.
def employee(request):
    employees=Employee.objects.all()
    task_list=Task.objects.all()
    return render(request,'intranet/employee.html',{'employees':employees, 'task':task_list,})

def supplier(request):
    suppliers=Supplier.objects.all()
    return render(request,'intranet/supplier.html',{'suppliers':suppliers,})



def task(request):
    tasks = Task.objects.all()
    employees = Employee.objects.all()
    recent_tasks=Task.objects.order_by('task_title')[:5]
    return render(request, 'intranet/task.html', {'tasks':tasks})


def transaction(request):
    transactions= Transaction.objects.all()
    return render(request,'intranet/transaction.html',{'transactions':transactions})



def about(request):
    return render(request,'intranet/about.html',)

def news(request):
    articles = News.objects.all()
    return render(request, 'intranet/news.html', {'articles': articles})

def news_detail(request, pk):
    news_item = News.objects.get(pk=pk)
    return render(request, 'intranet/news_detail.html', {'news_item': news_item})

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Employee
from .serializers import EmployeeSerializer

class EmployeeListAPIView(APIView):
    def get(self, request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)

from .models import Document
from .forms import DocumentForm

def upload_file(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = DocumentForm()

    documents = Document.objects.all()  # Retrieve all uploaded files
    return render(request, 'intranet/upload_file.html', {'form': form, 'documents': documents})