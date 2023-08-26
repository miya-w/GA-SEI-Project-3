from django.urls import path, include
from . import views




	
urlpatterns = [
	path('', views.home, name='home'),
	path('about/', views.about, name='about'),
	path('properties/', views.properties_index, name='index'),
    path('properties/<int:property_id>/', views.properties_detail, name='detail'),
    path('properties/add/', views.PropertyAdd.as_view(), name='properties_add'),
    path('properties/<int:pk>/update/', views.PropertyUpdate.as_view(), name='properties_update'),
    path('properties/<int:pk>/delete/', views.PropertyDelete.as_view(), name='properties_delete'),
    path('properties/<int:property_id>/add_renting/', views.add_renting, name='add_renting'),
    
    path('cats/<int:property_id>/add_photo/', views.add_photo, name='add_photo'),
    
    path('properties/<int:property_id>/assoc_amenity/<int:amenity_id>/', views.assoc_amenity, name='assoc_amenity'),
    path('properties/<int:property_id>/unassoc_amenity/<int:amenity_id>/', views.unassoc_amenity, name='unassoc_amenity'),
    path('amenities/', views.AmenityList.as_view(), name='amenities_index'),
    path('amenities/<int:pk>/', views.AmenityDetail.as_view(), name='amenities_detail'),
    path('amenities/create/', views.AmenityCreate.as_view(), name='amenities_create'),
    path('amenities/<int:pk>/update/', views.AmenityUpdate.as_view(), name='amenities_update'),
    path('amenities/<int:pk>/delete/', views.AmenityDelete.as_view(), name='amenities_delete'),
    path('accounts/signup/', views.signup, name='signup'),
     
    
]