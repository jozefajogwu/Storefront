from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product

# Create your views here.
def say_hello(request):
    query_set  = Product.objects.all()
    
    for Product in query_set:
       print(Product)
       
       list(Product)
       return render(request, 'hello.html', {'name': 'JozefAjogwu'})
