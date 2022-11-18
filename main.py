from management.product_handler import get_product_by_id, get_products_by_type, menu_report, add_product
from management.tab_handler import calculate_tab

new_product = { 
      "title": "Bolinho JS",
      "price": 1.0,
      "rating": 2,
      "description": "Bolinho de JS com cenoura",
      "type": "bakery",}

table_1 = [{"_id": 1, "amount": 5}, {"_id": 19, "amount": 5}]

menu_products = []

if __name__ == "__main__":
    #print(get_product_by_id(30))
    #print(get_products_by_type('vegetable'))
    #print(menu_report())
    print(add_product(menu_products, **new_product))
    #print(calculate_tab(table_1))
    ...
