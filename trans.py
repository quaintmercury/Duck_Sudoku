list1 = [[1,2,3],
        [1,2,3],
        [1,2,3]]

tlist1 = []
for col in range(len(list1[0])):
    colholder = []
    for row in list1:
        colholder.append(row[col])
    tlist1.append(colholder)

print(tlist1)
