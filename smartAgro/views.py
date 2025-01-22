from django . shortcuts import render
from intranet.models import*
import random

def smartagro(request):
    # Get random news
    news_count = News.objects.count()
    random_news = News.objects.all()
    if news_count > 5:
        random_news = random.sample(list(random_news), 5)
    
    # Get random tasks
    task_count = Task.objects.count()
    random_tasks = Task.objects.all()
    if task_count > 5:
        random_tasks = random.sample(list(random_tasks), 5)

    # Get random employees
    employee_count = Employee.objects.count()
    random_employees = Employee.objects.all()
    if employee_count > 5:
        random_employees = random.sample(list(random_employees), 5)
    
    return render(request, 'home.html', {
        'random_news': random_news,
        'random_tasks': random_tasks,
        'random_employees': random_employees,
    })


def news_detail(request, pk):
    news_item = News.objects.get(pk=pk)
    return render(request, 'news_detail.html', {'news_item': news_item})

