import csv
import re

def get_data(infofiles):
	os_prod_list, os_name_list, os_code_list, os_type_list = [], [], [], []
	os_prod, os_name, os_code, os_type = 'Изготовитель ОС', 'Название ОС', 'Код продукта', 'Тип системы'
	main_data = [os_prod, os_name, os_code, os_type]

	for infofile in infofiles:
		with open(infofile) as info:
			for line in info:
				if re.match(os_prod, line):
					os_prod_list.append((re.split(r':\s+', line)[1])[:-1])
				if re.match(os_name, line):
					os_name_list.append((re.split(r':\s+', line)[1])[:-1])
				if re.match(os_code, line):
					os_code_list.append((re.split(r':\s+', line)[1])[:-1])
				if re.match(os_type, line):
					os_type_list.append((re.split(r':\s+', line)[1])[:-1])
	return main_data, os_prod_list, os_name_list, os_code_list, os_type_list

def write_to_csv(filename):
	title, prod, name, code, os_type = get_data(['info_1.txt', 'info_2.txt', 'info_3.txt'])
	with open(filename, 'w') as info:
		info_writer = csv.writer(info)
		info_writer.writerow(title)
		for item in range(3):
			row = []
			for param in (prod, name, code, os_type):
				row.append(param[item])
			info_writer.writerow(row)

if __name__ == '__main__':

	write_to_csv('report.csv')
