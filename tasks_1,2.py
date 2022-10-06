cook_book = {}
with open('recipes.txt', 'rt',encoding = 'utf8') as file:
    for i in file:
        dish = i.strip()
        book = []
        ingredients_count = file.readline()
        for l in range(int(ingredients_count)):
            ingr = file.readline()
            name, quantities, measure = ingr.strip().split(' | ')
            book.append({'ingredient_name': name,
                         'quantity': quantities,
                         'measure': measure})
        null_line = file.readline()
        cook_book[dish] = book
print(cook_book)
#______________________2 ЗАДАНИЕ_________________
n = True
dishes = []
while n == True:
    start = input("Добавить блюдо в список?(Да/Нет) ")
    start.lower()
    if start == 'да':
        menu = input("Введите блюдо: ")
        dishes.append(menu)
    else:
        n = False
person_count = int(input("Введите кол-во персон: "))

def get_shop_list_by_dishes(dishes, person_count):
    recipes = {}
    for cook_dish in dishes:
        for dish, sources in cook_book.items():
            if cook_dish == dish:
                for ing in sources:
                    incr = 0
                    name = ing['ingredient_name']
                    if name in recipes:
                        incr = int(ing['quantity']) * person_count
                    recipes[name] = {'measure': ing['measure'], 'quantities': int(ing['quantity']) * person_count + incr }
    return print(recipes)

get_shop_list_by_dishes(dishes, person_count)
