import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'ini_level':2, 'status':1, 'time period(in days)':6, 'goal clarity':1,'experience(years)':1,'leadership':1,'completion on time':1,'budget':2,'employee talent':1,'environment':3,'adaptbility':1,'stress':1,'fear of loss':1})
if :
  print(yes)
else:
  print(no)
print(r.json())
