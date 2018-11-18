import requests
import re
import time
import os,sys
#url='http://www.14epep.com/vodata/1608/play.html?1608-0-1'
headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
    }
def star():
    urls=['http://www.14epep.com/arts/{}.html'.format(str(i)) for i in range(393293,393299)] 
    tp=re.compile(r'src.+?"(.+?jpg)"')
    for url in urls:
        print(url)
        html=requests.get(url,headers=headers) 
        jpg=re.findall(tp,html.text)
        save(jpg)
def save(urls):       
    i=0
    for url in urls:   
        print(url)
        try:
            tupian=requests.get(url,timeout=20)
            img=tupian.content
            with open('F:\\刘畅\\学习\\html\\tp\\'+str(0)+'\\'+str(i)+'.jpg','wb') as f:    
                f.write(img)
                print(str(i)+',ok')
                i+=1       
        except :
            print('no')
            pass

if __name__=='__main__':
    
    print(1)
    star()
    print(1)

    