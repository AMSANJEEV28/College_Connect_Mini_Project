import uuid
from django.db import models
from user.models import CustomUser

def generate_unique_group_id():
    return uuid.uuid4().hex[:10]

class Group(models.Model):
    name = models.CharField(max_length=255, unique=True)
    group_id = models.CharField(max_length=10, unique=True, default=generate_unique_group_id)
    description = models.TextField()
    members = models.ManyToManyField(CustomUser, related_name='group_members', blank=True)
    creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='group_creator')

    def __str__(self):
        return self.name
