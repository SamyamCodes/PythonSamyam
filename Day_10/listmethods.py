l = [112,2,34,43,54543,13312, 12131, 21,323,12,233]
l.append(7)
print(l)
l.sort()
print(l)
l.sort(reverse = True)
print(l)
l.reverse() # Reverses the original list
print(l)

l.insert(1, 899)  # index 1 ma 899 inset hunxa.
print(l)

m = [900, 1000, 1100]
l.extend(m) #m ko list l ko last ma rakhne.
print(l)

# This can also be done by: concatinating two list.
k = l+m
print(k)


