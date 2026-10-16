def purchase(product, wallet):
    """
    Kjøper en vare (dictionary med name/price) og returnerer det nye beløpet til lommeboka.
    """
    print(f"Du har {wallet} kr.")
    print(f"{product['name']} koster {product['price']} kr.")

    wallet = wallet - product["price"]
    print(f"Du sitter igjen med {wallet} kr")

    return wallet


def sell(product, wallet):
    """
    Selger en vare (dictionary med name/price) og returnerer det nye beløpet til lommeboka.
    """
    print(f"Du har {wallet} kr.")
    print(f"{product['name']} selges for {product['price']} kr.")

    wallet = wallet + product["price"]
    print(f"Du sitter igjen med {wallet} kr")

    return wallet
