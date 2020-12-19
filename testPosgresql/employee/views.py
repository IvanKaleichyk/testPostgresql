from idlelib.textview import view_file

from rest_framework import generics, viewsets

from .serializers import *
from .models import *


class EmployeesViewSets(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all().order_by('name')
