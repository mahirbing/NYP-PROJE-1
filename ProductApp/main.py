# main.py

from Helpers.product_helper import ProductHelper

def main():
    # Products.txt dosyasından ürünler okunuyor
    products = ProductHelper.create_item_from_text('Products.txt')

    # Her ürünü yazdır
    for product in products:
        print(product)

    # Toplam bakiye hesapla
    total_balance = ProductHelper.get_total_balance(products)
    print(f"Total balance with VAT: {total_balance}")

if __name__ == "__main__":
    main()
