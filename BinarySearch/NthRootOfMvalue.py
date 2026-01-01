# Nth Root of M

n = int(input("Enter the Root Number :"))
m = int(input("Enter the Base Value :"))

def mulResult(mid, n):
    ans = 1
    for i in range(1, n+1):
        ans = ans * mid
    return ans


low, high = 1, m
isPerfectNthroot = False

while low <= high:
    mid = (low + high) // 2
  
    ans = mulResult(mid, n)
    if ans == m:
        print(mid)
        isPerfectNthroot = True
        break
    elif ans > m:
        high = mid - 1
    else:
        low = mid + 1

if isPerfectNthroot == False:
   print(-1)




    



