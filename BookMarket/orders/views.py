from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from .models import Orders
from .forms import OrderForm, UpdateOrderForm
from django.urls import reverse_lazy
from reference.models import OrderStatus

# Create your views here.


class CreateOrderView(CreateView):
    template_name = 'cart/view_cart.html'
    model = Orders
    form_class = OrderForm

    def get_success_url(self):
        del self.request.session['cart_id']
        return reverse_lazy('orders:success', kwargs={'pk': self.object.pk})


class SuccessOrderView(DetailView):
    model = Orders
    template_name = 'orders/order-success.html'


class ListOrderView(ListView):
    model = Orders
    template_name = 'orders/order-list.html'


class DetailOrderView(DetailView):
    model = Orders
    template_name = 'orders/order-view.html'

    def get_object(self, queryset=None):
        order_status = OrderStatus.objects.get(name='Принят')
        order_id = self.kwargs.get('pk')
        Orders.objects.filter(pk=order_id).update(status=order_status)
        order = Orders.objects.get(pk=order_id)
        return order


class UpdateOrderView(UpdateView):
    model = Orders
    template_name = 'orders/order-update.html'
    form_class = UpdateOrderForm

    def get_success_url(self):
        return reverse_lazy('orders:detail-orders', kwargs={'pk': self.object.pk})


class DeleteOrderView(DeleteView):
    model = Orders
    template_name = 'orders/order-delete.html'
    success_url = reverse_lazy('orders:list-orders')