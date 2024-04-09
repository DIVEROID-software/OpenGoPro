"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
*
Defines the structure of protobuf messages for setting camera control status
"""

import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions
DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _EnumCameraControlStatus:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _EnumCameraControlStatusEnumTypeWrapper(
    google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_EnumCameraControlStatus.ValueType],
    builtins.type,
):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    CAMERA_IDLE: _EnumCameraControlStatus.ValueType
    CAMERA_CONTROL: _EnumCameraControlStatus.ValueType
    "Can only be set by camera, not by app or third party"
    CAMERA_EXTERNAL_CONTROL: _EnumCameraControlStatus.ValueType

class EnumCameraControlStatus(_EnumCameraControlStatus, metaclass=_EnumCameraControlStatusEnumTypeWrapper): ...

CAMERA_IDLE: EnumCameraControlStatus.ValueType
CAMERA_CONTROL: EnumCameraControlStatus.ValueType
"Can only be set by camera, not by app or third party"
CAMERA_EXTERNAL_CONTROL: EnumCameraControlStatus.ValueType
global___EnumCameraControlStatus = EnumCameraControlStatus

@typing_extensions.final
class RequestSetCameraControlStatus(google.protobuf.message.Message):
    """*
    Set Camera Control Status (as part of Global Behaviors feature)

    This command is used to tell the camera that the app (i.e. External Control) wishes to claim control of the camera.
    This causes the camera to immediately exit most contextual menus and return to the idle screen. Any interaction with
    the camera's physical buttons will cause the camera to reclaim control and update control status accordingly. If the
    user returns the camera UI to the idle screen, the camera updates control status to Idle.

    The entity currently claiming control of the camera is advertised in camera status 114. Information about whether the
    camera is in a contextual menu or not is advertised in camera status 63.

    Response: @ref ResponseGeneric
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CAMERA_CONTROL_STATUS_FIELD_NUMBER: builtins.int
    camera_control_status: global___EnumCameraControlStatus.ValueType
    "Declare who is taking control of the camera"

    def __init__(self, *, camera_control_status: global___EnumCameraControlStatus.ValueType | None = ...) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal["camera_control_status", b"camera_control_status"],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal["camera_control_status", b"camera_control_status"],
    ) -> None: ...

global___RequestSetCameraControlStatus = RequestSetCameraControlStatus
