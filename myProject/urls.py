from django.urls import path
from . import views

urlpatterns = (
    path('', views.index, name='index'),
    path('add/', views.add, name='addData'),
    path('show/', views.show, name='show'),
    path('showEvent', views.showEvent, name='showEvent'),
    path('showvenue', views.showVenue, name='showvenue'),
    path('AddEvent', views.AddEvents, name='AddEvent'),
    path('AddVenue', views.addVenue, name='AddVenue'),
    path('ShowAllEvent', views.catalog, name='ShowAllEvent'),
    path('ShowAll', views.event_venue, name='ShowAll'),
    path('<int:id>/', views.add, name='p_update'),
    path('delete/<int:id>/', views.delete, name='p_delete'),
    path('update/<int:id>/', views.AddEvents, name='e_update'),
    path('deleteevent/<int:id>/', views.deleteevent, name='e_delete'),
    path('ShowVenue/', views.showVenue, name='value'),
)
