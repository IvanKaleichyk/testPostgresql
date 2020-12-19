from rest_framework import routers

from .views import EmployeesViewSets

router = routers.SimpleRouter()

router.register(r'employees', EmployeesViewSets)
router.register(r'', EmployeesViewSets)

urlpatterns = router.urls
