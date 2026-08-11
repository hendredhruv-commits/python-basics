# from typing import Literal


# countries=("India","USA","UK","Germany","France")
# temp=list(countries)
#                             #add
# # temp.pop(3)

# # countries = tuple(temp)
# # temp[2]="China"
# countries: tuple[Literal['India'] | Literal['USA'] | Literal['UK'] | Literal['Germany'] | Literal['France'], ...] = tuple(temp)
# print(countries)

tuple1=(0,1,1,2,3,4,5,6,6,7,8)
res = tuple1.count(6)
res = tuple1.index(6)
res = tuple1.index(6, 7, 8)
# print("Count of 6 in tuple1 is:", res)