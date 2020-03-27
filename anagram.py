class Solution:
    def Anagram(a,b):
        result = []
        for i in range(0,len(b)):
            if a[i] in b:
                result.append(b.index(a[i]))

        return result

    a = [12,28,46,32,50]
    b=[50,12,32,46,28]
    print(Anagram(a,b))