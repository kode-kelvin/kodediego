from django.db import models
import uuid

# Create your models here.
class Project(models.Model):

    WORKTYPE = (
        ('software dev', 'Software Dev'),
        ('product design', 'Product Design'),
        ('random', 'Random')
    )
    title = models.CharField(max_length=500)
    description = models.TextField(null=False, blank=False)
    tags = models.ManyToManyField('Tag', blank=True)
    product = models.TextField(null=True, blank=False)
    role = models.TextField(null=True, blank=False)
    pdf = models.FileField(upload_to='media/pdf', null=True, blank=True)
    cover = models.ImageField(upload_to='media/covers', null=False, blank=False)
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    source_code = models.CharField(max_length=2000, null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    worktype = models.CharField(max_length=50, null=True, blank=True, choices=WORKTYPE)


    def __str__(self):
        return self.title


# tags
class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False, primary_key=True)

    def __str__(self):
        return self.name
