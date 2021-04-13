
def test_DeviceInfoDocument_exists():
    from sps_base.db.device import DeviceInfoDocument
    deviceId = "00010956AB05004B1201"
    diDoc = DeviceInfoDocument(docId=deviceId)
    print(diDoc.exists())

def test_DeviceInfoDocument_get():
    from sps_base.db.device import DeviceInfoDocument
    deviceId = "00010956AB05004B1201"
    diDoc = DeviceInfoDocument(docId=deviceId)
    print(diDoc.get())

def test_DeviceInfoDocument_create():
    from sps_base.db.device import DeviceInfoDocument
    deviceId = "00010956AB05004B1201"
    diDoc = DeviceInfoDocument(docId=deviceId)
    data = {
        'house_id': 'Sn05C2ui8ru5FluwfqWw', 
        'user_id': 'm2wUMhgAHjR2CbE4PUA8jD22pu82'
    }
    result = diDoc.create(data)
    print(result)

def test_DeviceInfoDocument_update():
    from sps_base.db.device import DeviceInfoDocument
    deviceId = "00010956AB05004B1201"
    diDoc = DeviceInfoDocument(docId=deviceId)
    data = {
        'house_id': 'Sn05C2ui8ru5FluwfUPDATE', 
        'user_id': 'm2wUMhgAHjR2CbE4PUA8jD22pu82'
    }
    result = diDoc.update(data)
    print(result)

def test_DeviceInfoDocument_delete():
    from sps_base.db.device import DeviceInfoDocument
    deviceId = "00010956AB05004B1201"
    diDoc = DeviceInfoDocument(docId=deviceId)
    data = {
        'house_id': 'Sn05C2ui8ru5FluwfqWw', 
        'user_id': 'm2wUMhgAHjR2CbE4PUA8jD22pu82'
    }
    result = diDoc.delete()
    print(result)



def test_DeviceHistoryDatasCollection_get():
    from sps_base.db.device import DeviceHistoryDatasCollection
    userId = "2UD13YiZzOa247jdB0GVWYf9bIG2"
    houseId = "johKvru3sEPJ2eMpqvKk"
    dhdCol = DeviceHistoryDatasCollection(
        userId=userId, houseId=houseId)
    result = dhdCol.get(documentId="00BGzj5QdfmpKtthUJ7X")
    print(result)

def test_DeviceHistoryDatasCollection_list():
    from sps_base.db.device import DeviceHistoryDatasCollection
    userId = "2UD13YiZzOa247jdB0GVWYf9bIG2"
    houseId = "johKvru3sEPJ2eMpqvKk"
    dhdCol = DeviceHistoryDatasCollection(
        userId=userId, houseId=houseId)
    result = dhdCol.list(condition={
        "deviceId": {
            "==": "0001D6E76B0F004B1200"
        }
    })
    print(result)
    for doc in result:
        print(doc)

def test_DeviceHistoryDatasCollection_add():
    from sps_base.db.device import DeviceHistoryDatasCollection
    userId = "2UD13YiZzOa247jdB0GVWYf9bIG2"
    houseId = "johKvru3sEPJ2eMpqvKk"
    dhdCol = DeviceHistoryDatasCollection(
        userId=userId, houseId=houseId)
    data = {
        'states': {'currentSensorStateData': {
            'temperatureAmbientCelsius': 24.1, 
            'humidityAmbientPercent': 55.7}}, 
            'time': 1606555506114, 
            'deviceId': '0001D6E76B0F004B1200'}
    result = dhdCol.add(data)
    print(result)

# hdJu25zyi2Kt2LRiwwZQ
def test_DeviceHistoryDatasCollection_delete():
    from sps_base.db.device import DeviceHistoryDatasCollection
    userId = "2UD13YiZzOa247jdB0GVWYf9bIG2"
    houseId = "johKvru3sEPJ2eMpqvKk"
    docId = "hdJu25zyi2Kt2LRiwwZQ"
    dhdCol = DeviceHistoryDatasCollection(
        userId=userId, houseId=houseId)
    result = dhdCol.delete(documentId=docId)
    print(result)



def test_DeviceDocument_get():
    from sps_base.db.device import DeviceDocument
    userId = "2UD13YiZzOa247jdB0GVWYf9bIG2"
    houseId = "johKvru3sEPJ2eMpqvKk"
    deviceId = "00010CD7D614004B1200"
    deviceDoc = DeviceDocument(
        userId=userId, houseId=houseId, deviceId=deviceId,
        deviceVendorPrefix="0001")
    result = deviceDoc.get()
    print(result)