from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('category', views.CategoryViewSet, basename='category')

urlpatterns = [
    path('', include(router.urls)),
    path('category/<int:category_id>/', views.CategoryRetrieveUpdateDestroyAPIView.as_view()),
    path('category/<int:category_id>/item/', views.ItemListCreateAPIView.as_view()),
    path('category/<int:category_id>/item/<int:pk>/', views.ItemRetrieveUpdateDestroyAPIView.as_view()),
    path('category/<int:category_id>/item/<int:pk>/order/', views.OrderListCreateAPIView.as_view()),
    path('category/<int:category_id>/item/<int:pk>/order/<int:order_id>/', views.OrderRetrieveUpdateDestroyAPIView.as_view()),
]
