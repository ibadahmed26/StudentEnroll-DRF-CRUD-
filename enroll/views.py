from .models import StudentModel, TeacherModel
from .serializer import StudentSerializer,TeacherSerializer
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser

class StudentViewsetprivate(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializer

class StudentViewsetpublic(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [AllowAny]
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializer

class TeacherViewsetprivate(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser]
    queryset = TeacherModel.objects.all()
    serializer_class = TeacherSerializer

class TeacherViewsetpublic(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [AllowAny]
    queryset = TeacherModel.objects.all()
    serializer_class = TeacherSerializer