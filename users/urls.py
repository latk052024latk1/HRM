from django.urls import path
from . import views
app_name = "users"
urlpatterns = [


    path('login/', views.login_user, name='login_u'),
    path('<int:pk>', views.user_view, name='u_view'),
    path('logout_u', views.user_logout, name='logout_u'),
    path('change', views.user_change, name='change'),
    path('signup', views.user_create, name='create'),
    path('', views.UserList.as_view(), name='u_list')
]