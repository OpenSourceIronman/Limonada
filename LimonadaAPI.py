#!/usr/bin/env python3

__author__ =  "Blaze Sanders"
__email__ =   "blaze.d.a.sanders@gmail.com"
__company__ = "Unlimited Custom Creations"
__status__ =  "Development"
__date__ =    "Late Updated: 2021-06-08"
__doc__ =     "Class to GET and POST data from a JSON web API"

# Allow encoding and decoding of a RESTFUL JSON data format
# https://docs.python.org/3/library/json.html
import json

# urllib3 is a powerful, sanity-friendly HTTP client for Python
# https://urllib3.readthedocs.io/en/latest/
import urllib3

# Allow program pausing & timestamp generation for data logging
# https://docs.python.org/3/library/time.html
# https://docs.python.org/3/library/datetime.html
import time
import datetime

# Allow program to extract filename of the current file
# https://docs.python.org/3/library/os.html
import os

try:
	# Generate .txt data logging and custom terminal debugging output
	from Debug import *
	#TODO

except ImportError:
	thisCodesFilename = os.path.basename(__file__)


class LimonadaAPI:

	# System architecture CONSTANTS
	KIOSK_DEVICE_ID = 1

	# Timezone helper CONSTANTS
	INTERNET_TIME = 0
	MANUAL_TIME = 1

	# Access Point CONSTANTS
	# List of Device Names and ID that you can perform http.GET on
	ACCESS_POINTS_URL = 'https://nomcon.foballthethings.org/api/accesspoints/'
	# Define dictionary for parameters being sent to the ACCESS_POINTS_URL
	ACCESS_POINTS_PARAMS = {'id': 'value', 'created_date': 'value','modified_date': 'value','name': 'value', 'location': 'value', 'verb': 'value'}	
	# The max number of devices hardcoded into the AccessPoint API
	MAX_NUMBER_OF_DEVICES = 8

	#
	# List of valid RFID fob UID's in hex format that you can perform http.GET on
	CREDENTIALS_URL = 'https://nomcon.foballthethings.org/api/credentials/'
	# Define dictionary for parameters being sent to the CREDENTAILS_URL
	CREDENTIALS_PARAMS = {'id': 'value', 'created_date': 'value','modified_date': 'value', 'encodedCredential': 'value'}
	# The number of IDs hardcoded into the Credentials API
	MAX_NUMBER_OF_CREDENTIALS = 503
	# This CONSTANT value is returned if credential is NOT FOUND
	CREDENTIALS_ID_NOT_FOUND = -1

	# Location for datalog that user RFID scans that you can perform http.POST on
	DATA_LOG_URL = 'https://nomcon.foballthethings.org/api/activitylistings/'

	# Highest level API URL
	API_ENDPOINT = 'https://nomcon.foballthethings.org/api/'

	# Security Key to allow POSTing to API
	API_KEY = 'Token 2e77c0656e0549e4cefadfac979ccc622b98b07f'

	# Django uses one indexed arrays and Python uses zero index arrays
	DJANGO_PYTHON_ARRAY_OFFSET = 1

	# Highest level JSON value definitions
	SwaggerHeaders = {  	'Content-Type': 'application/json',
            			'Accept': 'application/json',
            			'Allow': 'GET, POST, HEAD, OPTIONS',
            			'Authorization': 'Token 2e77c0656e0549e4cefadfac979ccc622b98b07f'}


	def getTime(timeSource):
		"""
		Get current time
	# CONSTANTS to manually adjust timezone project is running in, if internet not working

		timeSource - Select INERNET_TIME or MANUAL_TIME contnts as true time of device

		return String variable with time formatted in iso8601 format
		"""
		if(timeSource == INTERNET_TIME):
        		timeStamp = time.time()
        		iso8601DateTime = datetime.datetime.fromtimestamp(timeStamp).strftime('%Y-%m-%d %H:%M:%S')
			message = "Current Time is: " + iso8601DateTime
        		Debug.Dprint(message)
        		return iso8601DateTime
    		elif(timeSource == MANUAL_TIME):
        		debugPrint("TODO MANUAL TIME ZONE UPDATING")
        		#TODO timezoneOffsett = ?-7? Zulu -7 or PT +3
        	#TODO return iso8601DateTime + timeZoneOffset
    		else:
        		print("INVALID timeSource parameters sent to getTime method, please use INTERNET_TIME or MANUAL_TIME")


	###
	# Convert Django ONE indexed array notation into Python ZERO indexed array notation
#
# return interger value of expected index
###
	def djangoToPythonIndexConversion(djangoIndex):
    	return djangoIndex - DJANGO_PYTHON_ARRAY_OFFSET

