from rest_framework import serializers
from .models import *


class CategorySerialier(serializers.ModelSerializer):
    class Meta:
        model = Category 
        fields = "__all__"

class ProjectImageSerialier(serializers.ModelSerializer):
    class Meta:
        model = ProjectImage 
        fields = "__all__"

class ProjectSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(many=True)
    project_images = ProjectImageSerialier(many=True)

    class Meta:
        model = Project 
        fields = "__all__"


class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill 
        fields = "__all__"


class AboutmeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutMe 
        fields = ['id', 'resume', 'readme', 'currentStatus', 'codingAchievement', 'myImage']