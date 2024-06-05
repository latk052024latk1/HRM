from django.urls import path, include
from . import views
app_name = 'driverdocs'
urlpatterns = [
    path('drivers/', views.DriverList.as_view(), name='dr_list'),
    path('drivers/<int:pk>', views.driver_view, name='dr_view'),
    path('drivers/new', views.driver_create, name='dr_new'),
    path(r'drivers/docs/<int:person_id>/<str:doc_category>/update', views.docs_update, name='docs_upd'),
    path('drivers/docs/new', views.docs_create, name='docs_new'),
    path('drivers/docs/<int:pk>/file', views.pdf_view, name='doc_pdf'),
]