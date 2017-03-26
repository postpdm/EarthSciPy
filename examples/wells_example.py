from earthscipy.wells import *
from wells_example_data import Create_WellField_North, Create_WellField_South
  
WF_N = Create_WellField_North()

WF_S = Create_WellField_South()

print('\nprint out the list of wells')

for wf in [ WF_N, WF_S, ]:
  print( "\nField", wf.field_name )
  for i in wf.Well_list:
    print( '\nWell', i.wellname )
    print ( 'wellhead X %+5d Y %+5d Z %+5d   well_length %d' % ( i.wellhead.X, i.wellhead.Y, i.wellhead.Z, i.well_length ) )
    print('\nprint out the geometry data for well', i.wellname )
    for s in i.geometry:
        print( 'Inclination %.1f tangent %.1f vertical %.1f. Start length %.1f. End point X Y Z (%.1f, %.1f, %.1f)' % ( s.inclination, s.tangent, s.vertical, s.start_length, s.end_dot.X, s.end_dot.Y, s.end_dot.Z ) )
  print ( '\nfield size top (X %d Y %d Z %d) bottom (X %d Y %d Z %d)' % ( wf.topleft.X, wf.topleft.Y, wf.topleft.Z, wf.bottomright.X, wf.bottomright.Y, wf.bottomright.Z ) )

print("\nEnd")