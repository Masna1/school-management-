from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Student, LibraryHistory, FeesHistory
from .serializers import StudentSerializer, LibraryHistorySerializer, FeesHistorySerializer

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and (
            getattr(request.user, 'role', None) == 'admin' or 
            request.method in permissions.SAFE_METHODS
        )

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAdminOrReadOnly]

class LibraryHistoryViewSet(viewsets.ModelViewSet):
    queryset = LibraryHistory.objects.all()
    serializer_class = LibraryHistorySerializer

    def get_permissions(self):
        if getattr(self.request.user, 'role', None) == 'librarian':
            return [permissions.IsAuthenticated()]
        return [permissions.IsAdminUser()]

class FeesHistoryViewSet(viewsets.ModelViewSet):
    queryset = FeesHistory.objects.all()
    serializer_class = FeesHistorySerializer
    permission_classes = [permissions.IsAuthenticated]

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and getattr(request.user, 'role', None) == 'admin'

class IsLibrarian(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and getattr(request.user, 'role', None) == 'librarian'

from django.shortcuts import render
from .models import Student

def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

def office_dashboard(request):
    return render(request, 'office_dashboard.html')

def librarian_dashboard(request):
    return render(request, 'librarian_dashboard.html')

def student_details(request):
    students = Student.objects.all()
    return render(request, 'student_details.html', {'students': students})
