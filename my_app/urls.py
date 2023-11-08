from django.urls import path, include
from my_app.views import MyProjectsView, AboutmeView, SkillsView, CategoryView
from rest_framework.routers import DefaultRouter 

router = DefaultRouter()

router.register('projects', MyProjectsView, basename='projects')
router.register('skills', SkillsView, basename='skills')
router.register('about-me', AboutmeView, basename='about-me')
router.register('project-categories', CategoryView, basename='project-categories')


urlpatterns = [
    path('', include(router.urls)),
]
