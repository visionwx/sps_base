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


# 添加设备类型 到 大类 : 一联墙壁开关
deviceCategory_Switch.addDeviceType(
    DeviceType(
        id=DEVICE_TYPE.wall_switch_1,
        name="wulian one-gang wall switch",
        description="",
        icon=getIconUrlByDeviceType(DEVICE_TYPE.wall_switch_1),
        pictures=[],
        enable=True,
        deviceInfo=DeviceInfo(
            manufacturer=DEVICE_VENDOR.WULIAN,
            model="WL-ZCSWNPW-S1322-01"
        )
    )
)

# 添加设备类型 到 大类 : 二联墙壁开关
deviceCategory_Switch.addDeviceType(
    DeviceType(
        id=DEVICE_TYPE.wall_switch_2,
        name="wulian two-gang wall switch",
        description="",
        icon=getIconUrlByDeviceType(DEVICE_TYPE.wall_switch_2),
        pictures=[],
        enable=True,
        deviceInfo=DeviceInfo(
            manufacturer=DEVICE_VENDOR.WULIAN,
            model="WL-ZCSWNPW-S1322-02"
        )
    )
)

# 添加设备类型 到 大类 : 三联墙壁开关
deviceCategory_Switch.addDeviceType(
    DeviceType(
        id=DEVICE_TYPE.wall_switch_3,
        name="wulian three-gang wall switch",
        description="",
        icon=getIconUrlByDeviceType(DEVICE_TYPE.wall_switch_3),
        pictures=[],
        enable=True,
        deviceInfo=DeviceInfo(
            manufacturer=DEVICE_VENDOR.WULIAN,
            model="WL-ZCSWNPW-S1322-03"
        )
    )
)


# 开关数据模版