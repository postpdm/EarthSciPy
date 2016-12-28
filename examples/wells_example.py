from wells import *
  
print("Start")

WF = WellField()
WF.add_well( Well( 11, -7 ) )
WF.add_well( Well( -99, 88 ) )
WF.add_well( Well( 1, 1 ) )
WF.add_well( Well( 100, 100 ) )

for i in WF.Well_list:
  print (i.wellhead_X, i.wellhead_Y)

print( WF.topleft_X, WF.topleft_Y, WF.bottomright_X, WF.bottomright_Y )

print("End")