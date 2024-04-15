from django.http import JsonResponse
from django.db import connection

def read_data(category):
    with connection.cursor() as cursor:
        cursor.execute("SELECT nombreProducto,ruta,precio,sku,img FROM Products where category = %s", [category])
        columns = [col[0] for col in cursor.description]
        data = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return data

def read_data_full():
    with connection.cursor() as cursor:
        cursor.execute("SELECT nombreProducto,ruta,precio,sku,img FROM Products ")
        columns = [col[0] for col in cursor.description]
        data = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return data
    
def read_products_data(ruta):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM Products WHERE ruta = %s", [ruta])
        columns = [col[0] for col in cursor.description]
        data = [dict(zip(columns, row)) for row in cursor.fetchall()]

    if data:
        product_data = data[0]
        product_id = data[0].get('id')
        additional_images = []
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM Images WHERE id = %s", [product_id])
            columns = [col[0] for col in cursor.description]
            images = [dict(zip(columns, row)) for row in cursor.fetchall()]
            for image_dict in images:
                additional_images.append(image_dict.get('image'))
            product_data['additional_images'] ={}
            product_data['additional_images'] = additional_images

        return product_data
    else:
        return None
    
def read_categories():
    with connection.cursor() as cursor:
        cursor.execute("SELECT distinct category  FROM Products")
        categories = [col[0] for col in cursor.fetchall()]
        categories = [x for x in categories if x is not None]
        return categories