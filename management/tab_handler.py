from menu import products 

def calculate_tab(kwargs):
  sub_total = 0
  for table in kwargs:
    id_product = table['_id']
    product = [prod for prod in products if id_product == prod['_id']]
    for item in product:
      sub_total += item['price'] * table['amount'] 
  return {'subtotal': f'${round(sub_total,2)}'}
    