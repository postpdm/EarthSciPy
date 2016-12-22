

class BaseWell():
  """Base well class"""
  wellhead_X = 0
  wellhead_Y = 0
  
  def __init__(self, arg_wellhead_X = 0, arg_wellhead_Y = 0 ):
    self.wellhead_X = arg_wellhead_X
    self.wellhead_Y = arg_wellhead_Y    
   
class Well(BaseWell):
  """Well class"""
  #def __init__(self):
  #  print("Well")
  #  print( self.wellhead_X, self.wellhead_Y )

class WellField():
  """Well field class"""
  Well_list = []
  def __init__(self):
    pass
  
  def add_well(self, arg_well ):
    self.Well_list.append( arg_well )
    
print("Start")

WF = WellField()

WF.add_well( Well( 11, -7 ) )
WF.add_well( Well( -99, 88 ) )

for i in WF.Well_list:
  print (i.wellhead_X, i.wellhead_Y)

print("End")
