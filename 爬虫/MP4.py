import requests
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}
i=1
urls=['https://hd1.o0omvo0o.com/ny/80B2E382/SD/out00{}.ts'.format(str(i)) for i in range(1,9)]
for url in urls:
    a=requests.get(url,headers=headers)
    print()
    with open('F:\\刘畅\\学习\\html\\tp\\'+str(i)+'.ts','wb') as f:           
        f.write(a.content)
        i+=1
        print('ok')
    