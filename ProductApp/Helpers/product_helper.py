# Helpers/product_helper.py

from Models.product import Product

class ProductHelper:
    @staticmethod
    def create_item_from_text(filename):
        products = []
        with open(filename, 'r') as file:
            for line in file:
                name, price, quantity = line.strip().split(',')
                # Tip dönüşümleri yapılıyor
                price = float(price)
                quantity = int(quantity)
                products.append(Product(name, price, quantity))
        return products

    @staticmethod
    def get_total_balance(products):
        total = sum(product.get_total_price() for product in products)
        total_with_vat = total * 1.20  # %20 KDV ekleniyor
        return total_with_vat
