def print_ware_information(ware):
    print(f"Name: {ware['name']}")
    print(f"Price: {ware['price']},-")
    print(f"Number in stock: {ware['number_in_stock']}")
    print(f"Description: {ware['description']}")

def calculate_average_ware_rating(ware):

    sumRate = sum(ware["ratings"])
    length = len(ware["ratings"])
    
    try:
        avgRating = sumRate / length
    
    except ZeroDivisionError:
        return 0.0 
    
    else:
        return round(avgRating, 1)
    
def get_all_wares_in_stock(all_wares):

    allWaresInStock = {}

    #For loop som går igenom varorna i all_wares
    for wareId, ware in all_wares.items():
        if ware["number_in_stock"] >= 1:
            allWaresInStock[wareId] = ware

    return allWaresInStock

def is_number_of_ware_in_stock(ware, number_of_ware):
    #If test för att checka om ware är större eller lik number_of_ware
    if number_of_ware <= ware["number_in_stock"]:
        return True
    else:
        return False

def add_number_of_ware_to_shopping_cart(ware_key, ware, shopping_cart,
number_of_ware=1):
    
    if is_number_of_ware_in_stock(ware, number_of_ware):
        if ware_key in shopping_cart: # Om varan redan är i kundvagnen
            shopping_cart[ware_key] += number_of_ware
            ware["number_in_stock"] -= number_of_ware # Uppdaterar lagerstatus

        else: 
            shopping_cart[ware_key] = number_of_ware #Om varan inte redan finns i kundvagnen så ska den läggas till
            ware["number_in_stock"] -= number_of_ware 
    
        print(f"Du har lagt till {number_of_ware}st {ware['name']} i kundvagnen.")

    #Om antal varor är fler än dem som finns på lager och om det är fler än 0 i lager
    elif number_of_ware > ware["number_in_stock"] and 0 < ware["number_in_stock"]:
        prevStock = ware["number_in_stock"]

        if ware_key in shopping_cart: #Om varan redan finns i kundvagnen
            shopping_cart[ware_key] += prevStock #Lägger till samma antal som är i lagerstatus
            ware["number_in_stock"] -= prevStock #Uppdaterar lagerstatus genom att ta den minus sig själv

        else:
            shopping_cart[ware_key] = prevStock 
            ware["number_in_stock"] -= prevStock

        print(f"Du önskar {number_of_ware}st {ware['name']}, men det finns bara {prevStock}st. {prevStock}st {ware['name']} har lagts till i kundvagnen.")

    else:
        print(f"{ware['name']} finns inte i lager.")

def calculate_shopping_cart_price(shopping_cart, all_wares, tax=25):
    total = 0 

    #for loop för ware_key och dess antal i kundvagnen
    for ware_key, wareCount in shopping_cart.items():
        #Genom att ta priset på antal varor med det priset får jag ut totalen utan att skatt är inräknat
        total += all_wares[ware_key]["price"] * wareCount
    
    #Lägger till skatt genom att gångra totalen med 1,25
    return total * (1 + tax / 100)
        

