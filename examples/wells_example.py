from earthscipy.wells import *
  
print("Start")

WF1 = WellField( "North" )
WF1.add_well( Well( 'N_well#1', 11, -7 ) )
WF1.add_well( Well( 'N_well#3', 1, 1 ) )
WF1.add_well( Well( 'N_well#4', 100, 100, -2 ) )
w = Well( 'N_well#5', 0, 0 )
w.add_geometry_step( 10, 0 )
w.add_geometry_step( 10, 45 )
w.add_geometry_step( 10, 90 )
w.add_geometry_step( 100, 0 )
WF1.add_well( w )

WF1.add_well( Well( 'N_well#6', -99, 88, 1 ) )

w1 = Well( 'N_well#9', -100, -100 )
w1.add_geometry_step( 1, 0 )
WF1.add_well( w1 )

WF2 = WellField("South")
WF2.add_well( Well( 'S_well#1', 11, -7 ) )

print('\nprint out the list of wells')

for wf in [ WF1, WF2, ]:
  print( "\nField", wf.field_name )
  for i in wf.Well_list:
    print( '\nWell', i.wellname )
    print ( 'wellhead X %+5d Y %+5d Z %+5d   well_length %d' % ( i.wellhead.X, i.wellhead.Y, i.wellhead.Z, i.well_length ) )
    print('\nprint out the geometry data for well', i.wellname )
    for s in i.geometry:
      print( 'Inclination %.1f tangent %.1f vertical %.1f. Start lenght %.1f. End point X Y Z (%.1f, %.1f, %.1f)' % 
             ( s.inclination, s.tangent, s.vertical, s.start_lenght,
               s.end_dot.X, s.end_dot.Y, s.end_dot.Z ) )
  print ( '\nfield size top (X %d Y %d Z %d) bottom (X %d Y %d Z %d)' % ( wf.topleft.X, wf.topleft.Y, wf.topleft.Z, wf.bottomright.X, wf.bottomright.Y, wf.bottomright.Z ) )

print("\nEnd")