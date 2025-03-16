from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('random', views.random_sort, name='random_sort'),
    path('solve', views.solve_sort, name='solve_sort'),
    path('history', views.history, name='history')
]
