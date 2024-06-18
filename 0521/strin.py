s = input("string 3 : ").split()

print(s)
print(type(s))
print(type(s[0]))

lst = [int(x) for x in s]

print(lst)

lst2 = [int(x)for x in input().split()]

print(lst2)

a,b,c = map(int, input("int 3 : ").split())

print("a",a)
print("b",b)
