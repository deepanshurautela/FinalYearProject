import json 
import requests 
api_key = 'AIzaSyB8HUlDV-j-Cl0MXSwN5a4g9nW-qIzx0BA'
url = ('https://commentanalyzer.googleapis.com/v1alpha1/comments:analyze' +    
       '?key=' + api_key)

def get_sent_val(text):
	data_dict = {'comment': {'text': str(text)},'languages': ['en'],'requestedAttributes': {'TOXICITY': {}, "UNSUBSTANTIAL": {}, "INSULT" : {}, "PROFANITY" : {}}}
	response = requests.post(url=url, data=json.dumps(data_dict))
	#response_dict = json.loads(response.content)
	return response.content