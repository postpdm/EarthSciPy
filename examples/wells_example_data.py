from earthscipy.wells import *
  
def Create_WellField_North():
    # Create well field
    WF = WellField( "North" )
    # add some well to field
    WF.add_well( Well( 'N_well#1', 11, -7 ) )
    WF.add_well( Well( 'N_well#3', 1, 1 ) )
    WF.add_well( Well( 'N_well#4', 100, 100, -2 ) )
    w = Well( 'N_well#5', 0, 0 )
    w.add_geometry_step( 10, 0 )
    w.add_geometry_step( 10, 45 )
    w.add_geometry_step( 10, 90 )
    w.add_geometry_step( 100, 0 )
    WF.add_well( w )

    WF.add_well( Well( 'N_well#6', -99, 88, 1 ) )

    w1 = Well( 'N_well#9', -100, -100 )
    w1.add_geometry_step( 1, 0 )
    WF.add_well( w1 )
    
    return WF

def Create_WellField_South():
    WF = WellField("South")
    WF.add_well( Well( 'S_well#1', 11, -7 ) )
    
    return WF