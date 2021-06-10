from .support_devices import (
    DeviceCategory, 
    DeviceType, 
    DeviceInfo, 
    SupportDevice,
    getIconUrlByDeviceType,
    deviceCategory_Switch)
from sps_base.devices import (
    DEVICE_CATEGORY, 
    DEVICE_TYPE, 
    DEVICE_VENDOR)

import pprint


# 添加设备类型 到 大类 : 场景开关
deviceCategory_Switch.addDeviceType(
    DeviceType(
        id=DEVICE_TYPE.curtain_opener,
        name="tuya curtain controller",
        description="",
        icon=getIconUrlByDeviceType(DEVICE_TYPE.curtain_opener),
        pictures=[],
        enable=True,
        deviceInfo=DeviceInfo(
            manufacturer=DEVICE_VENDOR.TUYA,
            model="3r8gc33pnqsxfe1g"
        )
    )
)

# 数据模版