import json
import datetime
import ibm_boto3
from ibm_botocore.client import Config, ClientError
import cv2
import numpy as np
import sys
import ibmiotf.application
import ibmiotf.device
import random
import time
from cloudant.client import Cloudant
from cloudant.error import CloudantException 
from cloudant.result import Result, ResultByKey
from ibm_watson import VisualRecognitionV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import TextToSpeechV1

from playsound import playsound
#Provide your IBM Watson Device Credentials
organization = "wk8zhy"
deviceType = "RSIP"
deviceId = "10110"
authMethod = "token"
authToken = "EmCee9932"
def myCommandCallback(cmd):
        print("Command received: %s" % cmd.data)
        print(cmd.data['command'])
        
        if(cmd.data['command']=="Servomotoron"):
                print("Servo motor on")
        if(cmd.data['command']=="Servomotoroff"):
                print("Servo motor off")
try:
	deviceOptions = {"org": organization, "type": deviceType, "id": deviceId, "auth-method": authMethod, "auth-token": authToken}
	deviceCli = ibmiotf.device.Client(deviceOptions)
	#..............................................
	
except Exception as e:
	print("Caught exception connecting device: %s" % str(e))
	sys.exit()
# Connect and send a datapoint "hello" with value "world" into the cloud as an event of type "greeting" 10 times
deviceCli.connect()
COS_ENDPOINT = "https://s3.jp-tok.cloud-object-storage.appdomain.cloud" # Current list avaiable at https://control.cloud-object-storage.cloud.ibm.com/v2/endpoints
COS_API_KEY_ID = "0r1Q3G0T5VS5fEoNKlCbVYWxLkWYi7MeQnnhJBvRUzY_" # eg "W00YiRnLW4a3fTjMB-oiB-2ySfTrFBIQQWanc--P3byk"
COS_AUTH_ENDPOINT = "https://iam.cloud.ibm.com/identity/token"
COS_RESOURCE_CRN = "crn:v1:bluemix:public:cloud-object-storage:global:a/61fbb0885ad945358fd3f70f049c1d84:20842b15-b746-469c-af7e-30ee83df189f::"
authenticator1 = IAMAuthenticator('0r1Q3G0T5VS5fEoNKlCbVYWxLkWYi7MeQnnhJBvRUzY_')
visual_recognition = VisualRecognitionV3(
    version='2018-03-19',
    authenticator=authenticator1
)
visual_recognition.set_service_url('https://api.us-south.visual-recognition.watson.cloud.ibm.com/instances/6d315cce-6b35-43d4-a4c2-127c66dce577')
client = Cloudant("4245f642-3442-4182-99d1-18383673c9aa-bluemix", "0a10750da8c7467d7253b8a599c907e6607e2a573961df25578282b30bb6347f", url="https://4245f642-3442-4182-99d1-18383673c9aa-bluemix:0a10750da8c7467d7253b8a599c907e6607e2a573961df25578282b30bb6347f@4245f642-3442-4182-99d1-18383673c9aa-bluemix.cloudantnosqldb.appdomain.cloud")
client.connect()
database_name = "smartrecognition"
picname=datetime.datetime.now().strftime("%y-%m-%d-%H-%M")
picname=picname+".jpg"
pic=datetime.datetime.now().strftime("%y-%m-%d-%H-%M")
# Create resource
cos = ibm_boto3.resource("s3",
    ibm_api_key_id=COS_API_KEY_ID,
    ibm_service_instance_id=COS_RESOURCE_CRN,
    ibm_auth_endpoint=COS_AUTH_ENDPOINT,
    config=Config(signature_version="oauth"),
    endpoint_url=COS_ENDPOINT
)
def multi_part_upload(bucket_name, item_name, file_path):
    try:
        print("Starting file transfer for {0} to bucket: {1}\n".format(item_name, bucket_name))
        # set 5 MB chunks
        part_size = 1024 * 1024 * 5
        # set threadhold to 15 MB
        file_threshold = 1024 * 1024 * 15
        # set the transfer threshold and chunk size
        transfer_config = ibm_boto3.s3.transfer.TransferConfig(
            multipart_threshold=file_threshold,
            multipart_chunksize=part_size
        )
        # the upload_fileobj method will automatically execute a multi-part upload
        # in 5 MB chunks for all files over 15 MB
        with open(file_path, "rb") as file_data:
            cos.Object(bucket_name, item_name).upload_fileobj(
                Fileobj=file_data,
                Config=transfer_config
            )
        print("Transfer for {0} Complete!\n".format(item_name))
    except ClientError as be:
        print("CLIENT ERROR: {0}\n".format(be))
    except Exception as e:
        print("Unable to complete multi-part upload: {0}".format(e))
cam = cv2.VideoCapture(0)
cv2.namedWindow("Detection")

authenticator = IAMAuthenticator('Cp5pWRCW5x0ZCTzCEciFWJHReTPGaJYtBKSKVcSKJwLV')
text_to_speech = TextToSpeechV1(authenticator=authenticator)
text_to_speech.set_service_url('https://api.eu-gb.text-to-speech.watson.cloud.ibm.com/instances/9f80d26e-e18e-433a-aae7-ccee0693fb29')
person=1
global vy
vy=0
while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("Dectection", frame)
    
    k = cv2.waitKey(1) & 0xFF
    if  k== ord('q'):
        # q pressed
        print("q hit, closing...")
        break
    else:
        
        picname=datetime.datetime.now().strftime("%y-%m-%d-%H-%M")
        picname=picname+".jpg"
        pic=datetime.datetime.now().strftime("%y-%m-%d-%H-%M")
        cv2.imwrite(picname, frame)
        print("{} written!".format(picname))
        with open(picname, 'rb') as images_file:
            classes = visual_recognition.classify(
                images_file=images_file,
                threshold='0.6').get_result()
        print(json.dumps(classes, indent=2))
        for i in classes['images'][0]['classifiers'][0]['classes']:
            if i['class']=='person':
                print('person detected')
                for j in classes['images'][0]['classifiers'][0]['classes']:
                    if j['class']=='helmet':
                        vy=1
                        
                        
        if(vy==1):
                playsound('new_file3.mp3')
                print("played sound")
        else:
                with open('newfile4.mp3','wb') as audio_file:
                        audio_file.write(text_to_speech.synthesize('Your entry is restricted as you dint wear your helmet,please wear your helmet',voice='en-US_AllisonVoice',accept='audio/mp3'        ).get_result().content)
                my_database = client.create_database(database_name)
                multi_part_upload("cloud-object-storage-dsx-cos-standard-502",picname,pic+".jpg")
                if my_database.exists():
                    print("'{database_name}' successfully created.")
                    print(person)
                    json_document = {
                        "_id": pic,
                        "link":COS_ENDPOINT+"/cloud-object-storage-dsx-cos-standard-502/"+picname
                        }
                    new_document = my_database.create_document(json_document)
                    if new_document.exists():
                        print("Document '{new_document}' successfully created.")
                playsound('newfile4.mp3')
                print("played sound")

        time.sleep(1)
        person+=1
        t=34
        h=45
        vy=0
        data = {"d":{ 'temperature' : t, 'humidity': h, 'person': person}}
        #print data
        def myOnPublishCallback():
            print ("Published data to IBM Watson")
        success = deviceCli.publishEvent("Data", "json", data, qos=0, on_publish=myOnPublishCallback)
        if not success:
            print("Not connected to IoTF")
        time.sleep(1)
        deviceCli.commandCallback = myCommandCallback
        Key=cv2.waitKey(1)
        
cam.release()
        
cv2.destroyAllWindows()
             

deviceCli.disconnect()