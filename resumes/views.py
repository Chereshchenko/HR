from rest_framework import viewsets
from .models import Resume
from .serializers import ResumeSerializer
from .permissions import ResumePermission
from rest_framework.permissions import IsAuthenticated

class ResumeViewSet(viewsets.ModelViewSet):
    serializer_class = ResumeSerializer
    permission_classes = [IsAuthenticated, ResumePermission]
    
    def get_queryset(self):
        user = self.request.user
        if user.role == 'ADMIN':
            return Resume.objects.all()
        elif user.role == 'HR':
            return Resume.objects.all()
        else:
            return Resume.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
