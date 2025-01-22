from django.db import models

#ROLE
class Role(models.Model):
    name = models.CharField(max_length=50)
    Role_CHOICES=[
        ('Worker','Worker'),
        ('Driver','Driver'),
        ('Controler','Controler'),
        ('Reporter','Reporter'),
        ('Editor','Editor'),
        ('Mechanic','Mechanic'),
    ]
    name = models.CharField(max_length=100, choices=Role_CHOICES)

    def __str__(self):
        return self.name  
    

#DEPARMENT
class Department(models.Model):
    Department_CHOICES=[
        ('Human Resource','Human Resource'),
        ('Production Department','Production Department'),
        ('Finance','Finance'),
        ('Quality Control ','Quality Control '),
        ('Marketing','Marketing'),
        ('Procurement and Supply Chain','Procurement and Supply Chain'),
        ('Maintenance and Engineering','Maintenance and Engineering'),
        ('Labourer','Labourer'),
    ]
    name = models.CharField(max_length=100, choices=Department_CHOICES)

    def __str__(self):
        return self.name

#EMPLOYEE
class Employee(models.Model):
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

#SUPPLIER
class Supplier(models.Model):
    profile_pic = models.ImageField(upload_to='supplier_pics/', blank=True, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

#CUSTOMER
class Customer(models.Model):
    profile_pic = models.ImageField(upload_to='customer_pics/', blank=True, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# TRANSACTION 
class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ('SOLD', 'SOLD'),
        ('PURCHASE', 'PURCHASE'),

    ]
    STATUS_CHOICES = [
        ('pending', 'pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    ]

    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.transaction_type} - {self.amount} - {self.status}"

# TASK 
class Task(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('assign', 'Assign'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]
    task_title = models.CharField(max_length=100)
    task_description = models.TextField()
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='pending')
    creator = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='created_tasks')
    performer = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='assigned_tasks')
    due_date = models.DateField()

    def __str__(self):
        return self.task_title

#NEWs
class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=100)
    publish_date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='news_images/', null=True, blank=True)

    def __str__(self):
        return self.title
    
class Document(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='documents/')  # Files will be uploaded to MEDIA_ROOT/documents/
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name