import os 
import requests

def automate_post_request(external_ip):
  path = '/data/feedback/'
  lst = os.listdir(path)
  content = {}
  for file in lst:
    with open(os.path.join(path, file), 'r') as f:
        lines = [line.rstrip() for line in f]
        content['title'] = lines[0]
        content['name'] = lines[1]
        content['date'] = lines[2]
        content['feedback'] = lines[3]

    res = requests.post(
        f'http://{external_ip}/feedback/',
        data=content
    )
    print(res.status_code)

automate_post_request('35.224.100.10')
