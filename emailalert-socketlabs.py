#!C:\progra~1\Splunk\bin\python
#Should be /opt/splunk/bin/python on *nix or C:\progra~1\Splunk\bin\python on *indows.
import sys, urllib, urllib2, json


#Socketlabs api key
apiKey = "API KEY GOES HERE"
#Socketlabs server id
serverID = "SERVER ID GOES HERE"

#Email being sent to
toEmail = "EMAIL GOES HERE"

#Email being sent from.
fromEmail = "SplunkAlerts@gmail.com"


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
d = json.dumps({
    "ServerId": serverID,
    "ApiKey": apiKey,
    "Messages": [{
        "Subject": "Splunk Alert!: " + searchTerms,
        "HtmlBody": "<h2>"+searchReason+"</h2></br><a>"+ searchURL +"</a>",
        "To": [{
            "EmailAddress": toEmail,
        }],
        "From": {
            "EmailAddress": fromEmail,
        }
    }]
})

#socketlabs endpoint url.
url = "https://inject.socketlabs.com/api/v1/email"

#POST data
req = urllib2.Request(url, d, {'Content-Type': 'application/json'})
f = urllib2.urlopen(req)
response = f.read()
f.close()
