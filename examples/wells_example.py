from wells import *
  
print("Start")

WF = WellField()
WF.add_well( Well( 'well#1', 11, -7 ) )
WF.add_well( Well( 'well#2', -99, 88, 1 ) )
WF.add_well( Well( 'well#3', 1, 1 ) )

w = Well( 'well#4', 100, 100, -2 )
w.add_geometry_step( 10, 0 )
w.add_geometry_step( 10, 45 )
w.add_geometry_step( 10, 90 )
w.add_geometry_step( 100, 0 )
WF.add_well( w )

print('\nprint out the list of wells')

for i in WF.Well_list:
  print ( 'wellhead %s X %+5d Y %+5d Z %+5d   well_length %d' % ( i.wellname, i.wellhead_X, i.wellhead_Y, i.wellhead_Z, i.well_length ) )

print('\nprint out the geometry data for well', w.wellname )

for s in w.geometry:
  print( 'Inclination %.1f tangent %.1f vertical %.1f. Start lenght %.1f. End point X Y Z (%.1f, %.1f, %.1f)' % 
         ( s.inclination, s.tangent, s.vertical, s.start_lenght,
           s.end_X, s.end_Y, s.end_Z ) )

print ( 'field size top (X %d Y %d Z %d) bottom (X %d Y %d Z %d)' % ( WF.topleft_X, WF.topleft_Y, WF.topleft_Z, WF.bottomright_X, WF.bottomright_Y, WF.bottomright_Z ) )

print("\nEnd")