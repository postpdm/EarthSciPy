from math import cos, radians

class WellGeometryStep():
  """One step of clinometry data"""
  # consts from incliomerty
  inclination = 0 # in metres
  tangent = 0     # in degrees
  vertical = 0    # in degrees
  
  # calculable length 
  start_lenght = 0
  
  # calculable end point coordinates
  end_X = 0
  end_Y = 0
  end_Z = 0
  
  def __init__(self, arg_prev_step, arg_inclination, arg_tangent = 0, arg_vertical = 0, arg_start_lenght = 0 ): # no default value for arg_inclination
    self.inclination = arg_inclination
    self.tangent     = arg_tangent
    self.vertical    = arg_vertical
    
    self.start_lenght = arg_start_lenght
    if not arg_prev_step is None:
      self.end_X = arg_prev_step.end_X
      self.end_Y = arg_prev_step.end_Y
      self.end_Z = arg_prev_step.end_Z

    # first primitive variant
    self.end_X =+ arg_inclination * cos( radians( self.tangent ) )
    self.end_Y =+ arg_inclination * cos( radians( self.tangent ) )
    self.end_Z =+ arg_inclination * cos( radians( self.vertical ) )

class BaseWell():
  """Base well class"""
  wellname = ''
  
  wellhead_X = 0
  wellhead_Y = 0
  wellhead_Z = 0
  
  geometry = []
  
  well_length = 0
  
  def __init__(self, arg_wellname = '', arg_wellhead_X = 0, arg_wellhead_Y = 0, arg_wellhead_Z = 0 ):
    self.wellname = arg_wellname
    self.wellhead_X = arg_wellhead_X
    self.wellhead_Y = arg_wellhead_Y
    self.wellhead_Z = arg_wellhead_Z
    
  def add_geometry_step(self, arg_inclination, arg_tangent = 0, arg_vertical = 0 ): # no default value for arg_inclination    
    prev_step = None
    if len( self.geometry ) > 0:
      prev_step = self.geometry[-1]
    self.geometry.append( WellGeometryStep( prev_step, arg_inclination, arg_tangent, arg_vertical, self.well_length ) )
    self.well_length+=arg_inclination
   
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
