import requests

print ('hello world')

try:
   r = requests.get('https://google.com')
   print (r.status_code)
   if r.status_code == 200:
      print (r.text)
except Exception as e:
    print ('Ada error', e)
