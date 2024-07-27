from general import *
from domain_name import *
from ip_address import *
from nmap import *
from robots_txt import *
from whois import *

ROOT_DIR = "companies"
create_dir(ROOT_DIR)   #if it is not created than create it

def gather_info(name, url):  # "name" is the folder name which user wants to give and "url" contains the url of website you want to scan
    domain_name = get_domain_name(url)  # this will give top level domain
    ip_address = get_ip_address(url)
    nmap = get_nmap("-F", domain_name) 
    robots_txt = get_robots_txt(url)
    whois = get_whois(domain_name) #this will neeed top level domain name
    create_report(name, url, domain_name, nmap, robots_txt, whois)  

def create_report(name, full_url, domain_name, nmap, robots_txt, whois):  
    project_dir = ROOT_DIR + "/" + name
    create_dir(project_dir)
    write_file(project_dir + "/full_url.txt", full_url)       # write_file(path, data)
    write_file(project_dir + "/domain_name.txt", domain_name)
    write_file(project_dir + "/nmap.txt", nmap)
    write_file(project_dir + "/robots_txt.txt", robots_txt)
    write_file(project_dir + "/whois.txt", whois)
        
gather_info("Google", "https://www.google.com/")   # you can write '/' or not depends on you

