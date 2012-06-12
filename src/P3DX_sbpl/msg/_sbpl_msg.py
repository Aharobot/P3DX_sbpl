"""autogenerated by genmsg_py from sbpl_msg.msg. Do not edit."""
import roslib.message
import struct


class sbpl_msg(roslib.message.Message):
  _md5sum = "c5e98ef0a5b021e3e77f5108ba25b386"
  _type = "P3DX_sbpl/sbpl_msg"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """bool sbpl_wait_flag
int8 sbpl_present_x
int8 sbpl_present_y
int8 sbpl_new_x
int8 sbpl_new_y
bool start_P3DX_motion

"""
  __slots__ = ['sbpl_wait_flag','sbpl_present_x','sbpl_present_y','sbpl_new_x','sbpl_new_y','start_P3DX_motion']
  _slot_types = ['bool','int8','int8','int8','int8','bool']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.
    
    The available fields are:
       sbpl_wait_flag,sbpl_present_x,sbpl_present_y,sbpl_new_x,sbpl_new_y,start_P3DX_motion
    
    @param args: complete set of field values, in .msg order
    @param kwds: use keyword arguments corresponding to message field names
    to set specific fields. 
    """
    if args or kwds:
      super(sbpl_msg, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.sbpl_wait_flag is None:
        self.sbpl_wait_flag = False
      if self.sbpl_present_x is None:
        self.sbpl_present_x = 0
      if self.sbpl_present_y is None:
        self.sbpl_present_y = 0
      if self.sbpl_new_x is None:
        self.sbpl_new_x = 0
      if self.sbpl_new_y is None:
        self.sbpl_new_y = 0
      if self.start_P3DX_motion is None:
        self.start_P3DX_motion = False
    else:
      self.sbpl_wait_flag = False
      self.sbpl_present_x = 0
      self.sbpl_present_y = 0
      self.sbpl_new_x = 0
      self.sbpl_new_y = 0
      self.start_P3DX_motion = False

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    @param buff: buffer
    @type  buff: StringIO
    """
    try:
      _x = self
      buff.write(_struct_B4bB.pack(_x.sbpl_wait_flag, _x.sbpl_present_x, _x.sbpl_present_y, _x.sbpl_new_x, _x.sbpl_new_y, _x.start_P3DX_motion))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    @param str: byte array of serialized message
    @type  str: str
    """
    try:
      end = 0
      _x = self
      start = end
      end += 6
      (_x.sbpl_wait_flag, _x.sbpl_present_x, _x.sbpl_present_y, _x.sbpl_new_x, _x.sbpl_new_y, _x.start_P3DX_motion,) = _struct_B4bB.unpack(str[start:end])
      self.sbpl_wait_flag = bool(self.sbpl_wait_flag)
      self.start_P3DX_motion = bool(self.start_P3DX_motion)
      return self
    except struct.error as e:
      raise roslib.message.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    @param buff: buffer
    @type  buff: StringIO
    @param numpy: numpy python module
    @type  numpy module
    """
    try:
      _x = self
      buff.write(_struct_B4bB.pack(_x.sbpl_wait_flag, _x.sbpl_present_x, _x.sbpl_present_y, _x.sbpl_new_x, _x.sbpl_new_y, _x.start_P3DX_motion))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    @param str: byte array of serialized message
    @type  str: str
    @param numpy: numpy python module
    @type  numpy: module
    """
    try:
      end = 0
      _x = self
      start = end
      end += 6
      (_x.sbpl_wait_flag, _x.sbpl_present_x, _x.sbpl_present_y, _x.sbpl_new_x, _x.sbpl_new_y, _x.start_P3DX_motion,) = _struct_B4bB.unpack(str[start:end])
      self.sbpl_wait_flag = bool(self.sbpl_wait_flag)
      self.start_P3DX_motion = bool(self.start_P3DX_motion)
      return self
    except struct.error as e:
      raise roslib.message.DeserializationError(e) #most likely buffer underfill

_struct_I = roslib.message.struct_I
_struct_B4bB = struct.Struct("<B4bB")
