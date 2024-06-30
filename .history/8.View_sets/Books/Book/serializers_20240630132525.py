from rest_frameowork import serialaizers
from .models import *

class StudentSerializer(serialaizers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"