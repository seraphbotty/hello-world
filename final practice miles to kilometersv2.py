#John Salazar
#8-14-17
#engr 120


def miles2km(miles):
    one_mile = 1.609
    me = miles*one_mile

    return me


for i in range(1, 11):
    print(i, "\t\t", miles2km(i))