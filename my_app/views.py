from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import *
from .serializers import ProjectSerializer, SkillsSerializer, AboutmeSerializer, CategorySerialier


# Create your views here.


class MyProjectsView(ReadOnlyModelViewSet):
    queryset = Project.objects.all().order_by('-created_date')
    serializer_class = ProjectSerializer

class SkillsView(ReadOnlyModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillsSerializer

class AboutmeView(ReadOnlyModelViewSet):
    queryset = AboutMe.objects.all()
    serializer_class = AboutmeSerializer

class CategoryView(ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerialier