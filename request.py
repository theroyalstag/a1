import requests

url = 'http://localhost:9000/salary_predict_api'
r = requests.post(url,json={'experience':2, 'test_score':9, 'interview_score':6})

print(r.json())