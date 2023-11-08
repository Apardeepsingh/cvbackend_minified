from django.db import models
import uuid
from django.utils.text import slugify

# Create your models here.

class Category(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.category_name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.category_name



def get_product_image_upload_path(instance, filename):
    slug = slugify(instance.title)

    # return f"products/images/{slug}/{filename}"
    return '/'.join(['thumb', slug, filename])


def get_product_gallery_upload_path(instance, filename):
    slug = slugify(instance.title)

    # return f"products/images/{slug}/{filename}"
    return '/'.join(['large', slug, filename])

class Project(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, null=True, blank=True, max_length=100)
    thumbPoster = models.ImageField(upload_to=get_product_image_upload_path, default="")
    projectPreviewVideo = models.FileField(upload_to=get_product_image_upload_path, null=True, blank=True, default="")
    project_type = models.CharField(max_length=255)
    project_about = models.CharField(max_length=255, null=True, blank=True)
    date = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    tools = models.CharField(max_length=255)
    websiteName = models.CharField(max_length=255)
    websiteLink = models.CharField(max_length=255, null=True, blank=True)
    gitRepoName = models.CharField(max_length=255, null=True, blank=True)
    gitRepoLink = models.CharField(max_length=255, null=True, blank=True)
    client = models.CharField(max_length=255, null=True, blank=True)
    desciption = models.TextField()
    category = models.ManyToManyField(Category, related_name="projects_categories", blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class ProjectImage(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="project_images")
    image = models.ImageField(upload_to=get_product_gallery_upload_path)

    @property
    def title(self):
        return self.project.title
    

    def __str__(self):
        return self.image


def get_my_doc_upload_path(instance, filename):

    # return f"products/images/{slug}/{filename}"
    return '/'.join(['docs', filename])



class AboutMe(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    resume = models.FileField(upload_to=get_my_doc_upload_path, null=True, blank=True, default="")
    readme = models.TextField()
    currentStatus = models.CharField(max_length=255)
    codingAchievement = models.CharField(max_length=255)
    myImage = models.ImageField(upload_to=get_my_doc_upload_path, default="")


class Skill(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    skill_name = models.CharField(max_length=255)
    skill_level = models.IntegerField()
    skill_description = models.TextField()
    skill_icon = models.CharField(max_length=255)
    skill_border_color = models.CharField(max_length=255, null=True, blank=True)
    skill_background_color = models.CharField(max_length=255, null=True, blank=True)
    skill_background_image = models.CharField(max_length=255, null=True, blank=True)