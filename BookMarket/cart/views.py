from django.shortcuts import render
from django.views.generic import UpdateView, TemplateView, DeleteView
from .forms import AddToCartForm
from .models import ProductsInCart, Cart
from products.models import Book
from django.urls import reverse_lazy

# Create your views here.


class AddProductCartView(UpdateView):
    template_name = 'cart/add_to_cart.html'
    form_class = AddToCartForm
    model = ProductsInCart
    success_url = reverse_lazy('cart:cart')

    def get_object(self):
        cart_id = self.request.session.get('cart_id')
        cart, cart_created = Cart.objects.get_or_create(
            pk=cart_id,
        )
        if cart_created:
            self.request.session['cart_id'] = cart.pk

        book_id = self.kwargs.get('product')
        book = Book.objects.get(pk=book_id)

        obj, created = self.model.objects.get_or_create(
            cart=cart,
            book=book,
            defaults={
                'cart': cart,
                'book': book,
                'quantity': 1
            }
        )
        return obj


class ListCartView(TemplateView):
    template_name = 'cart/cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        cart_id = self.request.session.get('cart_id')
        cart, cart_created = Cart.objects.get_or_create(
            pk=cart_id,
        )
        if cart_created:
            self.request.session['cart_id'] = cart.pk
        prod_in_cart = ProductsInCart.objects.filter(cart__pk=cart_id)

        context['prod_in_cart'] = prod_in_cart

        return context


class UpdateProductCartView(UpdateView):
    template_name = 'cart/add_to_cart.html'
    form_class = AddToCartForm
    model = ProductsInCart
    success_url = reverse_lazy('cart:cart')


class DeleteProductCartView(DeleteView):
    form_class = AddToCartForm
    template_name = 'cart/delete_from_cart.html'
    success_url = reverse_lazy('cart:cart')
    model = ProductsInCart
