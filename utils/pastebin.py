# Python module to upload text to pastebin.com

import requests
import json

class Pastebin:
    def __init__(self, api_key, api_option='paste', api_paste_private='0', api_paste_expire_date='N', api_paste_format='text'):
        self.api_key = api_key
        self.url = 'https://pastebin.com/api/api_post.php'
        self.headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        self.data = {
            'api_dev_key': self.api_key, # api key
            'api_option': api_option, # Available options: paste, list, login, userdetails, delete, expire etc.
            'api_paste_private': api_paste_private, # 0 = public, 1 = unlisted, 2 = private
            'api_paste_expire_date': api_paste_expire_date, # N = Never, 10M = 10 Minutes, 1H = 1 Hour, 1D = 1 Day, 1W = 1 Week, 2W = 2 Weeks, 1M = 1 Month, 6M = 6 Months, 1Y = 1 Year
            'api_paste_format': api_paste_format # Available formats: text, c, cpp, csharp, css, diff, html4strict, java, javascript, lua, mysql, objectivec, perl, php, python, ruby, vb, xml
        }
    def upload(self, text, title):
        self.data['api_paste_code'] = text
        self.data['api_paste_name'] = title
        r = requests.post(self.url, headers=self.headers, data=self.data)
        return r.text
    
    def get_url(self, text, title):
        return self.upload(text, title)
    

if __name__ == '__main__':
    # Read config file for pastebin api key
    with open('config.json', 'r') as f:
        config = json.load(f)
    api_key = config['PASTEBIN_API_KEY']
    pastebin = Pastebin(api_key)
    print(pastebin.get_url('Hello World', 'Hello World'))
