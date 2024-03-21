from django.shortcuts import render
from darsa.const.dataSource import read_data,read_products_data
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import redirect

def index(request):
    return render(request,'index.html')

def products(request, ruta):
        products = read_products_data(ruta)
        if products:
             product = products[0]
        else:
            return redirect('home')
        return render(request, 'products.html', {'product': product})

         
def home(request, page):
    items = read_data()
    page = request.GET.get('page', 1)
    paginator = Paginator(items, 20)
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)

    return render(request, 'home.html', {'items': items, 'page': items})

def search(request):
    query = request.GET.get('query')
    items = read_data()
    items = [item for item in items if query.lower() in item['nombreProducto'].lower()]
    return render(request, 'home.html', {'items': items, 'page': items})






    


    

