"""
number_list = []
n = int(input("Introdu numarul de elemente: "))
print("\n")
for i in range(0, n):
    print("Introdu elementul la pozitia: ", i, )
    item = int(input())
    number_list.append(item)
print("\n")
print("Lista este", number_list)
sorted_numbers = sorted(number_list)

print("\n")
print("Lista ordonata este", sorted_numbers)
reversed_numbers = sorted(sorted_numbers, reverse=True)


print("\n")
print("Ordonata descrescator este", reversed_numbers)


print("\n")
print("Minimul listei este", min(number_list))
print("Maximul listei este", max(number_list))


print("\n")
number_list.remove(9)
print("Lista fara elementul \"9\" este", number_list)


print("\n")
number_list.pop()
print("Lista fara ultimul element este", number_list)


print("\n")
string_list = []
m = int(input("Introdu numarul de siruri: "))
print("\n")
for i in range(0, m):
    print("introdu sirul la pozitia: ", i, )
    sir = str(input())
    string_list.append(sir)
print("\n")
print("Lista de siruri este", string_list)


print("\n")
string_list.remove('a')
print("Lista fara elementu \"a\" este", string_list)


print("\n")
string_list.pop()
print("Lista fara ultimul element este", string_list)


"""


"""

def cmmdc(x, y):
    r=x%y
    if(r==0):
        return y
    else:
        return cmmdc(y, r)
n = int(input("Enter the first number :"))
m = int(input("Enter the second number :"))

print("Cel mai mare divizor comun este:", cmmdc(n, m))


"""


my_string = "A1T1730"
my_string = my_string[1] + my_string[-4]
print(my_string)




print("\n")
my_string = "A1T1730"
my_string = my_string[1] + my_string[-4:]
print(my_string)



print("\n")
my_string = "A1T1730"
my_string = my_string[2:]
print(my_string)


print("\n")
my_string = "A1T1730"
my_string = my_string[:2]
print(my_string)