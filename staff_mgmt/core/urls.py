from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DepartmentViewSet, StaffViewSet, AttendanceViewSet

router = DefaultRouter()
router.register(r'departments', DepartmentViewSet)
router.register(r'staff', StaffViewSet)
router.register(r'attendance', AttendanceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
