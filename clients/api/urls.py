from django.urls import path
from clients.api import views

urlpatterns = [
    path("client",views.clients),                       #display all clients
    path("client/create",views.createclient),           #create client
    path("client/update/<int:id>",views.updateclient),  #update spesific client
    path("client/<int:id>",views.getclient),            #display spesific client
    path("client/delete/<int:id>",views.deleteclient),  #delete spesific client
]
