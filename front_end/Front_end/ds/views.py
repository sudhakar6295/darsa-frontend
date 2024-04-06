from django.shortcuts import render
from ds.const.dataSource import read_data,read_products_data,read_categories
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import redirect

def index(request):
    categories = read_categories()
    return render(request,'home_page.html', {'categories': categories})

def products(request, ruta):
        products = read_products_data(ruta)
        if products:
             return render(request, 'products.html', {'product': products})
        else:
            return redirect('home')
        

         
def home(request, page ,category=None):
    items = read_data(category)
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
    filtered_items = []
    
    if query:
        for item in items:
            if query.lower() in item['nombreProducto'].lower() or query.lower() == item['sku'].lower():
                filtered_items.append(item)
    else:
        filtered_items = items
    
    return render(request, 'home.html', {'items': filtered_items, 'page': filtered_items})






    


    

