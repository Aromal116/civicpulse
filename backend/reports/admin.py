from django.contrib import admin
from .models import Report

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ("title", "issue_type", "severity", "status", "created_at")
    list_filter = ("issue_type", "severity", "status")
    search_fields = ("title", "description")