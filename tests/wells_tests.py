from earthscipy.wells import *
  
from unittest import TestCase

class WellField_Test(TestCase):
    def test_StaticDot3D(self):
        s = StaticDot3D( 1, 2, 3 )
        self.assertEqual( s.X, 1 )
        self.assertEqual( s.Y, 2 )
        self.assertEqual( s.Z, 3 )
    
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
    
    def test_well_inclination_circle(self):
      W1 = Well( 'test well', 0, 0, 0 )
      W1.add_geometry_step( 10, 0, 0 )
      self.assertEqual( W1.well_length, 10 )
      #self.assertEqual( W1.geometry[-1].end_X, 10 )
      
      # W1.add_geometry_step( 1, 0, 0 ) 

      # ??????????????
      # print( W1.geometry[-1].end_X, W1.geometry[-1].end_Y, W1.geometry[-1].end_Z )
      # W1.add_geometry_step( 10, 0, 0 )
      # print( W1.geometry[-1].end_X )
      # W1.add_geometry_step( 10, 0, 0 )
      # print( W1.geometry[-1].end_X )
      # W1.add_geometry_step( 10, 0, 0 )
      # print( W1.geometry[-1].end_X )
