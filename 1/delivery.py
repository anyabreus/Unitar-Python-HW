prices = [250, 480, 199, 71]
total = 0
for price in prices:
    total = total + price
if total >= 1000:
    print("Free delivery")
else:
    print("Missing to 1000:", 1000 - total)
