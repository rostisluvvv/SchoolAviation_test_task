from django.urls import include, path
from rest_framework import routers


from .views import EdcModuleViewSet


router = routers.DefaultRouter()

router.register('module', EdcModuleViewSet, basename='module')


urlpatterns = [
    path('v1/', include(router.urls)),
]
