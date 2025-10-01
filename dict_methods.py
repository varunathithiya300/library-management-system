
my_dict = dict(name = 'varun', age = 31)


def update_dict():
    print(my_dict)
    
    if my_dict.get('name'):
        my_dict.update(name = 'Athithiya')
    return my_dict

print(update_dict())