

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
  topleft_X = 0
  topleft_Y = 0
  bottomright_X = 0
  bottomright_Y = 0
  
  def __init__(self):
    pass
  
  def add_well(self, arg_well ):
    self.Well_list.append( arg_well )
    if self.topleft_X > arg_well.wellhead_X:
      self.topleft_X = arg_well.wellhead_X
    if self.topleft_Y > arg_well.wellhead_Y:
      self.topleft_Y = arg_well.wellhead_Y
    if self.bottomright_X < arg_well.wellhead_X:
      self.bottomright_X = arg_well.wellhead_X
    if self.bottomright_Y < arg_well.wellhead_Y:
      self.bottomright_Y = arg_well.wellhead_Y
    
print("Start")

WF = WellField()

print( WF.topleft_X, WF.topleft_Y, WF.bottomright_X, WF.bottomright_Y )

WF.add_well( Well( 11, -7 ) )
WF.add_well( Well( -99, 88 ) )
WF.add_well( Well( 1, 1 ) )

for i in WF.Well_list:
  print (i.wellhead_X, i.wellhead_Y)

print( WF.topleft_X, WF.topleft_Y, WF.bottomright_X, WF.bottomright_Y )
  
print("End")
