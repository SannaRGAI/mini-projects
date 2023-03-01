from utils import get_products, update_products

def create():
    title = input("Введите название: ")
    price = float(input("Введите цену: "))
    # принимаем данные

    new_product = {"title":title, "price":price}
    # собираем в словарь

    products = get_products() 
    # получаем список старых продуктов
    products.append(new_product)
    # добавляем в список новые данные
    update_products(products)
    # перезаписываем файл с новыми данными

def read():
    products = get_products()
    # получаем список продуктов
    for product in products:
        # проходимся по каждому продукту и принтим
        print(f"""
==========================================
Название: {product['title']}
Цена: {product['price']}
==========================================
""")

def delete():
    products  = get_products()
    print(" pick smth to delete: ")
    for ind, prod in enumerate(products):
        print(f'{ind} =>{prod["title"]}')
    index = int(input())
    products.pop(index)
    update_products(products)

def update():
    products  = get_products()
    print(" pick smth to update: ")
    for ind, prod in enumerate(products):
        print(f'{ind} =>{prod["title"]}')
    index = int(input())
    prod = products[index]
    print(f"""
    name: {prod['title']}
    price:{prod['price']}
    update_products(products)
""")
    field = input("what would you like ot update?")(title,price)
    if field =="title":
        ...
    elif field == 'price':
        ...
        prod['price'] = float(value)
        update_products(products)