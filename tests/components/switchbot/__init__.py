"""Tests for the switchbot integration."""
from unittest.mock import patch

from bleak.backends.device import BLEDevice
from bleak.backends.scanner import AdvertisementData

from homeassistant.components.bluetooth import BluetoothServiceInfoBleak
from homeassistant.const import CONF_ADDRESS
from homeassistant.core import HomeAssistant

from tests.common import MockConfigEntry

DOMAIN = "switchbot"

ENTRY_CONFIG = {
    CONF_ADDRESS: "e7:89:43:99:99:99",
}

USER_INPUT = {
    CONF_ADDRESS: "aa:bb:cc:dd:ee:ff",
}

USER_INPUT_UNSUPPORTED_DEVICE = {
    CONF_ADDRESS: "test",
}

USER_INPUT_INVALID = {
    CONF_ADDRESS: "invalid-mac",
}


def patch_async_setup_entry(return_value=True):
    """Patch async setup entry to return True."""
    return patch(
        "homeassistant.components.switchbot.async_setup_entry",
        return_value=return_value,
    )


async def init_integration(
    hass: HomeAssistant,
    *,
    data: dict = ENTRY_CONFIG,
    skip_entry_setup: bool = False,
) -> MockConfigEntry:
    """Set up the Switchbot integration in Home Assistant."""
    entry = MockConfigEntry(domain=DOMAIN, data=data)
    entry.add_to_hass(hass)

    if not skip_entry_setup:
        await hass.config_entries.async_setup(entry.entry_id)
        await hass.async_block_till_done()

    return entry


WOHAND_SERVICE_INFO = BluetoothServiceInfoBleak(
    name="WoHand",
    manufacturer_data={89: b"\xfd`0U\x92W"},
    service_data={"00000d00-0000-1000-8000-00805f9b34fb": b"H\x90\xd9"},
    service_uuids=["cba20d00-224d-11e6-9fb8-0002a5d5c51b"],
    address="AA:BB:CC:DD:EE:FF",
    rssi=-60,
    source="local",
    advertisement=AdvertisementData(
        local_name="WoHand",
        manufacturer_data={89: b"\xfd`0U\x92W"},
        service_data={"00000d00-0000-1000-8000-00805f9b34fb": b"H\x90\xd9"},
        service_uuids=["cba20d00-224d-11e6-9fb8-0002a5d5c51b"],
    ),
    device=BLEDevice("AA:BB:CC:DD:EE:FF", "WoHand"),
    time=0,
    connectable=True,
)


WOHAND_SERVICE_INFO_NOT_CONNECTABLE = BluetoothServiceInfoBleak(
    name="WoHand",
    manufacturer_data={89: b"\xfd`0U\x92W"},
    service_data={"00000d00-0000-1000-8000-00805f9b34fb": b"H\x90\xd9"},
    service_uuids=["cba20d00-224d-11e6-9fb8-0002a5d5c51b"],
    address="aa:bb:cc:dd:ee:ff",
    rssi=-60,
    source="local",
    advertisement=AdvertisementData(
        local_name="WoHand",
        manufacturer_data={89: b"\xfd`0U\x92W"},
        service_data={"00000d00-0000-1000-8000-00805f9b34fb": b"H\x90\xd9"},
        service_uuids=["cba20d00-224d-11e6-9fb8-0002a5d5c51b"],
    ),
    device=BLEDevice("aa:bb:cc:dd:ee:ff", "WoHand"),
    time=0,
    connectable=False,
)


