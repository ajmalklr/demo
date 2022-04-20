
from django.urls import path
from . import views

urlpatterns = [
   path('',views.home,name='home'),
   # path('details',views.details,name='details')
   path('delete/<int:taskid>/',views.delete,name='delete'),
   path('update/<int:id>/',views.update,name='update'),
   path('cbvhome/',views.TaskListView.as_view(),name='cbvhome'),
   path('cbvdetails/<int:pk>/',views.TaskDetailView.as_view(),name='cbvdetails'),
   path('cbvedit/<int:pk>/',views.TaskUpdateView.as_view(),name='cbvedit'),
   path('cbvdelete/<int:pk>/',views.TaskDeleteView.as_view(),name='cbvdelete')
]
