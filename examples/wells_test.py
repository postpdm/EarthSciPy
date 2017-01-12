from wells import *
  
from unittest import TestCase

class WellField_Test(TestCase):
    def test_well_coordinates(self):
      WF = WellField()

      WF.add_well( Well( 'well#1', 11, -7 ) )
      WF.add_well( Well( 'well#2', -99, 88, 1 ) )
      WF.add_well( Well( 'well#3', 1, 1 ) )
      WF.add_well( Well( 'well#4', 100, 100, -2 ) )

      self.assertEqual( WF.topleft_X, -99)
      self.assertEqual( WF.topleft_Y, -7)
      self.assertEqual( WF.topleft_Z, -2)
      self.assertEqual( WF.bottomright_X, 100)
      self.assertEqual( WF.bottomright_Y, 100)
      self.assertEqual( WF.bottomright_Z, 1)
    
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
      self.assertEqual( W.geometry[-1].start_lenght, 32 )
    
print("Test started")
MT=WellField_Test()
MT.test_well_coordinates()
MT.test_well_inclination()
  
print("Test ended")