# robot store

product_names = ["Ultrasonic range finder", "Servo motor", "Servo controller", "Microcontroller Board", "Laser range finder", "lithum polymer battery" ]
product_prices = [2.50, 14.99, 44.95, 34.95, 149.99, 8.99]
product_quantities = [4, 10, 5, 7, 2, 8]

def print_stock():
    print("\nAvailable Products")
    print("---------------")
    for i in range(0, len(product_names)):
        if product_quantities[i] > 0:
            print(str(i) + ")", product_names[i], "$", product_prices[i])
    print()
class product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
#
    def stock():
        from collections import Counter



# prodcuts are given values of name, price, and qauntity
p1 = product("Ultrasonic range finder", 2.50, 4)
p2 = product("servo motor", 14.99, 10)
p3 = product("Servo Controller", 44.95, 5)
p4 = product("Microcontroller Board", 34.95, 7)
p5 = product("Laser range finder", 149.99, 2)
p6 = product("Lithium polymer battery", 8.99, 8)

# declare list of items
#(already done)
# declare a counter variable
count = 0
 
# iterate on items using for-loop
# and keep increasing the value of count
for i in product_quantities:
    # increment the value of count
    count = count+1
 
# print the list elements
print(product_quantities)
print("Quantity of items in the list are:", count)


def price():
    count =  0
    for i in product_prices:
        count = count+1
    print(product_prices)
    print("Price of items in the list are:", count)


def main():
    cash = float(input("How much money do you have? $"))
    while cash < 0:
        print_stock()
        vals = input("Enter product ID and quantity you wish to buy: ").split(" ")
        if vals[0] =="quit": break

        prod_id = int(vals[0])
        count = int(vals[1])

        if product_quantities[prod_id] >= count:
            if cash >= product_prices[prod_id]:
                product_quantities[prod_id] * count
                print("you purchased", count, product_names[prod_id] + ".")
                print("you have $", "{0;.2f}".format(cash), "remaining.")
            else:
                print("sorry, you cannot afford that product.")
        else:
            print("sorry, we are sold out of", product_names[prod_id])

main()
