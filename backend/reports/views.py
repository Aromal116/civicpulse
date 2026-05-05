from rest_framework import viewsets
from .models import Report
from .serializers import ReportSerializer
from .ai_model import predict_issue

class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

    def perform_create(self, serializer):
        instance = serializer.save()

        if instance.image:
            issue, severity = predict_issue(
                instance.image.path, 
                instance.title,
                instance.description
            )
            instance.issue_type = issue
            instance.severity = severity
        else:
            instance.issue_type = "manual report"
            instance.severity = 1

        instance.save()