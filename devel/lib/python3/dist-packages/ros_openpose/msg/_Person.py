# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from ros_openpose/Person.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg
import ros_openpose.msg

class Person(genpy.Message):
  _md5sum = "5cbfeaba995a09efdb2c52e51374390b"
  _type = "ros_openpose/Person"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """# A person has some body parts. That is why we have created
# an array of body parts.
BodyPart[] bodyParts
BodyPart[] leftHandParts
BodyPart[] rightHandParts

================================================================================
MSG: ros_openpose/BodyPart
# The location and score of body parts are stored in a float array.
# Therefore we are using 32 bits instead of 64 bits.
# src: https://github.com/CMU-Perceptual-Computing-Lab/openpose/blob/master/include/openpose/core/datum.hpp
float32 score
Pixel pixel
geometry_msgs/Point32 point

================================================================================
MSG: ros_openpose/Pixel
# The location and score of body parts are stored in a float array.
# Therefore we are using 32 bits instead of 64 bits.
# src: https://github.com/CMU-Perceptual-Computing-Lab/openpose/blob/master/include/openpose/core/datum.hpp
# The location has been resized to the desired output
# resolution (e.g., `resolution` flag in the demo).
float32 x
float32 y

================================================================================
MSG: geometry_msgs/Point32
# This contains the position of a point in free space(with 32 bits of precision).
# It is recommeded to use Point wherever possible instead of Point32.  
# 
# This recommendation is to promote interoperability.  
#
# This message is designed to take up less space when sending
# lots of points at once, as in the case of a PointCloud.  

float32 x
float32 y
float32 z"""
  __slots__ = ['bodyParts','leftHandParts','rightHandParts']
  _slot_types = ['ros_openpose/BodyPart[]','ros_openpose/BodyPart[]','ros_openpose/BodyPart[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       bodyParts,leftHandParts,rightHandParts

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(Person, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.bodyParts is None:
        self.bodyParts = []
      if self.leftHandParts is None:
        self.leftHandParts = []
      if self.rightHandParts is None:
        self.rightHandParts = []
    else:
      self.bodyParts = []
      self.leftHandParts = []
      self.rightHandParts = []

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      length = len(self.bodyParts)
      buff.write(_struct_I.pack(length))
      for val1 in self.bodyParts:
        _x = val1.score
        buff.write(_get_struct_f().pack(_x))
        _v1 = val1.pixel
        _x = _v1
        buff.write(_get_struct_2f().pack(_x.x, _x.y))
        _v2 = val1.point
        _x = _v2
        buff.write(_get_struct_3f().pack(_x.x, _x.y, _x.z))
      length = len(self.leftHandParts)
      buff.write(_struct_I.pack(length))
      for val1 in self.leftHandParts:
        _x = val1.score
        buff.write(_get_struct_f().pack(_x))
        _v3 = val1.pixel
        _x = _v3
        buff.write(_get_struct_2f().pack(_x.x, _x.y))
        _v4 = val1.point
        _x = _v4
        buff.write(_get_struct_3f().pack(_x.x, _x.y, _x.z))
      length = len(self.rightHandParts)
      buff.write(_struct_I.pack(length))
      for val1 in self.rightHandParts:
        _x = val1.score
        buff.write(_get_struct_f().pack(_x))
        _v5 = val1.pixel
        _x = _v5
        buff.write(_get_struct_2f().pack(_x.x, _x.y))
        _v6 = val1.point
        _x = _v6
        buff.write(_get_struct_3f().pack(_x.x, _x.y, _x.z))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.bodyParts is None:
        self.bodyParts = None
      if self.leftHandParts is None:
        self.leftHandParts = None
      if self.rightHandParts is None:
        self.rightHandParts = None
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.bodyParts = []
      for i in range(0, length):
        val1 = ros_openpose.msg.BodyPart()
        start = end
        end += 4
        (val1.score,) = _get_struct_f().unpack(str[start:end])
        _v7 = val1.pixel
        _x = _v7
        start = end
        end += 8
        (_x.x, _x.y,) = _get_struct_2f().unpack(str[start:end])
        _v8 = val1.point
        _x = _v8
        start = end
        end += 12
        (_x.x, _x.y, _x.z,) = _get_struct_3f().unpack(str[start:end])
        self.bodyParts.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.leftHandParts = []
      for i in range(0, length):
        val1 = ros_openpose.msg.BodyPart()
        start = end
        end += 4
        (val1.score,) = _get_struct_f().unpack(str[start:end])
        _v9 = val1.pixel
        _x = _v9
        start = end
        end += 8
        (_x.x, _x.y,) = _get_struct_2f().unpack(str[start:end])
        _v10 = val1.point
        _x = _v10
        start = end
        end += 12
        (_x.x, _x.y, _x.z,) = _get_struct_3f().unpack(str[start:end])
        self.leftHandParts.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.rightHandParts = []
      for i in range(0, length):
        val1 = ros_openpose.msg.BodyPart()
        start = end
        end += 4
        (val1.score,) = _get_struct_f().unpack(str[start:end])
        _v11 = val1.pixel
        _x = _v11
        start = end
        end += 8
        (_x.x, _x.y,) = _get_struct_2f().unpack(str[start:end])
        _v12 = val1.point
        _x = _v12
        start = end
        end += 12
        (_x.x, _x.y, _x.z,) = _get_struct_3f().unpack(str[start:end])
        self.rightHandParts.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      length = len(self.bodyParts)
      buff.write(_struct_I.pack(length))
      for val1 in self.bodyParts:
        _x = val1.score
        buff.write(_get_struct_f().pack(_x))
        _v13 = val1.pixel
        _x = _v13
        buff.write(_get_struct_2f().pack(_x.x, _x.y))
        _v14 = val1.point
        _x = _v14
        buff.write(_get_struct_3f().pack(_x.x, _x.y, _x.z))
      length = len(self.leftHandParts)
      buff.write(_struct_I.pack(length))
      for val1 in self.leftHandParts:
        _x = val1.score
        buff.write(_get_struct_f().pack(_x))
        _v15 = val1.pixel
        _x = _v15
        buff.write(_get_struct_2f().pack(_x.x, _x.y))
        _v16 = val1.point
        _x = _v16
        buff.write(_get_struct_3f().pack(_x.x, _x.y, _x.z))
      length = len(self.rightHandParts)
      buff.write(_struct_I.pack(length))
      for val1 in self.rightHandParts:
        _x = val1.score
        buff.write(_get_struct_f().pack(_x))
        _v17 = val1.pixel
        _x = _v17
        buff.write(_get_struct_2f().pack(_x.x, _x.y))
        _v18 = val1.point
        _x = _v18
        buff.write(_get_struct_3f().pack(_x.x, _x.y, _x.z))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.bodyParts is None:
        self.bodyParts = None
      if self.leftHandParts is None:
        self.leftHandParts = None
      if self.rightHandParts is None:
        self.rightHandParts = None
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.bodyParts = []
      for i in range(0, length):
        val1 = ros_openpose.msg.BodyPart()
        start = end
        end += 4
        (val1.score,) = _get_struct_f().unpack(str[start:end])
        _v19 = val1.pixel
        _x = _v19
        start = end
        end += 8
        (_x.x, _x.y,) = _get_struct_2f().unpack(str[start:end])
        _v20 = val1.point
        _x = _v20
        start = end
        end += 12
        (_x.x, _x.y, _x.z,) = _get_struct_3f().unpack(str[start:end])
        self.bodyParts.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.leftHandParts = []
      for i in range(0, length):
        val1 = ros_openpose.msg.BodyPart()
        start = end
        end += 4
        (val1.score,) = _get_struct_f().unpack(str[start:end])
        _v21 = val1.pixel
        _x = _v21
        start = end
        end += 8
        (_x.x, _x.y,) = _get_struct_2f().unpack(str[start:end])
        _v22 = val1.point
        _x = _v22
        start = end
        end += 12
        (_x.x, _x.y, _x.z,) = _get_struct_3f().unpack(str[start:end])
        self.leftHandParts.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.rightHandParts = []
      for i in range(0, length):
        val1 = ros_openpose.msg.BodyPart()
        start = end
        end += 4
        (val1.score,) = _get_struct_f().unpack(str[start:end])
        _v23 = val1.pixel
        _x = _v23
        start = end
        end += 8
        (_x.x, _x.y,) = _get_struct_2f().unpack(str[start:end])
        _v24 = val1.point
        _x = _v24
        start = end
        end += 12
        (_x.x, _x.y, _x.z,) = _get_struct_3f().unpack(str[start:end])
        self.rightHandParts.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2f = None
def _get_struct_2f():
    global _struct_2f
    if _struct_2f is None:
        _struct_2f = struct.Struct("<2f")
    return _struct_2f
_struct_3f = None
def _get_struct_3f():
    global _struct_3f
    if _struct_3f is None:
        _struct_3f = struct.Struct("<3f")
    return _struct_3f
_struct_f = None
def _get_struct_f():
    global _struct_f
    if _struct_f is None:
        _struct_f = struct.Struct("<f")
    return _struct_f
