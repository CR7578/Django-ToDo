from django.urls import path
from . import views

urlpatterns = [
    path('addTask/',views.addTask,name='addTask'),
    path('delete/<int:pk>',views.delete,name='delete'),
    path('editTask/<int:pk>',views.editTask,name='editTask'),
    path('taskDone/<int:pk>/',views.taskDone,name='taskDone'),
    path('taskNotdone/<int:pk>/',views.taskNotdone,name='taskNotdone'),
]
