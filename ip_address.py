import os

def get_ip_address(url):
    command = "host " + url  #this url is top level domain
    process = os.popen(command)  # in order to run the command and result back we need the new process
    results = str(process.read()) 
    marker = results.find("has address") + 12 #this will set the marker after has address 
    print("Getting IP address ...")
    return results[marker:].splitlines()[0]  # Now, we print the result from marker onwards and splitlines[0] because if some websites has more than 1 IP address then we only need the top one 

# print(get_ip_address("google.com"))