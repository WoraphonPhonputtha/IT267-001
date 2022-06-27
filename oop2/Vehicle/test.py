from bus import Bus
from motocycle import Motocycle

b = Bus('Bus', 4, 120,'v1234')
#b.color = 'Blue'
b.set_color('Blue')
#b.capacity = 34
b.set_capacity(34)
b.bus_detail()

bike = Motocycle('Motocycle', 2, 200,'v3456')
#bike.cc = 1200
bike.set_cc(1200)
bike.bike_detail()