with open('currencyData.txt') as f:
    lines = f.readlines()

currencyDict = {}
for line in lines:
    parsed = line.strip().split("\t")
    if len(parsed) == 2:
        try:
            currencyDict[parsed[0]] = float(parsed[1])
        except ValueError:
            print(f"Warning: Invalid conversion rate for {parsed[0]} - skipping.")

amount = float(input("Enter amount in USD: "))

print("Available currencies for conversion:")
for currency in currencyDict.keys():
    print(currency)

currency = input("Please enter the name of the currency to convert to: ")

if currency in currencyDict:
    conversion_rate = currencyDict[currency]
    converted_amount = amount * conversion_rate
    print(f"{amount} USD is equal to {converted_amount:.2f} {currency}")
else:
    print("Currency not found.")
