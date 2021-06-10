
from .support_devices import (
    DeviceCategory, 
    DeviceType, 
    DeviceInfo, 
    SupportDevice,
    getIconUrlByDeviceType,
    deviceCategory_Sensor)
from sps_base.devices import (
    DEVICE_CATEGORY, 
    DEVICE_TYPE, 
    DEVICE_VENDOR)

import pprint


# 添加设备类型 到 大类 : 光强检测器
deviceCategory_Sensor.addDeviceType(
    DeviceType(
        id=DEVICE_TYPE.light_sensor,
        name="wuLian light sensor",
        description="",
        icon=getIconUrlByDeviceType(DEVICE_TYPE.light_sensor),
        pictures=[],
        enable=True,
        deviceInfo=DeviceInfo(
            manufacturer=DEVICE_VENDOR.WULIAN,
            model="WL-ZSSWBPW-AL-01"
        )
    )
)

# 添加设备类型 到 大类 : 温度湿度检测器
deviceCategory_Sensor.addDeviceType(
    DeviceType(
        id=DEVICE_TYPE.temp_humi_sensor,
        name="WuLian tempeture and humidity sensor",
        description="",
        icon=getIconUrlByDeviceType(DEVICE_TYPE.temp_humi_sensor),
        pictures=[],
        enable=True,
        deviceInfo=DeviceInfo(
            manufacturer=DEVICE_VENDOR.WULIAN,
            model="WL-ZSSWBPW-TH-01"
        )
    )
)

# 添加设备数据模版







# 第一个设备组别 定义：
# Smart Gateway
supportDevice__SmartGateway = SupportDevice(
    id = "0001",
    rankId=1,
    groupName="Smart Gateway",
    enable=True,
    deviceCategorys=[]
)
deviceCategory_SmartGateway = DeviceCategory(
    id = DEVICE_CATEGORY.smart_gateway,
    name = "Smart Gateway",
    description="",
    icon="",
    enable=True,
    deviceTypes=[]
)
# 添加 物联网关类型01
deviceCategory_SmartGateway.addDeviceType(DeviceType(
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
deviceCategory_SmartGateway.addDeviceType(DeviceType(
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
# 添加 category到 supportDevice
supportDevice__SmartGateway.addDeviceCategory(deviceCategory_SmartGateway)




supportDevice__SensorDetector = SupportDevice(
    id = "0002",
    rankId=2,
    groupName="Sensor and Detector",
    enable=True,
    deviceCategorys=[
        DeviceCategory(
            id = DEVICE_CATEGORY.environment_sensor,
            name = "Environment Sensor",
            description="",
            icon="",
            enable=True,
            deviceTypes=[
                DeviceType(
                    id=DEVICE_TYPE.light_sensor,
                    name="wuLian light sensor",
                    description="",
                    icon=getIconUrlByDeviceType(DEVICE_TYPE.light_sensor),
                    pictures=[],
                    enable=True,
                    deviceInfo=DeviceInfo(
                        manufacturer=DEVICE_VENDOR.WULIAN,
                        model="WL-ZSSWBPW-AL-01"
                    )
                ),
                DeviceType(
                    id=DEVICE_TYPE.temp_humi_sensor,
                    name="WuLian tempeture and humidity sensor",
                    description="",
                    icon=getIconUrlByDeviceType(DEVICE_TYPE.temp_humi_sensor),
                    pictures=[],
                    enable=True,
                    deviceInfo=DeviceInfo(
                        manufacturer=DEVICE_VENDOR.WULIAN,
                        model="WL-ZSSWBPW-TH-01"
                    )
                ),
            ]
        ),
        DeviceCategory(
            id = DEVICE_CATEGORY.security_detector,
            name = "Security Detector",
            description="",
            icon="",
            enable=True,
            deviceTypes=[
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
                ),
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
                ),
                DeviceType(
                    id=DEVICE_TYPE.pir_detector,
                    name="wulian smoke detector",
                    description="",
                    icon=getIconUrlByDeviceType(DEVICE_TYPE.pir_detector),
                    pictures=[],
                    enable=True,
                    deviceInfo=DeviceInfo(
                        manufacturer=DEVICE_VENDOR.WULIAN,
                        model="WL-ZSPWBPW-PI11-02"
                    )
                ),
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
                ),
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
                ),
            ]
        )
    ]
)





supportDevice__SmartSwitch = SupportDevice(
    id = "0003",
    rankId=3,
    groupName="Smart Switch",
    enable=True,
    deviceCategorys=[
        DeviceCategory(
            id = DEVICE_CATEGORY.smart_switch,
            name = "Smart Switch",
            description="",
            icon="",
            enable=True,
            deviceTypes=[
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
                ),
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
                ),
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
                ),

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
                ),
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
                ),

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
                ),


            ]
        )
    ]
)


pprint.pprint(supportDevice__SmartGateway.toDict())