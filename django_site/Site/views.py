from datetime import (date, datetime)

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (CreateView, ListView, UpdateView)

from .forms import (CreateTableDataForm, DateForm, DateInputTableForm, TableBookingForm)
from .models import Table


class MyPage(ListView):
    model = Table
    template_name = 'index.html'
    success_url = reverse_lazy('index')
    # def get(self, request):
    #     form = DateInputTableForm()
    #     return render(request, "index.html", {"form": form})
    #
    # def post(self, response):
    #     pass


class CreateTableDataView(CreateView):
    model = Table
    template_name = 'create_table_data.html'
    form_class = CreateTableDataForm
    success_url = reverse_lazy('index')


class ListTablesView(ListView):
    model = Table
    template_name = 'list_tables.html'
    success_url = reverse_lazy('index')

    def get_queryset(self):
        return self.model.objects.all()

class TableListView1(ListView):
    model = Table
    template_name = 'index.html'
    extra_context = {'date': DateInputTableForm}

    def get_queryset(self):
        if self.request.GET.get('date'):
            return self.model.objects.filter(
                date=self.request.GET['date'],
                booking=False
            )
        return self.model.objects.filter(booking=False)


class TableBookingView(UpdateView):
    model = Table
    template_name = 'booking_table.html'
    form_class = TableBookingForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        table = form.save(commit=False)
        table.booking = True
        return super().form_valid(form=form)