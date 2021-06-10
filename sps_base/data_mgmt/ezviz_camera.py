from .support_devices import (
    DeviceCategory, 
    DeviceType, 
    DeviceInfo, 
    SupportDevice,
    getIconUrlByDeviceType,
    deviceCategory_Camera)
from sps_base.devices import (
    DEVICE_CATEGORY, 
    DEVICE_TYPE, 
    DEVICE_VENDOR)

import pprint


# 添加设备类型 到 大类 : c3w
deviceCategory_Camera.addDeviceType(
    DeviceType(
        id=DEVICE_TYPE.camera_c3w,
        name="Ezviz C3W",
        description="",
        icon=getIconUrlByDeviceType(DEVICE_TYPE.camera_c3w),
        pictures=[],
        enable=True,
        deviceInfo=DeviceInfo(
            manufacturer=DEVICE_VENDOR.EZVIZ,
            model="C3W"
        )
    )
)

# 添加设备类型 到 大类 : c3x
deviceCategory_Camera.addDeviceType(
    DeviceType(
        id=DEVICE_TYPE.camera_c3x,
        name="Ezviz C3X",
        description="",
        icon=getIconUrlByDeviceType(DEVICE_TYPE.camera_c3x),
        pictures=[],
        enable=True,
        deviceInfo=DeviceInfo(
            manufacturer=DEVICE_VENDOR.EZVIZ,
            model="C3X"
        )
    )
)

# 添加设备类型 到 大类 : c3A
deviceCategory_Camera.addDeviceType(
    DeviceType(
        id=DEVICE_TYPE.camera_c3a,
        name="Ezviz C3A",
        description="",
        icon=getIconUrlByDeviceType(DEVICE_TYPE.camera_c3a),
        pictures=[],
        enable=True,
        deviceInfo=DeviceInfo(
            manufacturer=DEVICE_VENDOR.EZVIZ,
            model="C3A"
        )
    )
)

# 添加设备类型 到 大类 : LC1C
deviceCategory_Camera.addDeviceType(
    DeviceType(
        id=DEVICE_TYPE.camera_lc1c,
        name="Ezviz LC1C",
        description="",
        icon=getIconUrlByDeviceType(DEVICE_TYPE.camera_lc1c),
        pictures=[],
        enable=True,
        deviceInfo=DeviceInfo(
            manufacturer=DEVICE_VENDOR.EZVIZ,
            model="LC1C"
        )
    )
)

# 添加设备类型 到 大类 : BC1
deviceCategory_Camera.addDeviceType(
    DeviceType(
        id=DEVICE_TYPE.camera_bc1,
        name="Ezviz BC1",
        description="",
        icon=getIconUrlByDeviceType(DEVICE_TYPE.camera_bc1),
        pictures=[],
        enable=True,
        deviceInfo=DeviceInfo(
            manufacturer=DEVICE_VENDOR.EZVIZ,
            model="BC1"
        )
    )
)

# 数据模版
