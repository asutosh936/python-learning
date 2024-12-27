numbers = [5,10,2,0]

numbers.sort()
print(numbers)
print(numbers[0])

def mergeStrings(string1, string2):

    mergeString = ''
    for i in range(len(string1)):
        mergeString = mergeString + string1[i] + string2[i]
            
        
    return mergeString

print(mergeStrings('abc', 'def'))
