import re
import json

with open("raw.txt", "r", encoding="utf-8") as f:
    text = f.read()

lines = [line.strip() for line in text.splitlines() if line.strip()]

#1
price_pattern = r'\d[\d ]*,\d{2}'
prices = re.findall(price_pattern, text)

print(prices)

#2
product_names = []

for i in range(len(lines) - 1):
    if re.match(r'^\d+\.$', lines[i]):
        product_names.append(lines[i + 1])

print(product_names)

#3
item_totals = []

for i in range(len(lines) - 3):
    if re.match(r'^\d+\.$', lines[i]):
        line_total = lines[i + 3]
        if re.match(r'^\d[\d ]*,\d{2}$', line_total):
            value = float(line_total.replace(' ', '').replace(',', '.'))
            item_totals.append(value)

calculated_total = sum(item_totals)
print(calculated_total)

#4
datetime_match = re.search(r'Время:\s*(\d{2}\.\d{2}\.\d{4})\s+(\d{2}:\d{2}:\d{2})', text)

if datetime_match:
    date = datetime_match.group(1)
    time = datetime_match.group(2)
else:
    date = None
    time = None

print("Date:", date)
print("Time:", time)

#5
payment_match = re.search(r'(Банковская карта|Наличные|Карта)', text, re.IGNORECASE)

if payment_match:
    payment_method = payment_match.group(1)
else:
    payment_method = "Не найден"

print(payment_method)

#6
items = []

for i in range(len(lines) - 3):
    if re.match(r'^\d+\.$', lines[i]):
        name = lines[i + 1]

        qty_price_match = re.match(r'^([\d,]+)\s*x\s*([\d ]+,\d{2})$', lines[i + 2])
        total_match_item = re.match(r'^(\d[\d ]*,\d{2})$', lines[i + 3])

        if qty_price_match and total_match_item:
            quantity = qty_price_match.group(1)
            unit_price = qty_price_match.group(2)
            line_total = total_match_item.group(1)

            items.append({
                "name": name,
                "quantity": quantity,
                "unit_price": unit_price,
                "line_total": line_total
            })

total_str = None

total_match = re.search(r'ИТОГО:\s*([\d ]+,\d{2})', text)
if total_match:
    total_str = total_match.group(1)

result = {
    "items": items,
    "prices": prices,
    "total": total_str,
    "date": date,
    "time": time,
    "payment_method": payment_method
}

print(json.dumps(result, ensure_ascii=False, indent=2))