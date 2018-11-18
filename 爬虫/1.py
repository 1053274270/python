import requests
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}

url='http://www.14epep.com/arts/393291.html'
a=requests.get(url,headers=headers)
print(a)
with open('F:\\刘畅\\学习\\html\\tp\\1.html','wb') as f:    
    print(1)
    f.write(a.content)
    print('ok')
    