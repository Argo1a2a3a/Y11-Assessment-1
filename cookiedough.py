print("COOKIE DOUGH SALES POINTS AND PRIZES TRACKER")

sales_data = {}

while True:
    name = input("Name: ").strip().lower()
    if name == "":  
        break
    cookie_dough_sold = int(input("Cookie dough sold: "))

    if name in sales_data:
        sales_data[name] += cookie_dough_sold  
    else:
        sales_data[name] = cookie_dough_sold  

print("\nSelling over! Let's see how everyone did!")

for name, points in sales_data.items():
    prizes = points // 10  
    print(f"{name.capitalize()} has {points} points and can redeem {prizes} prize(s).")