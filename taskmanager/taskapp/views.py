from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import PostSerializer
from .models import Task
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class TaskAPIView(APIView):
    
    def get(self, request, id=None):
        if id:
            print("GET on TaskAPIView with id")
            task = Task.objects.get(id=id)
            serializer = PostSerializer(task)
            return Response(serializer.data)
        print("GET on TaskAPIView") # DEBUG
        tasks = Task.objects.all()
        serializer = PostSerializer(tasks, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        print("POST on TaskAPIView")
        serializer = PostSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # else return BAD REQUEST
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, id=None):
        print("PATCH on TaskAPIView")
        task = Task.objects.get(id=id)
        serializer = PostSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        # else return BAD REQUEST
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id=None):
        print("DELETE on TaskAPIView")
        task = Task.objects.get(id=id)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)