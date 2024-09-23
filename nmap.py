import os

def get_nmap(options, ip):  #nmpa has -F option. So, we let user decide which option he wants
    command = "nmap " + options + " " + ip
    process = os.popen(command)
    results = str(process.read()) #it will store in string format
    print("Getting nmap ...")
    return results
