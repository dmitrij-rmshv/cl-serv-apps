import json

def write_order_to_json(item, quantity, price, buyer, date):
	with open('orders.json') as f:
		objs = json.load(f)
		order_num = len(objs['orders']) + 1
		order = dict(order_number=order_num, item=item, quantity=quantity, price=price, buyer=buyer, date=date)
		objs['orders'].append(order)
	with open('orders.json', 'w') as f:
		json.dump(objs, f, indent=4)

if __name__ == '__main__':

	item = input('Введите наименование товара: ')
	quantity = int(input('Введите количество товара: '))
	price = int(input('Введите цену: '))
	buyer = input('Введите имя покупателя: ')
	date = input('Введите дату: ')

	write_order_to_json(item, quantity, price, buyer, date)
