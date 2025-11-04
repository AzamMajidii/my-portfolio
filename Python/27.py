import csv

with open("products.csv", mode="r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    products = list(reader)

processed_data = []
for product in products:
    Name = product["Product Name"]
    Price = float(product["Price"])
    Quantity = int(product["Quantity"])
    Total = Price * Quantity
    processed_data.append({
        "Name": Name,
        "Price": Price,
        "Quantity": Quantity,
        "Total": Total
    })


with open("processed_products.csv", mode="w", newline="", encoding="utf-8") as file:
    fieldnames = ["Name", "Price", "Quantity", "Total"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(processed_data)

