class BaseWell():
  """Base well class"""
  wellname = ''
  
  wellhead_X = 0
  wellhead_Y = 0
  wellhead_Z = 0
  
  Geometry = []
  
  def __init__(self, arg_wellname = '', arg_wellhead_X = 0, arg_wellhead_Y = 0, arg_wellhead_Z = 0 ):
    self.wellname = arg_wellname
    self.wellhead_X = arg_wellhead_X
    self.wellhead_Y = arg_wellhead_Y
    self.wellhead_Z = arg_wellhead_Z
   
class Well(BaseWell):
  """Well class"""
  #def __init__(self):
  #  pass

class WellField():
  """Well field class"""
  Well_list = []
  topleft_X = 0
  topleft_Y = 0
  topleft_Z = 0
  bottomright_X = 0
  bottomright_Y = 0
  bottomright_Z = 0
  
  def __init__(self):
    pass
  
  def add_well( self, arg_well ):
    # append well to list
    self.Well_list.append( arg_well )
    # recalculate field size
    if self.topleft_X > arg_well.wellhead_X:
      self.topleft_X = arg_well.wellhead_X
    if self.topleft_Y > arg_well.wellhead_Y:
      self.topleft_Y = arg_well.wellhead_Y
    if self.topleft_Z > arg_well.wellhead_Z:
      self.topleft_Z = arg_well.wellhead_Z
    
    if self.bottomright_X < arg_well.wellhead_X:
      self.bottomright_X = arg_well.wellhead_X
    if self.bottomright_Y < arg_well.wellhead_Y:
      self.bottomright_Y = arg_well.wellhead_Y
    if self.bottomright_Z < arg_well.wellhead_Z:
      self.bottomright_Z = arg_well.wellhead_Z