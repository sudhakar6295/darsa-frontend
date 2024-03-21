import scrapy,json
import requests
import os

class DarsaSpider(scrapy.Spider):
    name = "darsa"
    
    start_urls = ["https://www.darsa.cl/"]

    headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,ta;q=0.6',
            'Connection': 'keep-alive',
            'Origin': 'https://www.darsa.cl',
            'Referer': 'https://www.darsa.cl/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'cross-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            }
    
    def save_image(self, url,folder="Image"):
        abs_url = f"https://www.darsa.cl/images/original/{url}"
        if not os.path.exists(folder):
                    os.makedirs(folder)
        filepath = os.path.join(folder,url)
        response = requests.get(abs_url)
        if response.status_code == 200:
            with open(filepath, 'wb') as f:
                f.write(response.content)
                print(f"Image saved as {filepath}")
        else:
            print(f"Failed to download image from {filepath}")

    def parse(self, response):

        valid_items = ['id', 'id_erp', 'idMarca', 'seller_id', 'sku', 'nombreProducto', 'modelo', 'dimension', 'peso', 'peso_volumetrico', 'ancho', 'largo', 'alto', 'apilable', 'maxApilable', 'propAncho', 'propAlto', 'propLargo', 'ruta', 'pack', 'variantesAgrupadas', 'packPadre', 'margen', 'stock', 'idMedida', 'precio', 'precioReferencia', 'img', 'youtube', 'video', 'descripcion', 'descripcionCorta', 'despacho', 'retiroTienda', 'descuento', 'mostrarHome', 'probador', 'destacado', 'complemento', 'precioComplemento', 'fichaTecnica', 'nombreFicha', 'orientacion', 'delivery', 'idProveedor', 'idioma', 'tag', 'meta_title', 'meta_description', 'actionStore', 'currencyBasePrice', 'saleDecimal', 'criticalStock', 'idCategoria', 'tipoVenta', 'cantidadLote', 'precioUnitario', 'rechazoProducto', 'publicado', 'created_at', 'updated_at', 'deleted_at', 'published_at', 'centry_id', 'cat_id', 'cat_nombre', 'cat_alias', 'cat_ruta', 'cat_img', 'cat_banner', 'marca']
        
        categorys = ['retail','industrial']

        url = "https://darsa.samurai.cl/getProductosCategoria/"

        for category in categorys:
            page_no =1
            while True:
                payload = {'slug': category,
                        'filterByAttribute': '',
                        'filterByPrice': '',
                        'isPaginated': 'true',
                        'page': str(page_no)}
                
                data = requests.request("POST", url, headers=self.headers, data=payload)
                json_data = data.json()
                row_datas = json_data.get('data')

                for row_data in row_datas:
                    output_data = {}
                    for valid_item in valid_items:
                        output_data[valid_item] = row_data.get(valid_item)
                    self.save_image(output_data.get('img'))
                    yield output_data

                next_page_url = json_data.get('next_page_url')

                if next_page_url:
                    page_no = page_no + 1
                else:
                    break
                

                






        
