def main(array):
    options = ((2018, None, 'SAS', 'XTEND'),
               (2017, None, 'SAS', 'XTEND'),
               (2000, None, 'SAS', 'XTEND'),
               (2018, None, 'SAS', 'JAVA'),
               (2017, None, 'SAS', 'JAVA'),
               (2000, None, 'SAS', 'JAVA'),
               (2018, None, 'SAS', 'NUMPY'),
               (2017, None, 'SAS', 'NUMPY'),
               (2000, None, 'SAS', 'NUMPY'),
               (None, 'GOLO', 'POD', None),
               (None, 'XSLT', None, None),
               (None, None, 'BRO', None))
    for i, option in enumerate(options):
        flag = True
        for j in range(len(option)):
            if option[j] is None:
                continue
            elif option[j] != array[j]:
                flag = False
                break
        if flag:
            return i


print(main([2018, 'GOLO', 'POD', 'NUMPY']))
print(main([2017, 'XSLT', 'SAS', 'XTEND']))
print(main([2017, 'GOLO', 'BRO', 'XTEND']))
print(main([2018, 'XSLT', 'POD', 'NUMPY']))
print(main([2017, 'GOLO', 'SAS', 'NUMPY']))


def main_2(array):
    options = (('DYLAN', None, 2004, None, 'GAMS'),
               ('DYLAN', None, 2005, 'HY', 'GAMS'),
               ('DYLAN', None, 2005, 'ADA', 'GAMS'),
               ('DYLAN', None, 2005, 'LUA', 'GAMS'),
               ('DYLAN', None, 2001, None, 'GAMS'),
               ('DYLAN', None, None, 'HY', 'TLA'),
               ('DYLAN', None, None, 'ADA', 'TLA'),
               ('DYLAN', 1990, None, 'LUA', 'TLA'),
               ('DYLAN', 2013, None, 'LUA', 'TLA'),
               ('DYLAN', 1960, None, 'LUA', 'TLA'),
               ('DYLAN', None, None, None, 'NGINX'),
               ('M', None, None, None, None),
               ('ATS', None, None, None, None))

    for i, option in enumerate(options):
        flag = True
        for j in range(len(option)):
            if option[j] is None:
                continue
            elif option[j] != array[j]:
                flag = False
                break
        if flag:
            return i


print(main_2(['ATS', 2013, 2001, 'HY', 'NGINX']))
print(main_2(['DYLAN', 1960, 2001, 'LUA', 'NGINX']))
print(main_2(['DYLAN', 1960, 2005, 'HY', 'GAMS']))
print(main_2(['DYLAN', 1990, 2005, 'LUA', 'GAMS']))
print(main_2(['DYLAN', 1990, 2005, 'ADA', 'GAMS']))
