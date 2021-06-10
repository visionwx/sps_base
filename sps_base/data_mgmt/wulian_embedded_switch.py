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


# 添加设备类型 到 大类 : 嵌入式开关 1
deviceCategory_Switch.addDeviceType(
    DeviceType(
        id=DEVICE_TYPE.embedded_switch_1,
        name="wulian one-gang embedded switch",
        description="",
        icon=getIconUrlByDeviceType(DEVICE_TYPE.embedded_switch_1),
        pictures=[],
        enable=True,
        deviceInfo=DeviceInfo(
            manufacturer=DEVICE_VENDOR.WULIAN,
            model="WL-ZCSENPB-S0410-01"
        )
    )
)

# 添加设备类型 到 大类 : 嵌入式开关 2
deviceCategory_Switch.addDeviceType(
    DeviceType(
        id=DEVICE_TYPE.embedded_switch_2,
        name="wulian two-gang embedded switch",
        description="",
        icon=getIconUrlByDeviceType(DEVICE_TYPE.embedded_switch_2),
        pictures=[],
        enable=True,
        deviceInfo=DeviceInfo(
            manufacturer=DEVICE_VENDOR.WULIAN,
            model="WL-ZCSENPB-S0410-02"
        )
    )
)