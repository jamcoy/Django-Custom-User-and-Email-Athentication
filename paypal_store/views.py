from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, get_object_or_404
from products.models import Product


@csrf_exempt
def paypal_return(request):
    invoice = request.POST.getlist('invoice')
    db_id = invoice[0][0]
    item = get_object_or_404(Product, pk=db_id)
    args = {'post': request.POST, 'get': request.GET, 'item': item}
    return render(request, 'paypal/paypal_return.html', args)


def paypal_cancel(request):
    args = {'post': request.POST, 'get': request.GET}
    return render(request, 'paypal/paypal_cancel.html', args)
