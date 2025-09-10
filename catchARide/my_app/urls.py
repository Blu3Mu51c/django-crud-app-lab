from django.urls import path
from . import views

urlpatterns = [
    # Home & About
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),

    path('accounts/signup/', views.signup, name='signup'),

    # Cars
    path('cars/', views.car_index, name='car-index'),
    path('cars/create/', views.CarCreate.as_view(), name='car-create'),
    path('cars/<int:car_id>/', views.car_detail, name='car-detail'),
    path('cars/<int:pk>/update/', views.CarUpdate.as_view(), name='car-update'),
    path('cars/<int:pk>/delete/', views.CarDelete.as_view(), name='car-delete'),

    # Add service record to a car
    path('cars/<int:car_id>/add-service/', views.add_service, name='add-service'),

    # Accessories (like toys for cats)
     path('accessories/', views.AccessoryList.as_view(), name='accessory-index'),
    path('accessories/create/', views.AccessoryCreate.as_view(), name='accessory-create'),
    path('accessories/<int:pk>/', views.AccessoryDetail.as_view(), name='accessory-detail'),
    path('accessories/<int:pk>/update/', views.AccessoryUpdate.as_view(), name='accessory-update'),
    path('accessories/<int:pk>/delete/', views.AccessoryDelete.as_view(), name='accessory-delete'),

    # Associate / remove accessories from cars
    path('cars/<int:car_id>/assoc-accessory/<int:accessory_id>/', views.assoc_accessory, name='assoc-accessory'),
    path('cars/<int:car_id>/unassoc-accessory/<int:accessory_id>/', views.unassoc_accessory, name='unassoc-accessory'),
]
