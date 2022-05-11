#Daily coding problem 1

#Given a list of numbers and a number k, return whether any two numbers from the list add up to k.For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.


l = [10, 15, 3, 7]
k = 17

l_len = len(l)

def compute(a_list, k):
    
    
    for i in range(l_len):

        a_list_len = len(a_list)
        base_num = a_list[0]
        sum_num = 0
 
        a_list.pop(0)

        
        a_list_len = len(a_list)
        for j in range(a_list_len):
            sum_num = base_num + a_list[j]
           

            if sum_num == k:
               
                return base_num, a_list[j]
    
    return False

r = compute(l, k)

if not r:
    print("there was no match!")
else:
    print(f'there was a match with k({k}), {r[0]} + {r[1]}')












