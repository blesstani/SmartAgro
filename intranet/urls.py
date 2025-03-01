
from django.urls import path
from . import views
from .views import EmployeeListAPIView
from .views import upload_file


urlpatterns = [
    
    path('employee/', views.employee, name='employee'),
    path('task/', views.task,name='task'),
    path('transaction/', views.transaction, name='transaction'), 
    path('news/', views.news, name='news'),
    path('news/<int:pk>/', views.news_detail, name='news_detail'),
    path('about/', views.about, name='about'),
    path('document/',views.upload_file, name='document'),
    path('supplier/',views.supplier, name='supplier'),
    path('api/employees/', EmployeeListAPIView.as_view(), name='employee-list-api'),
    path('documents/', views.upload_file, name='upload_file'),
]