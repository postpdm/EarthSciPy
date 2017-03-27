from earthscipy.wells import *
  
from unittest import TestCase

from math import fabs, sqrt

# We do not much care about trigonometry precision. Underground measurements is not so accurate
PERMISSIBLE_VARIATION_VALUE = 0.000001

PERMISSIBLE_VARIATION_VALUE_ROUGH = 0.01

class WellField_Test(TestCase):
    def test_StaticDot3D(self):
        s = StaticDot3D( 1, 2, 3 )
        self.assertEqual( s.X, 1 )
        self.assertEqual( s.Y, 2 )
        self.assertEqual( s.Z, 3 )
    
    def test_WellGeometryStepX_0( self ):
        WGS = WellGeometryStep( StaticDot3D( 0, 0, 0 ), 10 )
        self.assertEqual( WGS.end_dot.X, 10 )
        
    def test_WellGeometryStepY_0( self ):
        WGS = WellGeometryStep( StaticDot3D( 0, 0, 0 ), 10 )
        self.assertEqual( WGS.end_dot.Y, 0 )
        
    def test_WellGeometryStepZ_0( self ):
        WGS = WellGeometryStep( StaticDot3D( 0, 0, 0 ), 10 )
        self.assertEqual( WGS.end_dot.Z, 0 )

    def test_WellGeometryStepX_45( self ):
        WGS = WellGeometryStep( StaticDot3D( 0, 0, 0 ), 10, 45 )
        self.assertTrue( fabs( fabs( WGS.end_dot.X ) - 7.0710687 ) < PERMISSIBLE_VARIATION_VALUE )
        
    def test_WellGeometryStepY_45( self ):
        WGS = WellGeometryStep( StaticDot3D( 0, 0, 0 ), 10, 45 )
        self.assertTrue( fabs( fabs( WGS.end_dot.Y ) - 7.0710687 ) < PERMISSIBLE_VARIATION_VALUE )
        
    def test_WellGeometryStepZ_45( self ):
        WGS = WellGeometryStep( StaticDot3D( 0, 0, 0 ), 10, 45 )
        self.assertEqual( WGS.end_dot.Z, 0 )
        
    def test_WellGeometryStepX_90( self ):
        WGS = WellGeometryStep( StaticDot3D( 0, 0, 0 ), 10, 90 )
        self.assertTrue( fabs( WGS.end_dot.X ) < PERMISSIBLE_VARIATION_VALUE )
        
    def test_WellGeometryStepY_90( self ):
        WGS = WellGeometryStep( StaticDot3D( 0, 0, 0 ), 10, 90 )
        self.assertEqual( WGS.end_dot.Y, 10 )
        
    def test_WellGeometryStepZ_90( self ):
        WGS = WellGeometryStep( StaticDot3D( 0, 0, 0 ), 10, 90 )
        self.assertEqual( WGS.end_dot.Z, 0 )
        
    def test_WellGeometryStepX_5_2( self ):
        WGS = WellGeometryStep( StaticDot3D( 0, 0, 0 ), 10, 5, 2 )
        self.assertTrue( fabs( fabs( WGS.end_dot.X ) - 9.955878 ) < PERMISSIBLE_VARIATION_VALUE )
    
    def test_WellGeometryStepY_5_2( self ):
        WGS = WellGeometryStep( StaticDot3D( 0, 0, 0 ), 10, 5, 2 )
        self.assertTrue( fabs( fabs( WGS.end_dot.Y ) - 0.871026 ) < PERMISSIBLE_VARIATION_VALUE )
        
    def test_WellGeometryStepZ_5_2( self ):
        WGS = WellGeometryStep( StaticDot3D( 0, 0, 0 ), 10, 5, 2 )
        self.assertTrue( fabs( fabs( WGS.end_dot.Z ) - 0.348994 ) < PERMISSIBLE_VARIATION_VALUE )

    def test_well_coordinates(self):
      WF = WellField("_")

      WF.add_well( Well( 'well#1', 11, -7 ) )
      WF.add_well( Well( 'well#2', -99, 88, 1 ) )
      WF.add_well( Well( 'well#3', 1, 1 ) )
      WF.add_well( Well( 'well#4', 100, 100, -2 ) )

      self.assertEqual( WF.topleft.X, -99)
      self.assertEqual( WF.topleft.Y, -7)
      self.assertEqual( WF.topleft.Z, -2)
      self.assertEqual( WF.bottomright.X, 100)
      self.assertEqual( WF.bottomright.Y, 100)
      self.assertEqual( WF.bottomright.Z, 1)
    
    def test_well_field_mutable(self):
      # WellField contain mutable lists. Test it's not shared
      WF_1 = WellField("1")
      WF_2 = WellField("2")
      WF_1.add_well( Well( 'well#1', 0, 0 ) )
      self.assertEqual( len( WF_1.Well_list ), 1 ) # because we has add well to a first field
      self.assertEqual( len( WF_2.Well_list ), 0 ) # because we hasn't add well to a second field
    
    def test_well_mutable(self):
      # Well contain mutable lists. Test it's not shared
      W_1 = Well("well#1", 0, 0 )
      W_2 = Well("well#2", 0, 0)
      W_1.add_geometry_step( 10 )
      self.assertEqual( len( W_1.geometry ), 1 ) # because we has add inclinometry step to a first well
      self.assertEqual( len( W_2.geometry ), 0 ) # because we hasn't add inclinometry step to a second well
    
    def test_well_inclination(self):
      W = Well( 'test well', 1, 1, 1 )
      self.assertEqual( W.well_length, 0 )
      W.add_geometry_step( 10 )
      self.assertEqual( W.well_length, 10 )
      W.add_geometry_step( 10 )
      self.assertEqual( W.well_length, 20 )
      W.add_geometry_step( 12 )
      self.assertEqual( W.well_length, 32 )
      W.add_geometry_step( 12 )
      self.assertEqual( W.well_length, 44 )
      self.assertEqual( W.geometry[-1].start_length, 32 )
    
    def test_well_inclination_circle_X(self):
      # ths couldn't be in real life
      W1 = Well( 'test well', 0, 0, 0 )
      W1.add_geometry_step( 10, 0, 0 )
      W1.add_geometry_step( 10, 90, 0 )
      W1.add_geometry_step( 10, 180, 0 )
      W1.add_geometry_step( 10, 270, 0 )
     
      self.assertEqual( W1.well_length, 40 )
      self.assertTrue( fabs( W1.End_Dot().X ) < PERMISSIBLE_VARIATION_VALUE )
      
    def test_well_inclination_circle_XY(self):
      # ths couldn't be in real life
      W1 = Well( 'test well', 0, 0, 0 )
      W1.add_geometry_step( 10, 0, 0 )
      W1.add_geometry_step( 10, 90, 0 )
      W1.add_geometry_step( 10, 180, 0 )
      W1.add_geometry_step( 10, 270, 0 )
     
      self.assertEqual( W1.well_length, 40 )
      self.assertTrue( fabs( W1.End_Dot().X ) < PERMISSIBLE_VARIATION_VALUE )
      self.assertTrue( fabs( W1.End_Dot().Y ) < PERMISSIBLE_VARIATION_VALUE )

    def test_well_inclination_50steps(self):
      W1 = Well( 'test well', 0, 0, 0 )
      for i in range(0, 50):
        W1.add_geometry_step( 10, 11, -7 )
        W1.add_geometry_step( 10, -11, 7 )      
      
      self.assertEqual( W1.End_Dot().Y, 0 )
      self.assertEqual( W1.End_Dot().Z, 0 )
      self.assertTrue( W1.End_Dot().X < W1.well_length )
      
      self.assertEqual( W1.well_length, 1000 )
      
    def test_well_inclination_drill_small_cube(self):
      W1 = Well( 'test well 1', 0, 0, 0 )
      W1.add_geometry_step( sqrt(3), 45, 35.5 ) #  it sould be a cube with 1m edges
            
      self.assertTrue( fabs( 1 - W1.End_Dot().X ) < PERMISSIBLE_VARIATION_VALUE_ROUGH )
      self.assertTrue( fabs( 1 - W1.End_Dot().Y ) < PERMISSIBLE_VARIATION_VALUE_ROUGH )
      self.assertTrue( fabs( 1 - W1.End_Dot().Z ) < PERMISSIBLE_VARIATION_VALUE_ROUGH )      
      
      self.assertEqual( sqrt( ( W1.End_Dot().X * W1.End_Dot().X ) + ( W1.End_Dot().Y * W1.End_Dot().Y ) + ( W1.End_Dot().Z * W1.End_Dot().Z ) ), sqrt(3) )

    def test_well_inclination_drill_small_cuboid(self):
      W1 = Well( 'test well 1', 0, 0, 0 )
      W1.add_geometry_step( sqrt(1+4+9), 56.309932474, 15.5013595669 ) #  it sould be a cuboid with 1-2-3m edges
            
      self.assertTrue( fabs( 2 - W1.End_Dot().X ) < PERMISSIBLE_VARIATION_VALUE_ROUGH )
      self.assertTrue( fabs( 3 - W1.End_Dot().Y ) < PERMISSIBLE_VARIATION_VALUE_ROUGH )
      self.assertTrue( fabs( 1 - W1.End_Dot().Z ) < PERMISSIBLE_VARIATION_VALUE_ROUGH )      
      
      self.assertTrue( fabs( sqrt( ( W1.End_Dot().X * W1.End_Dot().X ) + ( W1.End_Dot().Y * W1.End_Dot().Y ) + ( W1.End_Dot().Z * W1.End_Dot().Z ) ) - sqrt(1+4+9) ) < PERMISSIBLE_VARIATION_VALUE )
      
    def test_well_inclination_drill_big_cube(self):
      W1 = Well( 'test well 1', 0, 0, 0 )
      W1.add_geometry_step( 1000, 17, 9 )
      
      W2 = Well( 'test well 2', 0, 0, 0 )
      for i in range(0, 100):
        W2.add_geometry_step( 10, 17, 9 )      
      
      self.assertTrue( fabs( W1.End_Dot().X - W2.End_Dot().X ) < PERMISSIBLE_VARIATION_VALUE )
      self.assertTrue( fabs( W1.End_Dot().Y - W2.End_Dot().Y ) < PERMISSIBLE_VARIATION_VALUE )
      self.assertTrue( fabs( W1.End_Dot().Z - W2.End_Dot().Z ) < PERMISSIBLE_VARIATION_VALUE )
      