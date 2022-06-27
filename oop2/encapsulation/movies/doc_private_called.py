from documentary_private import Documentary

m = Documentary('Mulan', 2020, 'Action')
#m.__get_movie() #เรียก Pirvate method จะ error
#print(m.__genre) #เรียก Pirvate attribute จะ error
m.print_detail()
print(f'year : {m._Movie__year}')