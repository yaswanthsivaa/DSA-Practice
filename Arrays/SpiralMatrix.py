# Spiral Matrix

mat = [
    [ 1,  2,  3,  4],
    [ 5,  6,  7,  8],
    [ 9, 10, 11, 12],
    [13, 14, 15, 16]
]

top = left = 0

lm = len(mat)

right = len(mat[0])-1

bottom = len(mat)-1

ans = []

while (left <= right and top <= bottom):
  for i in range(left, right+1):
    ans.append(mat[top][i])

  top += 1

  for i in range(top, bottom+1):
    ans.append(mat[i][right])

  right -= 1

  if top <= bottom:
    for i in range(right, left-1, -1):
      ans.append(mat[bottom][i])

    bottom -= 1
  
  if left <= right:
    for i in range(bottom, top-1, -1):  # top + 1
      ans.append(mat[i][left])

    left += 1

print(ans)
