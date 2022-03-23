import requests

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0', 'content-type': 'application/x-www-form-urlencode'}

req = requests.head("http://mercury.picoctf.net:45028/index.php", headers=headers)

print(req.headers['flag'])
