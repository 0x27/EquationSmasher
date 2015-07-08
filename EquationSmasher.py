#!/usr/bin/python2
# coding: utf-8
import shodan

print """
 ________                                  __      __                           
/        |                                /  |    /  |                          
$$$$$$$$/   ______   __    __   ______   _$$ |_   $$/   ______   _______        
$$ |__     /      \ /  |  /  | /      \ / $$   |  /  | /      \ /       \       
$$    |   /$$$$$$  |$$ |  $$ | $$$$$$  |$$$$$$/   $$ |/$$$$$$  |$$$$$$$  |      
$$$$$/    $$ |  $$ |$$ |  $$ | /    $$ |  $$ | __ $$ |$$ |  $$ |$$ |  $$ |      
$$ |_____ $$ \__$$ |$$ \__$$ |/$$$$$$$ |  $$ |/  |$$ |$$ \__$$ |$$ |  $$ |      
$$       |$$    $$ |$$    $$/ $$    $$ |  $$  $$/ $$ |$$    $$/ $$ |  $$ |      
$$$$$$$$/  $$$$$$$ | $$$$$$/   $$$$$$$/    $$$$/  $$/  $$$$$$/  $$/   $$/       
                $$ |                                                            
                $$ |                                                            
                $$/                                                             
  ______                                     __                                 
 /      \                                   /  |                                
/$$$$$$  | _____  ____    ______    _______ $$ |____    ______    ______        
$$ \__$$/ /     \/    \  /      \  /       |$$      \  /      \  /      \       
$$      \ $$$$$$ $$$$  | $$$$$$  |/$$$$$$$/ $$$$$$$  |/$$$$$$  |/$$$$$$  |      
 $$$$$$  |$$ | $$ | $$ | /    $$ |$$      \ $$ |  $$ |$$    $$ |$$ |  $$/       
/  \__$$ |$$ | $$ | $$ |/$$$$$$$ | $$$$$$  |$$ |  $$ |$$$$$$$$/ $$ |            
$$    $$/ $$ | $$ | $$ |$$    $$ |/     $$/ $$ |  $$ |$$       |$$ |            
 $$$$$$/  $$/  $$/  $$/  $$$$$$$/ $$$$$$$/  $$/   $$/  $$$$$$$/ $$/             
                                                                       
     Using the SHODAN API to identify NSA/Equation APT C&C Servers."""


SHODAN_API_KEY = "" # your key here
api = shodan.Shodan(SHODAN_API_KEY)
try:
    # Search Shodan
    results = api.search('Microsoft-IIS/7.5 401 Content-Length: 1293 -X-Powered-By -NTLM -WWW-Authenticate Cache-Control: no-cache -private -public')

    # Show the results
    print '{+} NSA C&C FOUND: %s' % results['total']
    for result in results['matches']:
            print '{!} NSA C&C DISCOVERED: %s' % result['ip_str']
            # you could add a function to own them here ;)
except shodan.APIError, e:
    print 'Error: %s' % e # we shouldn't ever get here. but then again... Shodan's API does tend to flake out every so often.
