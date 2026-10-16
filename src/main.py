import time
from store import purchase, sell

print("Velkommen til nettbutikken!")

wallet = 1000

while True:
    print('Du kan bruke "k" (kjøp) eller "s" (selg). "q" avslutter')
    print(f"Du har {wallet} kr i lommeboka.")
    command = input("Hva vil du gjøre? ")
    if command == "k":
        product_name = input("Hva kjøper du? ")
        product_price = int(input("Hvor mye koster det (helt tall)? "))
        product = {
            "name": product_name,
            "price": product_price,
        }
        wallet = purchase(product, wallet)
    elif command == "s":
        product_name = input("Hva selger du? ")
        product_price = int(input("Hvor mye selger du det (helt tall)? "))
        product = {
            "name": product_name,
            "price": product_price,
        }
        wallet = sell(product, wallet)
    elif command == "q":
        break
    else:
        print("Ukjent kommando.")
    time.sleep(2)
    print("=========================\n")  # Mer rom til neste gang ;)

print("Takk for at du handlet med oss!")
