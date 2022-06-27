from area import Area

b = float(input('Enter Base : '))
h = float(input('Enter high : '))

aobj = Area()
#Using Setter
aobj.base = b
aobj.high = h
print(f'Area : {aobj.compute_area()}')