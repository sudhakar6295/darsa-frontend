from django.http import JsonResponse
from django.db import connection

def read_data():
    with connection.cursor() as cursor:
        cursor.execute("SELECT nombreProducto,ruta,precio,sku,img FROM Products")
        columns = [col[0] for col in cursor.description]
        data = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return data
    
def read_products_data(ruta):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM Products WHERE ruta = %s", [ruta])
        columns = [col[0] for col in cursor.description]
        data = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return data