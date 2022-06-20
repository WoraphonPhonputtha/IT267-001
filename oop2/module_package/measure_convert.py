def inchtocen(inch:float):
    return f'{inch * 2.54:,.2f}'

def centoinch(cen:float):
    return f'{cen / 2.54:,.2f}'

if __name__ == '__main__':
    print(inchtocen(2.54))
    print(centoinch(5))
