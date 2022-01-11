# Author: SCT (AMDG) 1/11/22

sixth_letter = []
not_foods = []
short_foods = []

def add_foods(lst):
    for i, v in enumerate(lst):
        try:
            if v[5] == i:
                sixth_letter.append(v)
            elif v != str:
                not_foods.append(v)
            else:
                v[7] < i
                short_foods.append(v)
        except:
            print("Invalid, input letters only")
        finally:
            print("sixth_letter:", sixth_letter)
            print("not_foods:", not_foods)
            print("short_foods:", short_foods)


add_foods(['potatoes', 'salsa', 'cherries', 'banana', 'apple'])
add_foods(['naan', 'celery', 'buckwheat', 7, 'clementine'])
add_foods(['cheeseburger', True, 'chicken', 'rice', 'radish'])
