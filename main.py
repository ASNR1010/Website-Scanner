from general import *
from domain_name import *
from ip_address import *
from nmap import *
from robots_txt import *
from whois import *
import time

ROOT_DIR = "Websites"
create_dir(ROOT_DIR)   #if it is not created than create it
gather_info_time = 0
generating_report_time = 0

def gather_info(name, url):  # "name" is the folder name which user wants to give and "url" contains the url of website you want to scan
    global gather_info_time 
    start_time = time.time()
    print("\n\nGATHERING WEBSITE INFO...\n")
    domain_name = get_domain_name(url)  # this will give top level domain
    ip_address = get_ip_address(url)
    nmap = get_nmap("-F", domain_name) 
    robots_txt = get_robots_txt(url)
    whois = get_whois(domain_name) #this will neeed top level domain name
    end_time = time.time()
    gather_info_time = (end_time - start_time)
    print("GATHERING INFO COMPLETED IN %s seconds\n\n" %gather_info_time)
    create_report(name, url, domain_name, nmap, robots_txt, whois)  

def create_report(name, full_url, domain_name, nmap, robots_txt, whois):  
    global generating_report_time 
    start_time1 = time.time()	
    print("GENERATING REPORT...\n") 	
    project_dir = ROOT_DIR + "/" + name
    create_dir(project_dir)
    write_file(project_dir + "/full_url.txt", full_url)       # write_file(path, data)
    write_file(project_dir + "/domain_name.txt", domain_name)
    write_file(project_dir + "/nmap.txt", nmap)
    write_file(project_dir + "/robots_txt.txt", robots_txt)
    write_file(project_dir + "/whois.txt", whois)
    end_time1 = time.time()
    generating_report_time = (end_time1 - start_time1)
    print("GATHERING INFO COMPLETED IN %s seconds\n\n" %generating_report_time)
    print("TOTAL TIME TAKEN = %s seconds\n\n" %(gather_info_time + generating_report_time))
        
gather_info("IIT BHU", "https://www.iitbhu.ac.in/")   # you can write '/' or not depends on you

