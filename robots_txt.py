import urllib.request  # make a request to url
import io   # to get a readable format 

def get_robots_txt(url):  
    if url.endswith('/'):  # this is just make it ending with '/'
        path = url
    else:
        path = url + '/'
    req = urllib.request.urlopen(path + "robots.txt", data=None)
    data = io.TextIOWrapper(req, encoding='utf-8') # utf-8 standard encoding 
    print("Getting robots_txt ...")
    return data.read()
