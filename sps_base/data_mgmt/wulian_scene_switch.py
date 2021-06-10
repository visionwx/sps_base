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
        id=DEVICE_TYPE.scene_switch_6,
        name="wulian scene switch",
        description="",
        icon=getIconUrlByDeviceType(DEVICE_TYPE.scene_switch_6),
        pictures=[],
        enable=True,
        deviceInfo=DeviceInfo(
            manufacturer=DEVICE_VENDOR.WULIAN,
            model="WL-ZCSENPB-S0410-02"
        )
    )
)