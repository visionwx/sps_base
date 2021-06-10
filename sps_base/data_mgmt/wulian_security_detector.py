
from .support_devices import (
    DeviceCategory, 
    DeviceType, 
    DeviceInfo, 
    SupportDevice,
    getIconUrlByDeviceType,
    deviceCategory_Detector)
from sps_base.devices import (
    DEVICE_CATEGORY, 
    DEVICE_TYPE, 
    DEVICE_VENDOR)

import pprint


# 添加设备类型 到 大类 : 天然气检测
deviceCategory_Detector.addDeviceType(
    DeviceType(
        id=DEVICE_TYPE.gas_detector,
        name="wuLian gas detector",
        description="",
        icon=getIconUrlByDeviceType(DEVICE_TYPE.gas_detector),
        pictures=[],
        enable=True,
        deviceInfo=DeviceInfo(
            manufacturer=DEVICE_VENDOR.WULIAN,
            model="WL-ZSSWBPW-AL-01"
        )
    )
)

# 添加设备类型 到 大类 : 烟雾检测
deviceCategory_Detector.addDeviceType(
    DeviceType(
        id=DEVICE_TYPE.smoke_detector,
        name="wulian smoke detector",
        description="",
        icon=getIconUrlByDeviceType(DEVICE_TYPE.smoke_detector),
        pictures=[],
        enable=True,
        deviceInfo=DeviceInfo(
            manufacturer=DEVICE_VENDOR.WULIAN,
            model="JTYJ-GD-2690/W"
        )
    )
)

# 添加设备类型 到 大类 : 动作检测
deviceCategory_Detector.addDeviceType(
    DeviceType(
        id=DEVICE_TYPE.pir_detector,
        name="wulian pir detector",
        description="",
        icon=getIconUrlByDeviceType(DEVICE_TYPE.pir_detector),
        pictures=[],
        enable=True,
        deviceInfo=DeviceInfo(
            manufacturer=DEVICE_VENDOR.WULIAN,
            model="WL-ZSPWBPW-PI11-02"
        )
    )
)

# 添加设备类型 到 大类 : 门窗磁分离检测器
deviceCategory_Detector.addDeviceType(
    DeviceType(
        id=DEVICE_TYPE.contact_detector,
        name="wulian contactor detector",
        description="",
        icon=getIconUrlByDeviceType(DEVICE_TYPE.contact_detector),
        pictures=[],
        enable=True,
        deviceInfo=DeviceInfo(
            manufacturer=DEVICE_VENDOR.WULIAN,
            model="WL-ZSPDBPW-MT-02"
        )
    )
)

# 添加设备类型 到 大类 : 水漏检测器
deviceCategory_Detector.addDeviceType(
    DeviceType(
        id=DEVICE_TYPE.water_leak_detector,
        name="wulian water leak detector",
        description="",
        icon=getIconUrlByDeviceType(DEVICE_TYPE.water_leak_detector),
        pictures=[],
        enable=True,
        deviceInfo=DeviceInfo(
            manufacturer=DEVICE_VENDOR.WULIAN,
            model="WL-ZSSMBPW-FD-01"
        )
    )
)


# 添加设备数据模版