WOHAND_ENCRYPTED_SERVICE_INFO = BluetoothServiceInfoBleak(
    name="WoHand",
    manufacturer_data={89: b"\xd8.\xad\xcd\r\x85"},
    service_data={"00000d00-0000-1000-8000-00805f9b34fb": b"\xc8\x10\xcf"},
    service_uuids=["cba20d00-224d-11e6-9fb8-0002a5d5c51b"],
    address="798A8547-2A3D-C609-55FF-73FA824B923B",
    rssi=-60,
    source="local",
    advertisement=AdvertisementData(
        local_name="WoHand",
        manufacturer_data={89: b"\xd8.\xad\xcd\r\x85"},
        service_data={"00000d00-0000-1000-8000-00805f9b34fb": b"\xc8\x10\xcf"},
        service_uuids=["cba20d00-224d-11e6-9fb8-0002a5d5c51b"],
    ),
    device=BLEDevice("798A8547-2A3D-C609-55FF-73FA824B923B", "WoHand"),
    time=0,
    connectable=True,
)


WOHAND_SERVICE_ALT_ADDRESS_INFO = BluetoothServiceInfoBleak(
    name="WoHand",
    manufacturer_data={89: b"\xfd`0U\x92W"},
    service_data={"00000d00-0000-1000-8000-00805f9b34fb": b"H\x90\xd9"},
    service_uuids=["cba20d00-224d-11e6-9fb8-0002a5d5c51b"],
    address="cc:cc:cc:cc:cc:cc",
    rssi=-60,
    source="local",
    advertisement=AdvertisementData(
        local_name="WoHand",
        manufacturer_data={89: b"\xfd`0U\x92W"},
        service_data={"00000d00-0000-1000-8000-00805f9b34fb": b"H\x90\xd9"},
        service_uuids=["cba20d00-224d-11e6-9fb8-0002a5d5c51b"],
    ),
    device=BLEDevice("aa:bb:cc:dd:ee:ff", "WoHand"),
    time=0,
    connectable=True,
)
WOCURTAIN_SERVICE_INFO = BluetoothServiceInfoBleak(
    name="WoCurtain",
    address="aa:bb:cc:dd:ee:ff",
    manufacturer_data={89: b"\xc1\xc7'}U\xab"},
    service_data={"00000d00-0000-1000-8000-00805f9b34fb": b"c\xd0Y\x00\x11\x04"},
    service_uuids=["cba20d00-224d-11e6-9fb8-0002a5d5c51b"],
    rssi=-60,
    source="local",
    advertisement=AdvertisementData(
        local_name="WoCurtain",
        manufacturer_data={89: b"\xc1\xc7'}U\xab"},
        service_data={"00000d00-0000-1000-8000-00805f9b34fb": b"c\xd0Y\x00\x11\x04"},
        service_uuids=["cba20d00-224d-11e6-9fb8-0002a5d5c51b"],
    ),
    device=BLEDevice("aa:bb:cc:dd:ee:ff", "WoCurtain"),
    time=0,
    connectable=True,
)

WOSENSORTH_SERVICE_INFO = BluetoothServiceInfoBleak(
    name="WoSensorTH",
    service_uuids=["cba20d00-224d-11e6-9fb8-0002a5d5c51b"],
    address="aa:bb:cc:dd:ee:ff",
    manufacturer_data={2409: b"\xda,\x1e\xb1\x86Au\x03\x00\x96\xac"},
    service_data={"0000fd3d-0000-1000-8000-00805f9b34fb": b"T\x00d\x00\x96\xac"},
    rssi=-60,
    source="local",
    advertisement=AdvertisementData(
        manufacturer_data={2409: b"\xda,\x1e\xb1\x86Au\x03\x00\x96\xac"},
        service_data={"0000fd3d-0000-1000-8000-00805f9b34fb": b"T\x00d\x00\x96\xac"},
    ),
    device=BLEDevice("aa:bb:cc:dd:ee:ff", "WoSensorTH"),
    time=0,
    connectable=False,
)

NOT_SWITCHBOT_INFO = BluetoothServiceInfoBleak(
    name="unknown",
    service_uuids=[],
    address="aa:bb:cc:dd:ee:ff",
    manufacturer_data={},
    service_data={},
    rssi=-60,
    source="local",
    advertisement=AdvertisementData(
        manufacturer_data={},
        service_data={},
    ),
    device=BLEDevice("aa:bb:cc:dd:ee:ff", "unknown"),
    time=0,
    connectable=True,
)
