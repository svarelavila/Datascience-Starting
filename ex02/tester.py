from find_ft_type import all_thing_is_obj

"""
Definición de diferentes tipos de datos
"""
ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

"""
Llamar a la función con diferentes tipos de datos
"""
all_thing_is_obj(ft_list)
all_thing_is_obj(ft_tuple)
all_thing_is_obj(ft_set)
all_thing_is_obj(ft_dict)
all_thing_is_obj("Brian")
all_thing_is_obj("Toto")

"""
Imprimir el resultado de la función con un entero
"""
print(all_thing_is_obj(10))
