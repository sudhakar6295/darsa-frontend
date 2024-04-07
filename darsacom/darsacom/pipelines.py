# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import mysql.connector
import datetime
from mysql.connector import IntegrityError


class MySQLPipeline:
    
    def  __init__(self):
        self.create_connection()
        #self.create_table()

    def create_connection(self):
        self.conn=mysql.connector.connect(
            host='localhost',
            user='dsprodi',
            passwd='u30sicdu2SjR',
            database='dsprodi',
            

        )
        self.curr=self.conn.cursor()

    def create_table(self):
        
        self.curr.execute("""DROP TABLE IF EXISTS Products""") 

        self.curr.execute("""  CREATE TABLE `Products` (
                                `id` int NOT NULL,
                                `id_erp` int DEFAULT NULL,
                                `idMarca` int DEFAULT NULL,
                                `seller_id` int DEFAULT NULL,
                                `sku` varchar(255) DEFAULT NULL,
                                `nombreProducto` varchar(255) DEFAULT NULL,
                                `modelo` varchar(255) DEFAULT NULL,
                                `dimension` int DEFAULT NULL,
                                `peso` decimal(10,4) DEFAULT NULL,
                                `peso_volumetrico` decimal(10,4) DEFAULT NULL,
                                `ancho` decimal(10,2) DEFAULT NULL,
                                `largo` decimal(10,2) DEFAULT NULL,
                                `alto` decimal(10,2) DEFAULT NULL,
                                `apilable` int DEFAULT NULL,
                                `maxApilable` int DEFAULT NULL,
                                `propAncho` varchar(255) DEFAULT NULL,
                                `propAlto` varchar(255) DEFAULT NULL,
                                `propLargo` varchar(255) DEFAULT NULL,
                                `ruta` varchar(255) DEFAULT NULL,
                                `pack` int DEFAULT NULL,
                                `variantesAgrupadas` int DEFAULT NULL,
                                `packPadre` int DEFAULT NULL,
                                `margen` int DEFAULT NULL,
                                `stock` decimal(10,2) DEFAULT NULL,
                                `idMedida` int DEFAULT NULL,
                                `precio` int DEFAULT NULL,
                                `precioReferencia` int DEFAULT NULL,
                                `img` varchar(255) DEFAULT NULL,
                                `youtube` varchar(255) DEFAULT NULL,
                                `video` varchar(255) DEFAULT NULL,
                                `descripcion` text DEFAULT NULL,
                                `descripcionCorta` text DEFAULT NULL,
                                `despacho` int DEFAULT NULL,
                                `retiroTienda` int DEFAULT NULL,
                                `descuento` decimal(10,6) DEFAULT NULL,
                                `mostrarHome` int DEFAULT NULL,
                                `probador` int DEFAULT NULL,
                                `destacado` int DEFAULT NULL,
                                `complemento` int DEFAULT NULL,
                                `precioComplemento` int DEFAULT NULL,
                                `fichaTecnica` int DEFAULT NULL,
                                `nombreFicha` varchar(255) DEFAULT NULL,
                                `orientacion` int DEFAULT NULL,
                                `delivery` int DEFAULT NULL,
                                `idProveedor` int DEFAULT NULL,
                                `idioma` int DEFAULT NULL,
                                `tag` varchar(255) DEFAULT NULL,
                                `meta_title` varchar(255) DEFAULT NULL,
                                `meta_description` text DEFAULT NULL,
                                `actionStore` int DEFAULT NULL,
                                `currencyBasePrice` int DEFAULT NULL,
                                `saleDecimal` int DEFAULT NULL,
                                `criticalStock` int DEFAULT NULL,
                                `idCategoria` int DEFAULT NULL,
                                `tipoVenta` varchar(255) DEFAULT NULL,
                                `cantidadLote` int DEFAULT NULL,
                                `precioUnitario` int DEFAULT NULL,
                                `rechazoProducto` varchar(255) DEFAULT NULL,
                                `publicado` int DEFAULT NULL,
                                `created_at` datetime DEFAULT NULL,
                                `updated_at` datetime DEFAULT NULL,
                                `deleted_at` datetime DEFAULT NULL,
                                `published_at` datetime DEFAULT NULL,
                                `centry_id` int DEFAULT NULL,
                                `cat_id` int DEFAULT NULL,
                                `cat_nombre` varchar(255) DEFAULT NULL,
                                `cat_alias` varchar(255) DEFAULT NULL,
                                `cat_ruta` varchar(255) DEFAULT NULL,
                                `cat_img` varchar(255) DEFAULT NULL,
                                `cat_banner` varchar(255) DEFAULT NULL,
                                `marca` varchar(255) DEFAULT NULL
                                ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

                            """)
        
        self.curr.execute("""DROP TABLE IF EXISTS Images""") 

        self.curr.execute("""  CREATE TABLE `Images` (
                                `id` int NOT NULL,
                                `images` varchar(255) DEFAULT NULL
                                ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

                            """)




    def process_item(self, item, spider):
        
        self.store_db(item)
        
        return item

    def store_db(self,item):
            
            

            item_id = item.get('id')
            images = item.get('images')
            del item['images']

            sql_query = """
                    INSERT INTO Products (
                        id, id_erp, idMarca, seller_id, sku, nombreProducto, modelo, dimension, peso, peso_volumetrico,
                        ancho, largo, alto, apilable, maxApilable, propAncho, propAlto, propLargo, ruta, pack,
                        variantesAgrupadas, packPadre, margen, stock, idMedida, precio, precioReferencia, img,
                        youtube, video, descripcion, descripcionCorta, despacho, retiroTienda, descuento, mostrarHome,
                        probador, destacado, complemento, precioComplemento, fichaTecnica, nombreFicha, orientacion,
                        delivery, idProveedor, idioma, tag, meta_title, meta_description, actionStore, currencyBasePrice,
                        saleDecimal, criticalStock, idCategoria, tipoVenta, cantidadLote, precioUnitario, rechazoProducto,
                        publicado, created_at, updated_at, deleted_at, published_at, centry_id, cat_id, cat_nombre,
                        cat_alias, cat_ruta, cat_img, cat_banner, marca, category
                    )
                    VALUES (
                        %(id)s, %(id_erp)s, %(idMarca)s, %(seller_id)s, %(sku)s, %(nombreProducto)s, %(modelo)s, %(dimension)s, %(peso)s, %(peso_volumetrico)s,
                        %(ancho)s, %(largo)s, %(alto)s, %(apilable)s, %(maxApilable)s, %(propAncho)s, %(propAlto)s, %(propLargo)s, %(ruta)s, %(pack)s,
                        %(variantesAgrupadas)s, %(packPadre)s, %(margen)s, %(stock)s, %(idMedida)s, %(precio)s, %(precioReferencia)s, %(img)s,
                        %(youtube)s, %(video)s, %(descripcion)s, %(descripcionCorta)s, %(despacho)s, %(retiroTienda)s, %(descuento)s, %(mostrarHome)s,
                        %(probador)s, %(destacado)s, %(complemento)s, %(precioComplemento)s, %(fichaTecnica)s, %(nombreFicha)s, %(orientacion)s,
                        %(delivery)s, %(idProveedor)s, %(idioma)s, %(tag)s, %(meta_title)s, %(meta_description)s, %(actionStore)s, %(currencyBasePrice)s,
                        %(saleDecimal)s, %(criticalStock)s, %(idCategoria)s, %(tipoVenta)s, %(cantidadLote)s, %(precioUnitario)s, %(rechazoProducto)s,
                        %(publicado)s, %(created_at)s, %(updated_at)s, %(deleted_at)s, %(published_at)s, %(centry_id)s, %(cat_id)s, %(cat_nombre)s,
                        %(cat_alias)s, %(cat_ruta)s, %(cat_img)s, %(cat_banner)s, %(marca)s, %(category)s
                    )
                """
            
            # Extract item data and execute SQL query
            #params = (item['column1'], item['column2'], ...)
            

            try:
                self.curr.execute(sql_query, item)

                self.conn.commit()
            except IntegrityError:
                # IntegrityError occurred, handle it by updating the existing record
                update_query = """
                    UPDATE Products
                    SET id_erp = %(id_erp)s,
                        idMarca = %(idMarca)s,
                        seller_id = %(seller_id)s,
                        sku = %(sku)s,
                        nombreProducto = %(nombreProducto)s,
                        modelo = %(modelo)s,
                        dimension = %(dimension)s,
                        peso = %(peso)s,
                        peso_volumetrico = %(peso_volumetrico)s,
                        ancho = %(ancho)s,
                        largo = %(largo)s,
                        alto = %(alto)s,
                        apilable = %(apilable)s,
                        maxApilable = %(maxApilable)s,
                        propAncho = %(propAncho)s,
                        propAlto = %(propAlto)s,
                        propLargo = %(propLargo)s,
                        ruta = %(ruta)s,
                        pack = %(pack)s,
                        variantesAgrupadas = %(variantesAgrupadas)s,
                        packPadre = %(packPadre)s,
                        margen = %(margen)s,
                        stock = %(stock)s,
                        idMedida = %(idMedida)s,
                        precio = %(precio)s,
                        precioReferencia = %(precioReferencia)s,
                        img = %(img)s,
                        youtube = %(youtube)s,
                        video = %(video)s,
                        descripcion = %(descripcion)s,
                        descripcionCorta = %(descripcionCorta)s,
                        despacho = %(despacho)s,
                        retiroTienda = %(retiroTienda)s,
                        descuento = %(descuento)s,
                        mostrarHome = %(mostrarHome)s,
                        probador = %(probador)s,
                        destacado = %(destacado)s,
                        complemento = %(complemento)s,
                        precioComplemento = %(precioComplemento)s,
                        fichaTecnica = %(fichaTecnica)s,
                        nombreFicha = %(nombreFicha)s,
                        orientacion = %(orientacion)s,
                        delivery = %(delivery)s,
                        idProveedor = %(idProveedor)s,
                        idioma = %(idioma)s,
                        tag = %(tag)s,
                        meta_title = %(meta_title)s,
                        meta_description = %(meta_description)s,
                        actionStore = %(actionStore)s,
                        currencyBasePrice = %(currencyBasePrice)s,
                        saleDecimal = %(saleDecimal)s,
                        criticalStock = %(criticalStock)s,
                        idCategoria = %(idCategoria)s,
                        tipoVenta = %(tipoVenta)s,
                        cantidadLote = %(cantidadLote)s,
                        precioUnitario = %(precioUnitario)s,
                        rechazoProducto = %(rechazoProducto)s,
                        publicado = %(publicado)s,
                        created_at = %(created_at)s,
                        updated_at = %(updated_at)s,
                        deleted_at = %(deleted_at)s,
                        published_at = %(published_at)s,
                        centry_id = %(centry_id)s,
                        cat_id = %(cat_id)s,
                        cat_nombre = %(cat_nombre)s,
                        cat_alias = %(cat_alias)s,
                        cat_ruta = %(cat_ruta)s,
                        cat_img = %(cat_img)s,
                        cat_banner = %(cat_banner)s,
                        marca = %(marca)s,
                        updated_date = %(updated_date)s,
                        category = %(category)s
                    WHERE id = %(id)s
                """
                current_time = datetime.datetime.now()

                # Format the current time as required (YYYY-MM-DD HH:MM:SS)
                formatted_time = current_time.strftime('%Y-%m-%d %H:%M:%S')
                item['updated_date'] = formatted_time
                self.curr.execute(update_query, item)
                # Commit the transaction after updating the record
                self.conn.commit()

            
            for image in images:
                try:
                    self.curr.execute("INSERT INTO Images (id,image) VALUES (%s,%s)", (item_id,image))
                    self.conn.commit()  
                except Exception as e:
                    pass

