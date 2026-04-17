def remove_key(d, key):
    if key in d:
        del d[key]
        return d
    return "Kalit topilmadi"

info = {'name': 'Ali', 'age': 25, 'city': 'Toshkent'}
print(remove_key(info, 'age'))   # {'name': 'Ali', 'city': 'Toshkent'}
