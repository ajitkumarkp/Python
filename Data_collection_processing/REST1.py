# import statements for necessary Python modules
import os
os.environ['http_proxy'] = 'http://proxy-chain.intel.com:911'
os.environ['HTTP_PROXY'] = 'http://proxy-chain.intel.com:911'
os.environ['https_proxy'] = 'https://proxy-chain.intel.com:912'
os.environ['HTTPS_PROXY'] = 'https://proxy-chain.intel.com:912'
import requests
import json

def get_rhymes(word):
    baseurl = "https://api.datamuse.com/words"
    params_diction = {} # Set up an empty dictionary for query parameters
    params_diction["rel_rhy"] = word
    params_diction["max"] = "3" # get at most 3 results
    resp = requests.get(baseurl, params=params_diction)
    resp.text
    print (resp.url)
    # return the top three words

    # word_ds = resp.json() 
    # or below. Both convertes to a dcitionary obj.
    word_ds=json.loads(resp.text)

    return word_ds

    # return [d["word"] for d in word_ds]

print(get_rhymes("funny"))
