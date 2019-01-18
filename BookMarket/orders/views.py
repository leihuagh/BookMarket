from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from .models import Orders
from .forms import OrderForm, UpdateOrderForm
from django.urls import reverse_lazy
from reference.models import OrderStatus
from django.contrib.auth.mixins import PermissionRequiredMixin

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


class ListOrderView(PermissionRequiredMixin, ListView):
    model = Orders
    template_name = 'orders/order-list.html'
    paginate_by = 5

    permission_required = 'orders.view_order'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active'] = 'list_order'
        return context


class DetailOrderView(PermissionRequiredMixin, DetailView):
    model = Orders
    template_name = 'orders/order-view.html'

    permission_required = 'orders.view_order'

    def get_object(self, queryset=None):
        order_status = OrderStatus.objects.get(name='Принят')
        order_id = self.kwargs.get('pk')
        Orders.objects.filter(pk=order_id).update(status=order_status)
        order = Orders.objects.get(pk=order_id)
        return order


class UpdateOrderView(PermissionRequiredMixin, UpdateView):
    model = Orders
    template_name = 'orders/order-update.html'
    form_class = UpdateOrderForm

    permission_required = 'orders.change_order'

    def get_success_url(self):
        return reverse_lazy('orders:detail-orders', kwargs={'pk': self.object.pk})


class DeleteOrderView(PermissionRequiredMixin, DeleteView):
    model = Orders
    template_name = 'orders/order-delete.html'
    success_url = reverse_lazy('orders:list-orders')

    permission_required = 'orders.delete_order'
