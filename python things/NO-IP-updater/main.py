import urllib
import socket
import os.path
import base64

############################
############################
####    ####    ####    ####
####    ####    ####    ####
####    ####    ####    ####
####            ####    ####
####            ####    ####
####    ####    ############
####    ####    ####    ####
####    ####    ####    ####
############################
############################

print "No-IP Updater\nVersion 1.0.0\nBy Cesar Vasquez C. - Heellxz (heellxz@gmail.com)\n"

#FIND No-IP.ini
if os.path.exists("No-IP.ini") == True:
    old = raw_input("Use your old No-IP Information? (y/n): ")
    if old == "y":
        fx = open("No-IP.ini", "r")
        fy = fx.read()
        fz = fy.split(":")
        domain = fz[0]
        user = fz[1]
        pswd = base64.b64decode(fz[2])
        fx.close()
        print "No-IP Domain: " + domain + "\nNo-IP Email: " + user + "\nPassword: ********"
else:
#GETTING DOMAIN DATA
        domain = raw_input("Enter No-IP Domain (EJ: shukra.no-ip.biz): ")
        user = raw_input("Enter No-IP Email: ")
        pswd = raw_input("Enter No-IP Password: ")

#GETTING CURRENT IP
myip = socket.gethostbyname(socket.gethostname())

#GETTING REQUEST FORMAT
request = urllib.urlencode({"hostname": domain, "myip": myip})

#MAKING PETITION
peticion = urllib.urlopen("http://"+user+":"+pswd+"@dynupdate.no-ip.com/nic/update",request)

aux = peticion.read()
if "good" in aux:
    print "DNS hostname update successful."
if "nochg" in aux:
    print "IP address is current, no update performed."
if "nohost" in aux:
    print "Hostname supplied does not exist under specified account."
if "badauth" in aux:
    print "Invalid username password combination."
if "badagent" in aux:
    print "Client disabled."
if "!donator" in aux:
    print "An update request was sent including a feature that is not available to that particular user such as offline options."
if "abuse" in aux:
    print "Username is blocked due to abuse."
if "911" in aux:
    print "A fatal error on No-IP server. Retry the update no sooner 30 minutes."


save = raw_input("Save your No-IP user information? (y/n): ")
if save == "y":
    f = open("No-IP.ini", "w")
    f.write(domain+":"+user+":"+base64.b64encode(pswd))
    f.close()
    print "Adieu !"
else:
    print "Adieu !"