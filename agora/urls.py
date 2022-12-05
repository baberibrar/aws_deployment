from .views import AdvocatesViewSets, CompaniesViewSets
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()
router.register('advocates', AdvocatesViewSets)
router.register('companies', CompaniesViewSets)

urlpatterns = [
    path('', include(router.urls))
]
