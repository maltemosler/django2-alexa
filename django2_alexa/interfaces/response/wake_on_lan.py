# wol doc: https://developer.amazon.com/de/blogs/alexa/post/9640283e-07a8-4fa4-85fe-aaa024da53fe/now-alexa-can-power-on-devices-in-low-power-mode-with-the-wake-on-lan-controller
# https://developer.amazon.com/docs/device-apis/alexa-wakeonlancontroller.html

from django2_alexa.utils import Directive


class WakeUp(Directive):
    def __init__(self, mac_addresses: list=None, properties: dict=None):
        if mac_addresses:
            self.mac_addresses = mac_addresses
        else:
            self.mac_addresses = []

        if properties:
            self.properties = properties
        else:
            self.properties = {}

    def to_dict(self):
        return {
            'type': "Alexa.WakeOnLANController",
            'properties': self.properties,
            'configuration': {
                'MACAddresses': self.mac_addresses
            }
        }
