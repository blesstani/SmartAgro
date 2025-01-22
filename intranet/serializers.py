from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    department = serializers.StringRelatedField()  # Returns the string representation of the department
    role = serializers.StringRelatedField()  # Returns the string representation of the role

    class Meta:
        model = Employee
        fields = ['id', 'profile_pic', 'first_name', 'last_name', 'email', 'department', 'role']
