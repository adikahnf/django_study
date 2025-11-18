from django.urls import path
from . import views

# Create a path
urlpatterns = [
    path('function', views.MyViews),
    path('class', views.MyViewsClass.as_view())
]
