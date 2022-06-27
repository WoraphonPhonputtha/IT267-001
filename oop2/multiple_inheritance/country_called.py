from country import Country

#create countries
#Thai lat 13.7649136 long 100.5360959 area 513120 pop 70078203 temp 32c  

c1 = Country('Thailand', 513120, 70078203)
c1.setcordinate(13.7649136, 100.5360959)
c1.setcelcius(32)
c1.showdetail()

c2 = Country('England', 130279, 68497907)
c2.setcordinate(51.509865, -0.118092)
c2.setcelcius(13)
c2.showdetail()

c3 = Country('Senegal', 196722, 17653671)
c3.setcordinate(14.716677, -17.467686)
c3.setcelcius(29)
c3.showdetail()