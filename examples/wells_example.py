from wells import *
  
print("Start")

WF = WellField()
WF.add_well( Well( 'well#1', 11, -7 ) )
WF.add_well( Well( 'well#2', -99, 88, 1 ) )
WF.add_well( Well( 'well#3', 1, 1 ) )

w = Well( 'well#4', 100, 100, -2 )
w.add_geometry_step( 15 )
w.add_geometry_step( 11 )
WF.add_well( w )

for i in WF.Well_list:
  print ( 'wellhead %s X %+5d Y %+5d Z %+5d   well_length %d' % ( i.wellname, i.wellhead_X, i.wellhead_Y, i.wellhead_Z, i.well_length ) )

print ( 'field size top (X %d Y %d Z %d) bottom (X %d Y %d Z %d)' % ( WF.topleft_X, WF.topleft_Y, WF.topleft_Z, WF.bottomright_X, WF.bottomright_Y, WF.bottomright_Z ) )

print("End")