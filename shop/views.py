from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Product, ProductCategory, Contact, Cart
from django.db.models import Sum, Count
from django.template.loader import render_to_string
from math import ceil
from django.shortcuts import get_object_or_404
# Create your views here.


def index(request):
    # products = Product.objects.all()
    # print(products)
    # n = products.count()
    # nSlides = n//4 + ceil((n/4) - (n//4))
    # params = {'no_of_slides': nSlides, 'range': range(1, nSlides+1), 'products': products}
    # allProds = [[products, range(1, nSlides+1), nSlides], [products, range(1, nSlides+1), nSlides],
    #            [products, range(1, nSlides+1), nSlides]]
    cart = Cart.objects.all().aggregate(total_product=Sum('counter'))
    categories = ProductCategory.objects.all().prefetch_related('products', 'products__carts')
    cart_items = Cart.objects.all()
    params = {
        'categories': categories,
        'cart': cart,
        'cart_items': cart_items
    }
    return render(request, 'shop/index.html', params)


def add_in_cart(request):
    product_key = request.GET.get('a')  # request.GET['product_key']
    action = request.GET.get('b')  # request.GET['product_key']
    if product_key and action:
        product = Product.objects.filter(pk=product_key).first()
        if product:
            cart = Cart.objects.filter(product=product).first()
            if cart:
                if action == "add":
                    counter = cart.counter + 1
                    cart.counter = counter
                    cart.save()
                elif action == "remove":
                    counter = cart.counter - 1
                    if counter == 0:
                        cart.delete()
                        counter = 0
                    elif counter == -1:
                        counter = 0
                    else:
                        cart.counter = counter
                        cart.save()
                else:
                    counter = 0

            else:
                if action == 'add':
                    Cart.objects.create(product=product)
                counter = 1
            context = {
                'product': product,
            }
            html = render_to_string('shop/cart-exists.html', context=context, request=request)
            cart = Cart.objects.all().aggregate(total_product=Sum('counter'))
            cart_count = cart['total_product'] if cart['total_product'] else 0
            data = {
                'status': True,
                'count': cart_count,
                'html': html,
            }
            return JsonResponse(data)
        else:
            data = {
                'status': False,
                'message': 'Product id is invalid'
            }
            return JsonResponse(data)
    else:
        data = {
            'status': False,
            'message': 'product key not found.'
        }
        return JsonResponse(data)


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        mobile = request.POST.get('mobile', '')
        desc = request.POST.get('desc', '')
        print(name, email, mobile, desc)
        contact = Contact(name=name, email=email, mobile=mobile, desc=desc)
        contact.save()
    return render(request, 'shop/contact.html')


def popover(request):
    return render()

def tracker(request):
    return render(request, 'shop/tracker.html')


def search(request):
    return render(request, 'Shop/search.html')


def prodView(request, myid):
    product = Product.objects.get(id=myid)
    return render(request, 'Shop/prodView.html', {'product': product})


def checkout(request):
    return render(request, 'Shop/checkout.html')