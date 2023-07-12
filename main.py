from pprint import pprint

cook_book = {}

with open('recipes.txt', encoding="utf-8") as f:
    for line in f:
        ingredient_list = []
        menu = {}
        dish_name = line.strip()
        # print(dish_name)
        ingredient_quantity = f.readline()
        # print(ingredient_quantity)
        for ingredient in range(int(ingredient_quantity)):
            ingredient_name, quantity, measure = f.readline().strip().split(' | ')
            ingredient_list.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
        dish = {dish_name: ingredient_list}
        emp = f.readline()
        cook_book.update(dish)

# print(cook_book)
print()

def get_shop_list_by_dishes(dishes, person_count):
    shop_list_by_dishes = {}
    for dish in dishes:
        ingredient_list = cook_book.get(dish)
        for i in ingredient_list:
            ingredient = i.pop('ingredient_name')
            i['quantity'] = int(i.get('quantity')) * person_count
            ingredient_dict = {ingredient: i}
            if ingredient not in shop_list_by_dishes.keys() :
                shop_list_by_dishes.update(ingredient_dict)
            else:
                shop_list_by_dishes[ingredient]['quantity'] = shop_list_by_dishes[ingredient]['quantity'] + i['quantity']
    return shop_list_by_dishes


pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
print()
pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Картофель пюре'], 2))
