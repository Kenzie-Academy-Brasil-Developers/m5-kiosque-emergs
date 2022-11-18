from menu import products

def get_product_by_id(id:int):
  if type(id) == int:
    for prod in products:
      if prod['_id'] == id:
        return prod
    return {}
  else:
    raise TypeError('product id must be an int')

def get_products_by_type(_type:str):
  if type(_type) == str:
    products_list = []
    for prod in products:
      if prod['type'] == _type:
        products_list.append(prod)
      
    return products_list if len(products_list) > 0 else []
  else:
    raise TypeError('product type must be a str')

def menu_report():
  length_products = len(products)
  total_price = 0

  for prod in products:
    total_price += prod['price']
  average_price = round(total_price/length_products , 2)

  types = []
  occurrences = 0
  types_more_occurrences = ''
  for prod_type in products:
    types.append(prod_type['type'])

  for item in types:
    if types.count(item) > occurrences:
      types_more_occurrences = item
      occurrences = types.count(item)
  
  return(f"Products Count: {length_products} - Average Price: ${average_price} - Most Common Type: {types_more_occurrences}")

def generate_id(menu_products):
    biggest_id = 0
    new_id = 0
    if len(menu_products) == 0:
        new_id+=1
    else:
        for id in products:
            if id['_id'] > biggest_id:
                new_id = id['_id'] + 1
                biggest_id = id['_id']

    return new_id
   
def add_product(menu_products, **kwargs):
    new_id = generate_id(menu_products)
    new_item = {'_id':new_id, **kwargs}
    menu_products.append(new_item)
    return new_item
   
