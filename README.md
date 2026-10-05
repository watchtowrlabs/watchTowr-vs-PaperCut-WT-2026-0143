# WT-2026-0143/WT-2026-0142/CVE-2026-81578 PaperCut Authentication Bypass

PaperCut Authentication Bypass 1day Detection Artifact Generator Tool
 

# Detection in Action

Detection Artifact Generator attempts to access arbitrary forms through the `/Home` page, to verify if `/Home` can be used as a bridge to a different page:
* 200 response and page name in the response - vulnerable
* 302 response and redirect to the `/Home` related endpoint - not vulnerable

Script was tested on:
* PaperCut NG 26.0.3, 26.0.4, 26.0.4-PO build 76508 and 26.0.4-PO build 76530.

PaperCut MF and older branches (e.g. 25) were not tested.

This vulnerability leads to the full Pre-Auth RCE chain when chained with either CVE-2026-82078, WT-2026-0141 or CVE-2026-82077. This script does not attempt to achieve RCE, it only verifies if authentication bypass can be exploited.

You need to provide following inputs:
* `-H` - target host.

Sample run against vulnerable instance:

```
$ python3 watchTowr-vs-PaperCut-WT-2026-0143.py -H http://papercut.vuln.lab:9191
                         __         ___  ___________                   
         __  _  ______ _/  |__ ____ |  |_\__    ____\____  _  ________ 
         \ \/ \/ \__  \    ___/ ___\|  |  \|    | /  _ \ \/ \/ \_  __ \
          \     / / __ \|  | \  \___|   Y  |    |(  <_> \     / |  | \/
           \/\_/ (____  |__|  \___  |___|__|__  | \__  / \/\_/  |__|   
                                  \/          \/     \/                            
          
        watchTowr-vs-PaperCut-WT-2026-0143.py
        (*) WT-2026-0143/WT-2026-0142/CVE-2026-81578 - PaperCut Authentication Bypass Detection Artifact Generator

          - Piotr (@chudyPB) of watchTowr (@watchTowrcyber)

[+] Starting WT-2026-0143/WT-2026-0142/CVE-2026-81578 DAG
[+] Getting JSESSIONID cookie from /app endpoint
[+] Trying to access ConfigEditor/quickFindForm with authentication bypass
[+] VULNERABLE - Home page can be used to access arbitrary forms
```

Sample run against patched instance:

```
$ python3 watchTowr-vs-PaperCut-WT-2026-0143.py -H http://papercut.patched.lab:9191
                         __         ___  ___________                   
         __  _  ______ _/  |__ ____ |  |_\__    ____\____  _  ________ 
         \ \/ \/ \__  \    ___/ ___\|  |  \|    | /  _ \ \/ \/ \_  __ \
          \     / / __ \|  | \  \___|   Y  |    |(  <_> \     / |  | \/
           \/\_/ (____  |__|  \___  |___|__|__  | \__  / \/\_/  |__|   
                                  \/          \/     \/                            
          
        watchTowr-vs-PaperCut-WT-2026-0143.py
        (*) WT-2026-0143/WT-2026-0142/CVE-2026-81578 - PaperCut Authentication Bypass Detection Artifact Generator

          - Piotr (@chudyPB) of watchTowr (@watchTowrcyber)

[+] Starting WT-2026-0143/WT-2026-0142/CVE-2026-81578 DAG
[+] Getting JSESSIONID cookie from /app endpoint
[+] Trying to access ConfigEditor/quickFindForm with authentication bypass
[-] NOT VULNERABLE - Home with arbitrary forms redirects to /Home endpoint
```


# Description

This script attempts to detect if PaperCut is vulnerable to one of following Authentication Bypasses: WT-2026-0143, WT-2026-0142, or CVE-2026-81578.


# Affected Versions

According to the latest [vendor advisory](https://www.papercut.com/kb/Main/security-bulletin-27-aug-2026-urgent-security-advisory/):

* PaperCut NG/MF 26.05, 25.0.13 and 24.1.10 are NOT VULNERABLE
* Versions below are VULNERABLE.

According to our knowledge, intermediate build 26.0.4-PO build 76530 was also NOT VULNERABLE. However, this hasn't been stated officially by the PaperCut team, so there is a chance that a bypass may exist for this build.

# Follow [watchTowr](https://watchTowr.com) Labs

For the latest security research follow the [watchTowr](https://watchTowr.com) Labs Team 

- https://labs.watchtowr.com/

- https://x.com/watchtowrcyber
