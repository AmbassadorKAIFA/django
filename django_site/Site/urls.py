from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import (CreateTableDataView, ListTablesView, TableListView1, TableBookingView, MyPage, UserRegisterView, UserLoginView, UserLogoutView)


urlpatterns = [
    path('', TableListView1.as_view(), name = 'index'),
    path('create_table', CreateTableDataView.as_view(), name = 'create_table'),
    path('list_tables', ListTablesView.as_view(), name = 'list_tables'),
    path('', MyPage.as_view(), name='table_view'),
    path('booking_table/<int:pk>/', TableBookingView.as_view(), name='booking_table'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
]
