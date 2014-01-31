#!C:\progra~1\Splunk\bin\python
#Should be /opt/splunk/bin/python on *nix or C:\progra~1\Splunk\bin\python on *indows.
import sys, urllib, urllib2


#Twilio account SID
twilioID = "AC5c34481171314f4a5c7907f137eb4f10"
#Auth Token
twilioPW = "a3464ca38a05c4fae5cb55f25f8a481c"

#Number to send the SMS to
toNumber = "+14196317771"

#Number to send the SMS FROM 
fromNumber = "+13305295389"

alertText = "Splunk Alert:"


# Parameters passed in from the alert.
searchCount = sys.argv[1] # 1 - Number of events returned
searchTerms = sys.argv[2] # 2 - Search terms
searchQuery = sys.argv[3] # 3 - Fully qualified query string
searchName = sys.argv[4] # 4 - Name of saved search
searchReason = sys.argv[5] # 5 - Reason saved search triggered
searchURL = sys.argv[6] # 6 - URL/Permalink of saved search
searchTags = sys.argv[7] # 7 - Always empty
searchPath = sys.argv[8] # 8 - Path to raw saved results in Splunk instance (advanced)

#construct JSON data to send.
d = urllib.urlencode({"From" : fromNumber, "To" : toNumber, "Body" : alertText + " "+searchReason})
#authentication 
pwm = urllib2.HTTPPasswordMgrWithDefaultRealm()
pwm.add_password("Twilio API", "https://api.twilio.com/2010-04-01/Accounts/", twilioID, twilioPW)
hnd = urllib2.HTTPBasicAuthHandler(pwm)
#POST data
opn = urllib2.build_opener(hnd)
f = opn.open("https://api.twilio.com/2010-04-01/Accounts/" + twilioID + "/SMS/Messages", d)
f.close()
