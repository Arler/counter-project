from django.urls import path
from .views import counter_view


urlpatterns = [
	path('', counter_view)
]