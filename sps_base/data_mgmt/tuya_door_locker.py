from .support_devices import (
    DeviceCategory, 
    DeviceType, 
    DeviceInfo, 
    SupportDevice,
    getIconUrlByDeviceType,
    deviceCategory_Locker)
from sps_base.devices import (
    DEVICE_CATEGORY, 
    DEVICE_TYPE, 
    DEVICE_VENDOR)

import pprint


# 添加设备类型 到 大类 : 门锁开关
deviceCategory_Locker.addDeviceType(
    DeviceType(
        id=DEVICE_TYPE.door_locker,
        name="tuya door locker(E202)",
        icon=getIconUrlByDeviceType(DEVICE_TYPE.door_locker),
        deviceInfo=DeviceInfo(
            manufacturer=DEVICE_VENDOR.TUYA,
            model="E202"
        )
    )
)

# 数据模版