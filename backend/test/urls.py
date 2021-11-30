from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from test import views
from rest_framework.urlpatterns import format_suffix_patterns

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'test', views.TestViewSet)
#router.register(r'Token/', views.TokenViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('Token/', views.TokenList.as_view()),
    path('Token/<int:pk>/', views.TokenDetail.as_view()),
]
#urlpatterns = format_suffix_patterns(urlpatterns)
