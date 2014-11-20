import sys
import argparse

import usb.core
import usb.util


__version__ = '2014.11.20'


OFF = 0x0
ON = 0x1
RED = 0x10
YELLOW = 0x11
GREEN = 0x12


class ClewareAmpel:

    def __init__(self):
        self.interface = 0
        self.device = usb.core.find(idVendor=0x0d50, idProduct=0x0008)
        if self.device is None:
            raise Exception('Cleware Ampel not found')
        self.reattach = False
        if self.device.is_kernel_driver_active(self.interface):
            self.device.detach_kernel_driver(self.interface)
            self.reattach = True

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        usb.util.dispose_resources(self.device)
        if self.reattach:
            self.device.attach_kernel_driver(self.interface)

    def _set_led(self, color, value):
        self.device.ctrl_transfer(0x21, 0x09, 0x200, 0x00, [0x00, color, value])

    def all_on(self):
        self.red_on()
        self.yellow_on()
        self.green_on()

    def all_off(self):
        self.red_off()
        self.yellow_off()
        self.green_off()

    def red_on(self):
        self._set_led(RED, ON)

    def red_off(self):
        self._set_led(RED, OFF)

    def red_only(self):
        self.all_off()
        self.red_on()

    def yellow_on(self):
        self._set_led(YELLOW, ON)

    def yellow_off(self):
        self._set_led(YELLOW, OFF)

    def yellow_only(self):
        self.all_off()
        self.yellow_on()

    def green_on(self):
        self._set_led(GREEN, ON)

    def green_off(self):
        self._set_led(GREEN, OFF)

    def green_only(self):
        self.all_off()
        self.green_on()


def main():
    parser = argparse.ArgumentParser(description='Cleware Ampel')
    parser.add_argument('--all-on', action='store_true',
                        help='Switch all lights on')
    parser.add_argument('--off', action='store_true',
                        help='Switch all lights off')
    parser.add_argument('--red', action='store_true',
                        help='Switch only red light on')
    parser.add_argument('--red-on', action='store_true',
                        help='Switch red light on')
    parser.add_argument('--red-off', action='store_true',
                        help='Switch red light off')
    parser.add_argument('--yellow', action='store_true',
                        help='Switch only yellow light on')
    parser.add_argument('--yellow-on', action='store_true',
                        help='Switch yellow light on')
    parser.add_argument('--yellow-off', action='store_true',
                        help='Switch yellow light off')
    parser.add_argument('--green', action='store_true',
                        help='Switch only green light on')
    parser.add_argument('--green-on', action='store_true',
                        help='Switch green light on')
    parser.add_argument('--green-off', action='store_true',
                        help='Switch green light off')
    args = parser.parse_args()

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    with ClewareAmpel() as ampel:
        if args.off:
            ampel.all_off()
        if args.all_on:
            ampel.all_on()
        if args.red_off:
            ampel.red_off()
        if args.red_on:
            ampel.red_on()
        if args.yellow_off:
            ampel.yellow_off()
        if args.yellow_on:
            ampel.yellow_on()
        if args.green_off:
            ampel.green_off()
        if args.green_on:
            ampel.green_on()
        if args.red:
            ampel.red_only()
        if args.yellow:
            ampel.yellow_only()
        if args.green:
            ampel.green_only()


if __name__ == '__main__':
    main()
