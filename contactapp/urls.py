from django.urls import path
from . import views

urlpatterns = [
    path('', views.ContatList.as_view()),
    path('contact/<int:id>/create/', views.ContactDetailView.as_view()),
]
