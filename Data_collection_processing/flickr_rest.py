import os
os.environ['http_proxy'] = 'http://proxy-chain.intel.com:911'
os.environ['HTTP_PROXY'] = 'http://proxy-chain.intel.com:911'
os.environ['https_proxy'] = 'https://proxy-chain.intel.com:912'
os.environ['HTTPS_PROXY'] = 'https://proxy-chain.intel.com:912'
import requests
import json
import webbrowser

# apply for a flickr authentication key at http://www.flickr.com/services/apps/create/apply/?
# paste the key (not the secret) as the value of the variable flickr_key
flickr_key = 'aa90da925d148a617c556e092229e3e5'

def get_flickr_data(tags_string):
    baseurl = "https://api.flickr.com/services/rest/"
    params_diction = {}
    params_diction["api_key"] = flickr_key # from the above global variable
    params_diction["tags"] = tags_string # must be a comma separated string to work correctly
    params_diction["tag_mode"] = "all"
    params_diction["method"] = "flickr.photos.search"
    params_diction["per_page"] = 5
    params_diction["media"] = "photos"
    params_diction["format"] = "json"
    params_diction["nojsoncallback"] = 1
    flickr_resp = requests.get(baseurl, params = params_diction)
    # Useful for debugging: print the url! Uncomment the below line to do so.
    print(flickr_resp.url) # Paste the result into the browser to check it out...

    return flickr_resp.json()


dict_flicker_resp = get_flickr_data ("Train")

print(json.dumps(dict_flicker_resp, indent=2))

list_photos= dict_flicker_resp["photos"]["photo"]

for d in list_photos:
    owner = d["owner"]
    photo_id = d["id"]
    print (owner, photo_id)
    webbrowser.open("https://www.flickr.com/photos/{}/{}".format(owner, photo_id))





