from django.views.generic import DetailView, FormView
from .models import Prf
from django.contrib.auth.models import User
from django.urls import reverse
from .forms import PrflUpdateForm
from cart.models import Cart
from products.models import Book
from django.contrib.auth.mixins import LoginRequiredMixin


class PrflDetailView(LoginRequiredMixin, DetailView):
    login_url = '/accounts/login/'
    template_name = 'prfls/prfls_view.html'
    model = User

    def get_context_data(self, **kwargs):
        context = super(PrflDetailView, self).get_context_data(**kwargs)

        user = User.objects.get(id=self.kwargs['pk'])
        if self.request.user.pk == user.pk:

            user_order = {}
            quantity_product_in_order = []
            for order in Cart.objects.filter(user_id=user.pk):
                books = Book.objects.filter(product_in_cart__cart=order)
                my_dic = {order: books}
                user_order.update(my_dic)
            context['user_order'] = user_order
            context['quantity_product_in_order'] = quantity_product_in_order
            return context


class PrflUpdateView(LoginRequiredMixin, FormView):
    login_url = '/accounts/login/'
    template_name = 'prfls/prfls_update.html'
    model = User

    def get_success_url(self):
        return reverse('prfls:prfls-view', args=(self.kwargs['pk'],))

    def get_context_data(self, **kwargs):
        context = super(PrflUpdateView, self).get_context_data(**kwargs)
        user = User.objects.get(id=self.kwargs['pk'])
        permission = False
        if self.request.user.pk == user.pk:
            permission = True
        context['permission'] = permission
        return context

    def get_form(self, form_class=None):
        user = User.objects.get(id=self.kwargs['pk'])
        if self.request.user.pk == user.pk:
            del_addr, created = Prf.objects.get_or_create(
                customer=user,
            )
            if self.request.method == 'GET':
                my_form = PrflUpdateForm(
                    initial={'delivery_address': user.prf.delivery_address,
                             'username': user.username,
                             'first_name': user.first_name,
                             'last_name': user.last_name,
                             'email': user.email,
                             'phone_number': user.prf.phone_number
                             }
                )

                return my_form
            else:
                my_form = PrflUpdateForm(self.request.POST)
                user.username = my_form['username'].value()
                user.first_name = my_form['first_name'].value()
                user.last_name = my_form['last_name'].value()
                user.email = my_form['email'].value()
                us_addr = Prf.objects.get(customer_id=user.id)
                us_addr.delivery_address = my_form['delivery_address'].value()
                us_addr.phone_number = my_form['phone_number'].value()
                us_addr.save()
                user.save()
                return my_form
