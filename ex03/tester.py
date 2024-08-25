from NULL_not_found import NULL_not_found
"""
Variables with different "null" types
"""
Nothing = None
Garlic = float("NaN")
Zero = 0
Empty = ""
Fake = False

"""
NULL_not_found function calls with different "null" types
"""
NULL_not_found(Nothing)
NULL_not_found(Garlic)
NULL_not_found(Zero)
NULL_not_found(Empty)
NULL_not_found(Fake)

"""
Function call to test the output "Type not Found"
"""
print(NULL_not_found("Brian"))