###
# Convert Python ZERO indexed array notation into Django ONE indexed array notation
#
# return interger value of expected index
###
def pythonToDjangoIndexConversion(pythonIndex):
    return pythonIndex + DJANGO_PYTHON_ARRAY_OFFSET


    ###
    # Constructor to initialize an Database object
    #
    # @self - Newly created object
    # @url - Highest level URL of API level you are attempting to read (GET) or write (POST) to
    #
    # url - URL documentation, not actually used in code (as of June 9, 2019)
    # httpObject - urlllib3 object used to perfom .request('POST') & .request('GET') commands
    # credentialsDict - Python Dictionary to hold fob ID whitelist locally
    #
    # return NOTHING
    ###
    def __init__(self, url):
        self.url = url
        self.httpObject = urllib3.PoolManager()
        self.credentialsDict = {}
		self.timeZone = 'PT' # or 'CT' or 'Zulu'

    ###
    # Search credentialsDict (a python Dictionary) for HEX whitelisted fobIDs
    #
    # @fobID - HEX Fob UID you are searching for (e.g. 002AC13)
    #
    # Return Interger variable with database ID if fobID is in the  whitelist, -1 OTHERWISE
    ###
    def getAutoGeneratedDatabaseID(self, fobID):
        try:
            # Not optimized! Searches entire dictionary in O(1) time
            for id in range(0, MAX_NUMBER_OF_CREDENTIALS):
                if(self.credentialsDict[id]['encodedCredential'] == fobID):
                    return self.credentialsDict[id]['id']
        except IndexError as error:
            print("ERROR THERE ARE ONLY 503 CREDENTIALS")
            return CREDENTIALS_ID_NOT_FOUND
        except Exception as exception:
            print("SOMETHING WEIRD HAPPENED MOVE TO MARS!")
            return CREDENTIALS_ID_NOT_FOUND
        #return self.credentialsDict.get(fobID, "CREDENTIALS_ID_NOT_FOUND").id


    ###
    # POST data to https://nomcon.foballthethings.org/api/activitylistings/
    #
    # @id - Autofenerated database id to log
    #
    # return HTTP Status Code of POSY attempt (201 is good)
    ###
    def postDataLog(self, id):
        data = {'credential': id,
            'access_point': THIS_PROJECTS_DEVICE_ID}
        encoded_data = json.dumps(data).encode('UTF-8')
        dataToPOST = self.httpObject.request(   'POST',
                            DATA_LOG_URL,
                            body = encoded_data,
                            headers = SwaggerHeaders)
        http_status = dataToPOST.status

        #201 means data POSTed https://httpstatuses.com/201
        print(http_status)


    ###
    # GET data from https://nomcon.foballthethings.org/api/credentials/
    # and store in the Python Dictionary "crenedtialsDict" in Database object
    #
    # return NOTHING
    ###
    def getCredentials(self):

        fobWhiteList = self.httpObject.request( 'GET',
                            CREDENTIALS_URL,
                            CREDENTIALS_PARAMS)

        self.credentialsDict = json.loads(fobWhiteList.data.decode('UTF-8'))
        #debugPrint("Print Dictionary 1 id and encodedCredentials:")
        #debugPrint(fobWhiteListDict[djangoToPythonIndexConversion(1)]['encodedCredential'])
        #debugPrint(fobWhiteListDict[djangoToPythonIndexConversion(1)]['id'])


if __name__ == "__main__":
    print("STARTING Database.py MAIN FUNCTION AT " + getTime(INTERNET_TIME))

    # Create database object to use functions above
    api = Database(API_ENDPOINT)
    api.getCredentials()

    # In Python 3, leading zeros are not allowed on integer (e.g. 0002755603)
    # UID = 2755603 #hex(0002755603) #002AC13 #2755603 #4 #str(0x002A0C13)
    hexFobID = "0028130D"
    databaseID = api.getAutoGeneratedDatabaseID(hexFobID)
    debugPrint(databaseID)

    if(databaseID != CREDENTIALS_ID_NOT_FOUND):
        api.postDataLog(databaseID)
    else:
        print("HEX code UID not found in Whitelist")

    print("ENDING Database.py MAIN FUNCTION")


# 1. GET /api/credentials, which is the whitelist of hex values and their associated ID in our system.
# 2. When a fob is swiped, find that value in the whitelist you pulled down and get the ID mapped to it.
# 3. POST to /api/activitylistings with the ID you just got and the hard-coded "access point ID" (ranging from 1-8 currently) so we know which fob and which device was swiped.

# POSTing to api/credentials would only add a fob to the whitelist.  There is no access point ID in that endpoint anywhere.

# When you hit /api/credentials, you'll get a list back like the following

# {"id":"200","encodedCredential":"1f00001111"},{"id":"201","encodedCredential":"002915D6"}

# Store that in an array somewhere.  Then when you swipe the fob, it will transmit a value which I believe is either in hex or 
# needs to be converted to hex, not sure.  So say it transmits "1f00001111", you'll find in your array that it is id 200.  
# And if you're coding the Kraken, you know the access point ID is 2, so you can post the "200" and the "2" to the 
# /api/activitylistings endpoint so we get the fob and the device.
