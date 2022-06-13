class C:
    dangerous = 2

c1 = C()
c2 = C()
print(c1.dangerous)
# output = 2

c1.dangerous = 3
print (c1.dangerous )
print (c2.dangerous )
# output = 3
# output = 2

del c1.dangerous
print (c1.dangerous )
# output = 2

C.dangerous = 3
print (c2.dangerous)
# output = 3
