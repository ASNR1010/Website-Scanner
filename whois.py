import os

def get_whois(url):  #this url is top level domain
    command = "whois " + url
    process = os.popen(command) # this will open a new process and return the result
    results = str(process.read()) 
    print("Getting whois...")
    return results
