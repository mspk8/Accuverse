from django.urls import path
from . import views
urlpatterns = [
    
    path('manage',views.manage,name="manage-clients"),
    path('manage/add',views.client_add,name="add-clients"),
    path('main',views.clients_main,name="dashboard"),
    path('details/<int:pk>/', views.client_details, name='client-details'),

]
