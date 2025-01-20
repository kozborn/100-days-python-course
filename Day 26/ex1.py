list1 = open('file1.txt').read().splitlines()
list2 = open('file2.txt').read().splitlines()

print(list1)
print(list2)

result = [int(n) for n in list1 if n in list2]

print(result)