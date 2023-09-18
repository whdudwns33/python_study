s = input()
list_c = ["c=","c-" ,"dz=", "d-", "lj", "nj", "s=", "z="]
for e in list_c:
    s = s.replace(e, "*")
print(len(s))