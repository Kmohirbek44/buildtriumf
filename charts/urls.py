from django.urls import path

from .views import charts
app_name='charts'
urlpatterns = [
    path('', charts, name='charts'),
]