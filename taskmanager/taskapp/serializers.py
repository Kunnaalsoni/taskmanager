from rest_framework import serializers
from .models import Task


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = [
            'id',
            'title',
            'description',
            'status',
            'created_at',
            'updated_at',
       ]

