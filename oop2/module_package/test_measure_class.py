from measure import Measure

if __name__ == '__main__':
    """m1 = Measure(12.5)
    m2 = Measure(100)
    m3 = Measure(56)
    m4 = Measure(78)
    m5 = Measure(14)
    m6 = Measure(250)
    print(f'{m1.inch_cm()} cm')
    print(f'{m2.cm_inch()} inch')
    print(f'{m3.inch_cm()} cm')
    print(f'{m4.inch_cm()} cm')
    print(f'{m5.cm_inch()} inch')
    print(f'{m6.cm_inch()} inch')"""

    """inch_list = [52,18,20,40]
    for i in inch_list:
        m = Measure(i)
        print(m.inch_cm())"""

    num = float(input('Enter number : '))
    ch = input('Choose I(Inch to CM) / C(CM to Inch) : ').upper()
    if ch == 'I':
        m = Measure(num)
        print(m.inch_cm())
    elif ch == 'C':
        m = Measure(num)
        print(m.cm_inch())
    else:
        print('Choose Wrong Character')