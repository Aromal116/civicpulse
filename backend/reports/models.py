from django.db import models

class Report(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    image = models.ImageField(upload_to='reports/', null=True, blank=True)

    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)

    issue_type = models.CharField(max_length=100, null=True, blank=True)
    severity = models.IntegerField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

    status = models.CharField(max_length=50, default="Pending")