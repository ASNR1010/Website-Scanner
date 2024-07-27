from tld import get_fld 
 # tld is a package which gives get_tld function (tld means top level domain which does not include http OR https or anthing extra.)

def get_domain_name(url):
    domain_name = get_fld(url)
    print("Getting domain Name ...")
    return domain_name

# print(get_domain_name('https://google.com/'))