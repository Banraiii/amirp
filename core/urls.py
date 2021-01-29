from django.urls import path

from . import views

urlpatterns = [
    path('', views.ServiceView.as_view()),
    path('servicese', views.ServiceViewNum2.as_view()),
    path('transport/communication', views.servicesendmail, name='index'),
    path('servicese/communication', views.serviceSendmailtwo),
    path('transport', views.TransportationListView.as_view()),
    path('avtobuses/<slug:slug>', views.AvtoParkDitail.as_view(), name='auto_park'),
    path("abouts/", views.FlatPage1.as_view()),
    path("landing_page/", views.FlatPage2.as_view()),
    path("broner/", views.FlatPage3.as_view()),
    path("search/", views.Search.as_view(), name='search'),
    path("<slug:slug>", views.ServiceDetailView.as_view(), name='services_detail'),
    path("transport/<slug:slug>", views.TransportationDetailView.as_view(), name='transport_detail'),
]

