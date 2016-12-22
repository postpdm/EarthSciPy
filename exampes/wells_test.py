

class BaseWell():
  """Base well class"""
  wellhead_X = 0
  wellhead_Y = 0
  
  def __init__(self):
    pass
   
class Well(BaseWell):
  """Well class"""
  def __init__(self):
    print("Well")
    print( self.wellhead_X, self.wellhead_Y )
    
print("Start")

BW = Well()

print("End")
