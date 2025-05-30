from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DepartmentViewSet, PositionViewSet, EmployeeViewSet

router = DefaultRouter()
router.register('departments', DepartmentViewSet)
router.register('positions', PositionViewSet)
router.register('employees', EmployeeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
