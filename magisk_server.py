from flask import Flask
from flask.json import jsonify

app = Flask(__name__)

# #PC running Ubuntu or other linux distros
# #Make sure python3 is already installed
# curl -L 'https://github.com/agnostic-apollo/magisk_server/raw/master/magisk_server.py' -o "magisk_server.py"
# sudo pip install Flask
# export FLASK_APP=magisk_server.py
# flask run --host=0.0.0.0
# #Connect pc to same wifi as android device running magisk manager
# #Magisk custom channel: http://<pc-ip>:5000 (example: http://192.168.0.2:5000)

# #Termux on Android
# curl -L 'https://github.com/agnostic-apollo/magisk_server/raw/master/magisk_server.py' -o "magisk_server.py"
# pkg install python
# pip install Flask
# export FLASK_APP=magisk_server.py
# flask run --host=0.0.0.0
# #Magisk custom channel: http://localhost:5000

# #You can can test the address in your browser as well to get the json response
# #DO NOT forget to prefix the ip with "http://" in magisk custom channel settings field

# #To find md5 for magisk-v*.zip, download it and run
# md5sum Magisk-v21.2.zip


@app.route('/')
def hello_world():

	return jsonify({
		'app': {
			'version': "8.0.4",
			'versionCode': "4768",
			'link': "https://github.com/topjohnwu/Magisk/releases/download/manager-v8.0.4/MagiskManager-v8.0.4.apk",
			'note': "https://github.com/topjohnwu/Magisk/blob/master/README.MD"
		},
		'magisk': {
			'version': "21.2",
			'versionCode': "21200",
			'link': "https://github.com/topjohnwu/Magisk/releases/download/v21.2/Magisk-v21.2.zip",
			'note': "https://github.com/topjohnwu/Magisk/blob/master/README.MD",
			'md5': "165b48cbd6fb2507bf74c820cccb9781"
		},
		'uninstaller': {
			'link': "https://github.com/topjohnwu/Magisk/releases/download/v21.2/Magisk-uninstaller-20201228.zip"
		},
		'stub': {
			'versionCode': "4768",
			'link': "https://github.com/topjohnwu/Magisk/releases/download/manager-v8.0.4/stub-release.apk"
		}
	})


if __name__ == '__main__':
	app.run()
