# Printing all subsequences of the Array 
  # TC = O(n × 2ⁿ).
  # SC = O(n) Recursive Stack + Auxillary Array Space O(N + N) = 2N

arr = [3,1,2]

def f(ind, auxi, n):
    
    if ind >= n:
        print(auxi)
        return
    
    auxi.append(arr[ind])
    f(ind+1, auxi, n)
    auxi.remove(arr[ind])
    f(ind+1, auxi, n)

f(0, [], len(arr))
