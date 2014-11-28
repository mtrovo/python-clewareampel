python-clewareampel
===================

[![version](https://pypip.in/v/clewareampel/badge.png?style=flat)](https://pypi.python.org/pypi/clewareampel)
[![Supported Python versions](https://pypip.in/py_versions/clewareampel/badge.svg?style=flat)](https://pypi.python.org/pypi/clewareampel/)
[![format](https://pypip.in/format/clewareampel/badge.png?style=flat)](https://pypi.python.org/pypi/clewareampel)
[![downloads](https://pypip.in/d/clewareampel/badge.png?style=flat)](https://pypi.python.org/pypi/clewareampel)
[![license](https://pypip.in/license/clewareampel/badge.png?style=flat)](https://pypi.python.org/pypi/clewareampel)

Control the Cleware USB Ampel (traffic lights) with Python.

In this version only one Ampel can be controlled. It was not tested what will
happen when you have two Ampels plugged.


## In code

    from clewareampel import ClewareAmpel

    with ClewareAmpel as ampel:
        ampel.green_only()

Have a look into `example.py` or just run it to see if your Ampel is working.

## On the command line

    usage: clewareampel.py [-h] [--all-on] [--off] [--red] [--red-on] [--red-off]
                           [--yellow] [--yellow-on] [--yellow-off] [--green]
                           [--green-on] [--green-off]

    Cleware Ampel

    optional arguments:
      -h, --help    show this help message and exit
      --all-on      Switch all lights on
      --off         Switch all lights off
      --red         Switch only red light on
      --red-on      Switch red light on
      --red-off     Switch red light off
      --yellow      Switch only yellow light on
      --yellow-on   Switch yellow light on
      --yellow-off  Switch yellow light off
      --green       Switch only green light on
      --green-on    Switch green light on
      --green-off   Switch green light off


To turn only the green light on, run

    clewareampel --green

Why not add a yellow to the green?

    clewareampel --yellow-on


## udev

Copy `99-clewareampel.rules` to `/etc/udev/rules.d/` to allow this tool to use
the USB device.
