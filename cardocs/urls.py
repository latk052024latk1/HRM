from django.urls import path, include
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'cardocs'
urlpatterns = [
    path('cars/', views.CarList.as_view(), name='car_list'),
    path('cars/<int:pk>', views.car_view, name='car_view'),
    path('cars/new', views.car_create, name='car_new'),
    path('cars/docs/new', views.docs_create, name='docs_new'),
    path(r'cars/docs/<int:car_id>/<str:car_doc_category>/update', views.docs_update, name='docs_upd'),

    path('cars/docs/<int:pk>/file', views.pdf_view_car, name='car_doc_pdf'),

    path('trailers/', views.TrailerList.as_view(), name='trailer_list'),
    path('trailers/<int:pk>', views.trailer_view, name='trailer_view'),
    path('trailers/new', views.trailer_create, name='trailer_new'),
    path('trailers/docs/new', views.trailer_docs_create, name='trailer_docs_new'),
    path(r'trailers/docs/<int:trailer_id>/<str:trailer_doc_category>/update', views.trailer_docs_update, name='trailer_docs_upd'),

    path('trailers/docs/<int:pk>/file', views.pdf_view_trailer, name='trailer_doc_pdf'),

]