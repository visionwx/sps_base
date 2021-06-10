from .support_devices import (
    DeviceCategory, 
    DeviceType, 
    DeviceInfo, 
    SupportDevice,
    getIconUrlByDeviceType,
    deviceCategory_Gateway)
from sps_base.devices import (
    DEVICE_CATEGORY, 
    DEVICE_TYPE, 
    DEVICE_VENDOR)

import pprint


# 添加 物联网关类型01
deviceCategory_Gateway.addDeviceType(DeviceType(
    id=DEVICE_TYPE.gateway_01,
    name="WuLian Smart Gateway Type_01",
    description="",
    icon=getIconUrlByDeviceType(DEVICE_TYPE.gateway_01),
    pictures=[],
    enable=True,
    deviceInfo=DeviceInfo(
        manufacturer=DEVICE_VENDOR.WULIAN,
        model="WL-ZGWMDPB-G110-05"
    )
))

# 添加 物联网关类型02
deviceCategory_Gateway.addDeviceType(DeviceType(
    id=DEVICE_TYPE.gateway_02,
    name="WuLian Smart Gateway Type_02",
    description="",
    icon=getIconUrlByDeviceType(DEVICE_TYPE.gateway_02),
    pictures=[],
    enable=True,
    deviceInfo=DeviceInfo(
        manufacturer=DEVICE_VENDOR.WULIAN,
        model="WL-ZGWMDPB-G100-0"
    )
))


# 物联网关数据模型