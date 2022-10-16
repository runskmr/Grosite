from django.http import HttpResponse

from .forms import OrderItemForm
from .models import Type, Item
from django.shortcuts import get_object_or_404, redirect, render
from django.shortcuts import render

# Create your views here.
def index(request):
    type_list = Type.objects.all().order_by('id')[:7]
    return render(request, 'myapp1/index0.html', {'type_list': type_list})


# def index(request):
#     type_list = Type.objects.all().order_by('id')[:7]
#     product = Type.objects.all().order_by('name')
#     response = HttpResponse()
#     heading1 = '<p>' + 'Different Types: ' + '</p>'
#     response.write(heading1)
#     for type in type_list:
#         para = '<p>' + str(type.id) + ': ' + str(type) + '</p>'
#         response.write(para)
#
#     heading2 = '<p>' + 'First 7 expensive items:' + '</p>'
#     response.write(heading2)
#     first_7_items = Item.objects.order_by(
#         '-price').values_list('name', 'price')[:7]
#
#     for item in first_7_items:
#         para = '<p>' + 'Item Name: ' + \
#             str(item[0])+',' + 'price: '+str(item[1])+'</p>'
#         response.write(para)
#     return response


def about(request):
    return render(request, 'myapp1/about0.html', {})


def products(request):
    prodlist = Type.objects.all().order_by('id')
    return render(request, 'myapp/products.html', content_type='application/html')


def hmeRedirect(request):
    return redirect("http://127.0.0.1:8000/")

def detail(request, type_no):
    items = Item.objects.filter(type=type_no)
    type = get_object_or_404(Type, id=type_no)
    response = HttpResponse()
    #if items:
    return render(request, 'myapp1/detail0.html', {'items': items})
   # else:
   #     response.write('There are no items in the type ' + str(type))

    #return response

def items(request):
    itemlist = Item.objects.all().order_by('id')[:20]
    return render(request, 'myapp1/items.html', {'itemlist': itemlist})


def placeorder(request):
            msg = ''
            itemlist = Item.objects.all()
            if request.method == 'POST':
                form = OrderItemForm(request.POST)
                if form.is_valid():
                    order = form.save(commit=False)
                    if order.items_ordered <= order.item.stock:
                            order.save()
                            msg = 'Your order has been placed successfully.'
                    else:
                            msg = 'We do not have sufficient stock to fill your order.'
                            return render(request, 'myapp1/order_response.html', {'msg': msg})
            else:
                    form = OrderItemForm()
            return render(request, 'myapp1/placeorder.html', {'form': form, 'msg': msg, 'itemlist':
            itemlist})