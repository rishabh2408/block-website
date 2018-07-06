import time
from datetime import datetime as dt

def block(start_time,end_time,web_list):
	
	hosts_path=r"C:\Windows\System32\drivers\etc\hosts"
	redirect="127.0.0.1"
	while True:
		if start_time <= dt.now().hour < end_time :
			
			with open(hosts_path,'r+') as file:
				content=file.read()
				for website in web_list:
					if website in content:
						pass
					else:
						file.write(redirect+" "+website+"\n")
						
						
		else:
			
			with open(hosts_path,'r+') as file:
				content=file.readlines()
				file.seek(0)
				for line in content:
					if not any(website in line for website in web_list):
						file.write(line)
						
				file.truncate()
		time.sleep(5)
if __name__=="__main__":
	block(10,17,['www.facebook.com'])