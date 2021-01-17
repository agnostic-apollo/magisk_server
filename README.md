# magisk_server

`magisk_server` is a python script to host your own local custom channel for a [Magisk](https://github.com/topjohnwu/Magisk). This can be used to patch the stock `boot.img` with a specific magisk version instead of the latest `stable` or `beta` one. The credit belongs to [here](https://www.programmersought.com/article/49955502921/).

You can either host the channel server on a pc running `Ubuntu` or other linux distros and likely windows or in [Termux App](https://github.com/termux/termux-app) directly in Android on the same phone running the Magisk Manager. It requires `python3` and [Flash](https://flask.palletsprojects.com/en/1.1.x/installation/#install-flask) to be installed. The dependency install and server run instructions are inside the [magisk_server.py](magisk_server.py) script.

Currently, it defaults to Magisk `v21.2` and Magisk manager `v8.0.4`.
##
