from django.db import models
import uuid


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title


class Review(models.Model):
    # owner
    JOB_INFO = (
        ('inp', 'In progress'),
        ('done', 'Already done'),
    )
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    value = models.CharField(max_length=200, choices=JOB_INFO)
    body = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.value
