items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

def find_item_index(items, item_):  # функция, принимающая список товаров и товар, который нужно найти
    for index, current_item in enumerate(items):  # поиск индекса
        if current_item == item_:
            return index

for find_item in ['банан', 'груша', 'персик']:
    index_item = find_item_index(items_list, find_item)
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")


