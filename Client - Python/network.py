# ******************************************************
#
# The Network module handles communication with the server
#
# ******************************************************

#Set the base url
base_url = "https://projects.joshheng.co.uk/musicquiz/api"

#Import libraries
import variables, urllib.parse, urllib.request, hashlib, base64, json, ssl, html

#Disable SSL certificate checking as the school network dangerously reissues certificates
sslcontext = ssl.create_default_context()
sslcontext.check_hostname = False
sslcontext.verify_mode = ssl.CERT_NONE

#Gets a list of songs from the server
def GetSongs():
    url = base_url + "/getSongs.php"
    
    result = GetURL(url, None)

    if (result['success']):
        if (result['md5'] == CheckMD5(json.dumps(result['songs'], separators=(',', ':')).replace("/", "\/"))):

            decodedsongs = []
            
            for song in result['songs']:
                artist = variables.CapitaliseName(html.unescape(song[0].lower()))
                title = variables.CapitaliseName(html.unescape(song[1].lower()))
                decodedsong = [artist, title]
                
                decodedsongs.append(decodedsong)

            return decodedsongs

    return False

#Attempts a user login attempt
def AttemptLogin(username, password):
    url = base_url + "/attemptLogin.php"

    passwordHash = GetPasswordHash(username, password)
    md5 = GetMD5(username + passwordHash)
    data = {
        'username':username,
        'password':passwordHash,
        'md5':md5
    }
    
    result = GetURL(url, data)

    if (result['credentials'] == 'true' and result['success'] == 'true'):
        if (result['md5'] == CheckMD5(username + result['authorised'] + result['highscore'] + result['token'])):
            user = {
                'username':username,
                'highScore':result['highscore'],
                'authorised':result['authorised'] == 'true',
                'token':result['token']
            }
            return user
        else:
            return None
            
    else:
        return None

#Attempts to registrate a user
def AttemptRegistration(username, password):
    url = base_url + "/attemptRegistration.php"

    passwordHash = GetPasswordHash(username, password)
    md5 = GetMD5(username + passwordHash)
    data = {
        'username':username,
        'password':passwordHash,
        'md5':md5
    }
    
    result = GetURL(url, data)
    if (result['success'] == 'true'):
        return 'good'
    else:
        return result['error']

#Uploads the user score to the server and returns the leaderboard
def SyncScores(token, score):
    score = str(score)
    url = base_url + "/syncScores.php"

    md5 = GetMD5(token + score)
    data = {
        'token':token,
        'score':score,
        'md5':md5
    }
    
    result = GetURL(url, data)
    
    if (result['success'] == 'true'):
        if (result['authenticated'] == 'true'):
            if (result['md5'] == CheckMD5("[" +
                                          json.dumps(result['leaderboard'], separators=(',', ':')) +
                                          "," +
                                          json.dumps(result['player'], separators=(',', ':')) +
                                          "]")):
                return [result['leaderboard'], result['player']]
    return "error"
    
#Get a URL using a POST request
def GetURL(url, data):
    try:
        #Pretend to be Mozilla to get past firewalls
        user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
        headers={'User-Agent':user_agent}

        #Encode POST data
        if (data == None):
            data = None
        else:
            data = urllib.parse.urlencode(data)
            data = data.encode('utf-8')

        #Create and send request
        request = urllib.request.Request(url, data, headers)
        response = urllib.request.urlopen(request, context=sslcontext)

        #Convert data received to json and return
        data = json.loads(response.read().decode(response.info().get_param('charset') or 'utf-8'))
        return data
    except:
        return False

#Get the client MD5 value to prevent tampering
def GetMD5(string):
    string = string + "asjioj9821u9j0faslf0921irasf" + string[2] + string[0].upper() + "amko!98"
    md5 = hashlib.md5(string.encode()).hexdigest()
  
    return md5

#Check a server MD5 value to prevent tampering
def CheckMD5(string):
    string = string + "3s14109dlf" + string[2].lower() + "asjdo"
    md5 = hashlib.md5(string.encode()).hexdigest()

    return md5

#Hashes a password
def GetPasswordHash(username, password):
    salt = username[3] + "ncuai2y9" + password[4] + username[1] + username + "duiasdah"
    hashed = hashlib.pbkdf2_hmac("sha512", password.encode(), salt.encode(), 100000)

    return base64.b64encode(hashed).decode()

