from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import (CreateTableDataView, ListTablesView, TableListView1, TableBookingView, MyPage)


urlpatterns = [
    path('', MyPage.as_view(), name = 'index'),
    path('create_table', CreateTableDataView.as_view(), name = 'create_table'),
    path('list_tables', ListTablesView.as_view(), name = 'list_tables'),
    path('', TableListView1.as_view(), name='index'),
    path(
        'booking_table/<int:pk>/',
        TableBookingView.as_view(),
        name='booking_table',
    ),
]