#####################First Attempt########################
def PP(a):
    length = len(a)
    countMap={i: a.count(i) for i in set(a)}
    result = True
    if length%2==0:
        for i in countMap:
            if countMap[i]%2==0:
                result  = True
            else:
                result = False
                break
    else:
        sum = 0
        for i in countMap:
            if countMap[i]%2==0:
                result=True
            else:
                sum+=1
        if sum==1:
            return result
        else:
            return False


    return result
################################Second Attempt#########################################################
def is_palindrome(s):
    odd_counter = 0
    for letter in s:
        if s.count(letter) % 2 != 0:
            odd_counter += 1

    if odd_counter > 1:
        return False
    return True





##########################################Runner########################################################
# print(PP("aabbccdddddd"))
print(is_palindrome("aabbccdddddddd"))