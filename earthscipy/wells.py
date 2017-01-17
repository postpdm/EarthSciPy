from math import cos, sin, radians

class StaticDot3D: 
  """3D coordinates for dot"""
  X = 0
  Y = 0
  Z = 0
  
  def __init__(self, arg_X, arg_Y, arg_Z ):
    self.X = arg_X
    self.Y = arg_Y
    self.Z = arg_Z

class WellGeometryStep():
  """One step of clinometry data"""
  # consts from incliomerty
  inclination = 0 # in metres
  tangent = 0     # in degrees
  vertical = 0    # in degrees
  
  # calculable length 
  start_lenght = 0
  
  # calculable end point coordinates
  end_dot = None # type StaticDot3D
  
  def __init__(self, arg_start_dot, arg_inclination, arg_tangent = 0, arg_vertical = 0, arg_start_lenght = 0 ): # no default value for arg_inclination
    # store inclination vector
    self.inclination = arg_inclination
    self.tangent     = arg_tangent
    self.vertical    = arg_vertical
    # store start lengtt
    self.start_lenght = arg_start_lenght
    
    # calculate end dot coordinates
    self.end_dot = StaticDot3D( arg_start_dot.X, arg_start_dot.Y, arg_start_dot.Z )
    # first primitive variant    
    self.end_dot.X += arg_inclination * cos( radians( self.tangent ) )
    self.end_dot.Y += arg_inclination * sin( radians( self.tangent ) )
    self.end_dot.Z += arg_inclination * cos( radians( self.vertical ) )

class BaseWell():
  """Base well class"""
  wellname = ''
  
  wellhead = None # StaticDot3D
  
  # geometry - list of WellGeometryStep

  well_length = 0
  
  def __init__(self, arg_wellname = '', arg_wellhead_X = 0, arg_wellhead_Y = 0, arg_wellhead_Z = 0 ):
    self.geometry = []
    self.wellname = arg_wellname    
    self.wellhead = StaticDot3D( arg_wellhead_X, arg_wellhead_Y, arg_wellhead_Z )
    
  def add_geometry_step(self, arg_inclination, arg_tangent = 0, arg_vertical = 0 ): # no default value for arg_inclination    
    prev_dot = None # StaticDot3D
    # if well has a geometry - use last step. Else use the wellhead dot
    if len( self.geometry ) > 0:
      prev_dot = self.geometry[-1].end_dot
    else:
      prev_dot = self.wellhead      
      
    # add step
    self.geometry.append( WellGeometryStep( prev_dot, arg_inclination, arg_tangent, arg_vertical, self.well_length ) )
    # inc the well length
    self.well_length+=arg_inclination
   
class Well(BaseWell):
  """Well class"""
  #def __init__(self):
  #  pass

datums = [ 'Baltic', 'NAD27', 'NAD83', 'Ordnance Datum Newlyn', 'Normalhöhennull', 'ETRS1989', 'AOD', 'TUDKA-99' ]
  
class WellField():
  """Well field class"""
  # Well_list - list of wells
  field_name = ''
  
  topleft = StaticDot3D( 0, 0, 0 )
  bottomright = StaticDot3D( 0, 0, 0 )
  
  def __init__(self, arg_field_name):
    self.Well_list = []
    self.field_name = arg_field_name
  
  def add_well( self, arg_well ):
    # append well to list
    self.Well_list.append( arg_well )
    # recalculate field size
    if self.topleft.X > arg_well.wellhead.X:
      self.topleft.X = arg_well.wellhead.X
    if self.topleft.Y > arg_well.wellhead.Y:
      self.topleft.Y = arg_well.wellhead.Y
    if self.topleft.Z > arg_well.wellhead.Z:
      self.topleft.Z = arg_well.wellhead.Z
    
    if self.bottomright.X < arg_well.wellhead.X:
      self.bottomright.X = arg_well.wellhead.X
    if self.bottomright.Y < arg_well.wellhead.Y:
      self.bottomright.Y = arg_well.wellhead.Y
    if self.bottomright.Z < arg_well.wellhead.Z:
      self.bottomright.Z = arg_well.wellhead.Z