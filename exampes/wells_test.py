

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

    
print("Start")

BW = Well( 11, -7 )

WF = WellField()

WF.Well_list.append( BW )

for i in WF.Well_list:
  print (i.wellhead_X, i.wellhead_Y)

print("End")
