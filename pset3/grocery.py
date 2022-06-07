from collections import OrderedDict

list = {
}
#getting items
while True:
    try:
        item=input().strip().upper()
    except EOFError:
        break
    else:
        if item in list:
            list[item]+=1
        else:
            list[item]=1
#sort list
sorted_keys = sorted(list.keys())
sorted_list = {key:list[key] for key in sorted_keys}
#print list
for item in sorted_list:
    print( sorted_list[item], item)