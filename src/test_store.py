from store import purchase, sell

# Et eksempel på et produkt-dictionary,
# name (str) og price (int) må eksistere
product = {"name": "Bok", "price": 200}
wallet = 1000

# Test av kjøp
wallet = purchase(product, wallet)
assert wallet == 0

# Test av salg
wallet = sell(product, wallet)
assert wallet == 0
