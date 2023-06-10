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
