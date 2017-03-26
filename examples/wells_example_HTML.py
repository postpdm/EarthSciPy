from earthscipy.wells import *
  
from wells_example_data import Create_WellField_North, Create_WellField_South
  
WF_N = Create_WellField_North()

WF_S = Create_WellField_South()

print( '<h1>Testing</h1>' )
#print('<h2>print out the list of wells</h2>')

for wf in [ WF_N, WF_S, ]:
  print( "<h2>Field", wf.field_name, "</h2>" )
  print( '<table border="2">' )
  print('<tr><th>Well</th><th>Well head</th><th>Well length</th><th>Geometry data</th></tr>')
  for i in wf.Well_list:
    print('<tr>')
    print( '<td>Well', i.wellname, '</td>' )
    print( '<td>' )
    print ( 'X %+5d Y %+5d Z %+5d' % ( i.wellhead.X, i.wellhead.Y, i.wellhead.Z ) )
    print( '</td>' )
    print( '<td>' )
    print ( 'well_length %d' % ( i.well_length ) )
    #print('\nprint out the geometry data for well', i.wellname )
    print('</td>')
    print( '<td>' )
    print('<table border="1">')
    print('<tr><th>Inclination</th><th>Vertical</th><th>Targent</th><th>Start length</th><th>End point X Y Z </th></tr>')
    for s in i.geometry:
      print('<tr>')
      print('<td>')
      print('%.1f' % ( s.inclination ) )
      print('</td>')
      print( '<td>%.2f.</td>' % ( s.vertical ) )
      print( '<td>%.2f.</td>' % ( s.tangent ) )
      print( '<td>%.2f.</td>' % ( s.start_length ) )
      print( '<td>%.2f, %.2f, %.2f</td>' % ( s.end_dot.X, s.end_dot.Y, s.end_dot.Z ) )
      print('</tr>')
    print('</table>')    
    print( '</td>' )
    print('</tr>')
  print( '</table>' )
  print ( '<p>field size top (X %d Y %d Z %d) bottom (X %d Y %d Z %d)' % ( wf.topleft.X, wf.topleft.Y, wf.topleft.Z, wf.bottomright.X, wf.bottomright.Y, wf.bottomright.Z ), '</p>' )

print("\nEnd")
