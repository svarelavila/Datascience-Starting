"""
Define the original data structures
"""
ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

"""
Modify data structures
"""
ft_list[1] = "World!"
ft_tuple = (ft_tuple[0], "Spain!")
ft_set = {"Hello", "Urduliz!"}
ft_dict["Hello"] = "42Urduliz!"

"""
Print the modified structures
"""
print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
