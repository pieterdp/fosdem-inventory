from django.urls import path

from . import views

urlpatterns = [
    path('boxes/', views.IndexView.as_view(), name='index'),
    path('boxes/<int:pk>/', views.DetailView.as_view(), name='detail')
]
