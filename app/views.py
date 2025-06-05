from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from app.models import Student
from app.serializer import StudentSerializer


# Create your view
#
# s here.
@api_view(['POST'])
def save(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#ngrok
@api_view(['GET'])
def fetch(request):
    # students = Student.objects.create(name ="Joel Katana", email="joe@gmail.com", password="122345", gender="male", sport="soccer", education="college")
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)