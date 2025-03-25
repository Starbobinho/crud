from django.urls import path
from .views import CrudAPI

urlpatterns = [
    path('', CrudAPI.as_view()),
    path('create/', CrudAPI.as_view()),
    path('update/<int:id>/', CrudAPI.as_view()),
    path('delete/<int:id>/', CrudAPI.as_view()),
]
