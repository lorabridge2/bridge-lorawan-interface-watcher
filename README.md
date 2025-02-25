# Lorawan interface watcher

This repository is part of the [LoRaBridge](https://github.com/lorabridge2/lorabridge) project.

This repository contains code, that restarts the lorawan-interface container if it is stopped due to an error.
In case the esp32 usb device is removed, docker stops the container, but does not try to bring it up again when the device is readded.

## Environment Variables

- `REDIS_HOST`: IP or hostname of Redis host
- `REDIS_PORT`: Port used by Redis
- `REDIS_DB`: Number of the database used inside Redis

## License

All the LoRaBridge software components and the documentation are licensed under GNU General Public License 3.0.

## Acknowledgements

The financial support from Internetstiftung/Netidee is gratefully acknowledged. The mission of Netidee is to support development of open-source tools for more accessible and versatile use of the Internet in Austria.
