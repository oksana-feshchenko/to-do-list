from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()
    completed = models.BooleanField()
    tags = models.ManyToManyField(to=Tag, related_name="tasks")

    class Meta:
        ordering = ["completed", "created_at"]

    def __str__(self):
        return f"{self.content} should be done to {self.deadline}"






