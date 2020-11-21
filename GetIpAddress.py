import re

ip_regex = "^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$"
      
def GetIpAddress(ip):  
    ip_check = False
    while not ip_check:
        ip = input(ip)
        if re.search(ip_regex, ip):  
            print(f"{ip} is valid IPv4 address")
            ip_check = True       
        else:  
            print(f"{ip} is invalid IPv4 address")
            continue  
        
user_ip = GetIpAddress("Enter IPv4 address:\n>>")