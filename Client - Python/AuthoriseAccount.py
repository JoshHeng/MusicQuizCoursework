#Constants
url = "https://projects.joshheng.co.uk/musicquiz/api/authoriseUser.php"
key = "dasji21u98DAj2989fjsaFAu985ufASJFoj"

#Import libraries
import urllib.parse, urllib.request, json, ssl

#Disable SSL certificate checking as the school network dangerously reissues certificates
sslcontext = ssl.create_default_context()
sslcontext.check_hostname = False
sslcontext.verify_mode = ssl.CERT_NONE

#Send an authorisation request to the server
def AuthoriseUser(username):
    username = username.lower()
    try:
        #Pretend to be Mozilla to get past firewalls
        user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
        headers={'User-Agent':user_agent}

        #Encode POST data
        data = urllib.parse.urlencode({'username':username, 'key':key})
        data = data.encode('utf-8')

        #Create and send request
        request = urllib.request.Request(url, data, headers)
        response = urllib.request.urlopen(request, context=sslcontext)

        #Convert data received to json and return if successful
        data = json.loads(response.read().decode(response.info().get_param('charset') or 'utf-8'))
        
        if (data['success'] and data['success'] == 'true'):
            return True
        else:
            return False
    except:
        return False

#User interaction
username = input("Please enter the username of the account you would like to authorise: ")
if (AuthoriseUser(username)):
    print("User authorised")
else:
    print("Error occured")


