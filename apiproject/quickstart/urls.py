from django.urls import path
from .views import list_appDetails, create_appDetails, list_userDetails

urlpatterns = [
	path('app', list_appDetails, name='list_appDetails'),
    path('new', create_appDetails, name='create_appDetails'),
    path('user/<str:idss>', list_userDetails, name='list_userDetails'),

]