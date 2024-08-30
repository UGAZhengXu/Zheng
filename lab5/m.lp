\ Model TestLP
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  x + y + z[0] + z[1] + z[2] + z[3] + z[4]
Subject To
 a0: 2 x + 3 y <= 15
 a1: y >= -3
 a2: x - y >= 0
 c3[0]: z[0] >= 2
 c3[1]: z[1] >= 2
 c3[2]: z[2] >= 2
 c3[3]: z[3] >= 2
 c3[4]: z[4] >= 2
 c4[0,0]: z[0] + z[1] + z[2] + z[3] + z[4] >= 10
 c4[0,1]: z[0] + z[1] + z[2] + z[3] + z[4] >= 10
 c5[0,0]: z[0] + z[1] + z[2] + z[3] + z[4] >= 10
 c5[0,1]: z[0] + z[1] + z[2] + z[3] + z[4] >= 10
 c5[1,0]: z[0] + z[1] + z[2] + z[3] + z[4] >= 10
 c5[1,1]: z[0] + z[1] + z[2] + z[3] + z[4] >= 10
Bounds
 x free
 y free
 z[0] >= 1
 z[1] >= 1
 z[2] >= 1
 z[3] >= 1
 z[4] >= 1
End
