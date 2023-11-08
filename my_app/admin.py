from django.contrib import admin
from .models import *

# Register your models here.


class ProjectImagesAdmin(admin.StackedInline):
    list_display = ['id', 'project']
    model = ProjectImage

admin.site.register(ProjectImage)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'category_name']
    model = Category



class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'project_type', 'websiteLink', 'date']
    inlines = [ProjectImagesAdmin]


admin.site.register(Project, ProjectAdmin)




@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['id', 'skill_name', 'skill_level', 'skill_icon']
    model = Skill


@admin.register(AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    list_display = ['id', 'currentStatus', 'codingAchievement']
    model = AboutMe




