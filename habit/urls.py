from django.urls import path
from habit.apps import HabitConfig
from habit.views.habit import *

app_name = HabitConfig.name

urlpatterns = [
    path('', HabitListView.as_view(), name='habit_list'),
    path('create/', HabitCreateView.as_view(), name='habit_create'),
    path('<int:pk>/', HabitRetrieveView.as_view(), name='habit_ditail'),
    path('update/<int:pk>/', HabitUpdateView.as_view(), name='habit_update'),
    path('delete/<int:pk>/', HabitDestroyView.as_view(), name='habit_delete'),
]
