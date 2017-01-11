from wells import *
  
from unittest import TestCase

class WellField_Test(TestCase):
    def test(self):
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

#print( WF.topleft_X, WF.topleft_Y, WF.bottomright_X, WF.bottomright_Y )


#for i in WF.Well_list:
#  print (i.wellhead_X, i.wellhead_Y)

#print( WF.topleft_X, WF.topleft_Y, WF.bottomright_X, WF.bottomright_Y )

MT=WellField_Test()
MT.test()
  
#print("End")