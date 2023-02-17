from django.db import models


# Create your models here.
class Article(models.Model):
    STATUS_CHOICES = (("new", "New"), ("in progress", "In Progress"), ("done", "Done"))

    title = models.CharField(max_length=200, null=False, blank=False, verbose_name="Title")
    text = models.TextField(max_length=3000, null=False, blank=False, verbose_name="Text")
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default="new", verbose_name="Status")
    deadline = models.DateField(null=True, verbose_name="Deadline")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creation date and time")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated date and time")

    def __str__(self):
        return f"{self.title} - {self.status}"
