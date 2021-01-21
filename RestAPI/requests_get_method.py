import requests

reply = requests.get('http://localhost:3000')
# print(reply.status_code)
# for k,v in requests.codes.__dict__.items():
#     print(k,v)
# if reply.status_code == requests.codes.ok:
#     print('yeah')

#print(reply.headers)
# print(reply.headers['Content-Type'])
# print(reply.text)

