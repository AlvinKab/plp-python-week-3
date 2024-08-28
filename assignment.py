def calculate_discount(price, discount_percent):
    discount = discount_percent / 100
    if discount > 1:
        print("Discount cannot be greater than 100%")
        return -1
    elif discount >= 0.2:
        print(f"Qualified for a discount! Final price: {price * (1 - discount)}")
        return price * (1 - discount)
    else:
        print(f"No discount for you. Final price: {price}")
        return price
    
user_price = int(input("Enter the price: "))
user_discount = float(input("Enter the discount in percentage form: "))
calculate_discount(user_price, user_discount)