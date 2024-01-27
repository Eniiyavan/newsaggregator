import requests
from bs4 import BeautifulSoup

def send_Data(city):
    if city is not None:
    # URL of the website to scrape
        url = "https://timesofindia.indiatimes.com/city/"+city
        url1="https://www.thehindu.com/news/cities/"+city
    else:
        url = "https://timesofindia.indiatimes.com/"
        url1="https://www.thehindu.com/news/"

    # Send an HTTP request to the URL
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    news_container = soup.find_all("figcaption")
    count=0
    result=[]
    result1=[]
    for i in news_container:
        p=i.parent
        j=p.find("img")
        if(p or j):
            if ('href' in p.attrs):
                count+=1
                content_url=p['href']
                img_url=None
            if(j is not None):
                img_url=j['data-src']
                
            if(img_url=="https://static.toiimg.com/thumb/imgsize-78512008,msid-47529300,width-600,resizemode-4/47529300.jpg" or img_url==None):
                a={
                "img_url":None,
                "content":i.string,
                "content_url":content_url
                }
                result.append(a)
            
            else:
                a={
                "img_url":img_url,
                "content":i.string,
                "content_url":content_url
                }
                result1.append(a)
    
    response1=requests.get(url1)
    soup1=BeautifulSoup(response1.text,'html.parser')
    
    news_container1=soup1.find_all(class_='title')
    for i in news_container1:
        c=i.find('a')
        if c and i.string:
            content_url=c['href']
            a={
            "content":i.string,
            "content_url":content_url
            }
        
            result.append(a)
    result=result+result1
    
    return result

    
def send_specific(link):
    if(link[:10]=='https://ti'):
        r=requests.get(link)
        s=BeautifulSoup(r.text,'html.parser')
        r1=s.find_all(class_='wJnIp')
        for i in r1:
            b=i.find('img')

            img_url=b['src']
            content=b['alt']
            print(content,img_url)
        all_content = s.find('div', class_='_s30J clearfix')
        if(all_content):
            all_contents=all_content.find_all(text=True, recursive=False)
            result=""  
            for content in all_contents:
                result+=content.strip()
        a={
            "content":content,
            "img_url":img_url,
            "content_url":result
        }
    else:


        result=[]
        r1=requests.get(link)
        s1=BeautifulSoup(r1.text,'html.parser')
        c1=s1.find(class_='sub-title')
        c2=s1.find(class_="articlebodycontent")
        p=c2.find_all('p')
        c3="  "
        for j in p:
            if(j.string):
                c3+=j.string
        p1=s1.find('picture')
        img_url=None
        if(p1):
            p2=p1.find('source')
            img_url=p2['srcset']
        a={
            "content":c1.string,
            "img_url":img_url,
            "content_url":c3
        }
    
    return a

