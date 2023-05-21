# pi-tools
Just a place for me to put some randomly helpful scripts for running on a Raspberry Pi as a development workstation on Raspberry Pi OS.

## Scripts
It is recommended these scripts be placed in a directory that is in your user's path (e.g. `~/bin`) and set to executable.
### raspipress.py
* **Usage:** `raspipress.py` (no script parameters)
* **Description:** Simple script to download all Raspberry Pi Press free books and magazines, by default for the Bookshelf app (see definition of [`localPath`](https://github.com/traek/pi-tools/blob/main/raspipress.py#L15)). Currently, this includes "The MagPi" and "Hackspace" magazines as well as several books they currently offer for free. NOTE: In 2023, Wireframe was shut down by Raspberry Pi Press and Custom PC was sold off and became an online-only publication. Though you may have issues of either in your Bookshelf folder, they will no longer be displayed nor updated by this script. This script is currently limited by the contents hosted at [`bookshelf`](https://github.com/traek/pi-tools/blob/main/raspipress.py#L13) for a list of new and existing content, including thumbnails and other meta data displayed in the [Bookshelf](https://github.com/raspberrypi-ui/bookshelf) app.

## License
[![License](http://img.shields.io/:license-mit-blue.svg)](http://doge.mit-license.org)
