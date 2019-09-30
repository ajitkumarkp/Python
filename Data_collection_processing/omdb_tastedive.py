#1
# import requests_with_caching
import json

def get_movies_from_tastedive(name):
    param_d = {}
    param_d ["q"] = name  
    param_d ["limit"] = 5  
    param_d ["type"] = "movies"  
  #  resp = requests_with_caching.get("https://tastedive.com/api/similar", params=param_d)
    print(resp.url)
    return resp.json()
     
get_movies_from_tastedive("Black Panther")

#2

# import requests_with_caching
import json

def get_movies_from_tastedive(name):
    param_d = {}
    param_d ["q"] = name  
    param_d ["limit"] = 5  
    param_d ["type"] = "movies"  
    #resp = requests_with_caching.get("https://tastedive.com/api/similar", params=param_d)
    print(resp.url)
    return resp.json()

def extract_movie_titles(movies_dict):
    movie_titles=[]
    #print(json.dumps(movies_dict, indent=2))
    results= movies_dict["Similar"]["Results"] 
    for d in results:
        movie_titles.append(d['Name'])
    return movie_titles
extract_movie_titles(get_movies_from_tastedive("Tony Bennett"))


#3
#import requests_with_caching
import json

def get_movies_from_tastedive(name):
    param_d = {}
    param_d ["q"] = name  
    param_d ["limit"] = 5  
    param_d ["type"] = "movies"  
  #  resp = requests_with_caching.get("https://tastedive.com/api/similar", params=param_d)
    #print(resp.url)
    return resp.json()

def extract_movie_titles(movies_dict):
    movie_titles=[]
    #print(json.dumps(movies_dict, indent=2))
    results= movies_dict["Similar"]["Results"] 
    for d in results:
        movie_titles.append(d['Name'])
    return movie_titles

extract_movie_titles(get_movies_from_tastedive("Tony Bennett"))

def get_related_titles(list_movies):
    single_list = []
    for movie in list_movies:
        for title in extract_movie_titles(get_movies_from_tastedive(movie)):
            if title not in single_list:
               single_list.append(title) 
    return single_list                    
                                         
                               
print(get_related_titles(["Black Panther", "Captain Marvel"]))

#4
#import requests_with_caching
import json
def get_movie_data(movie):
    endpoint = "http://www.omdbapi.com/"
    param_d = {}
    param_d["t"] = movie
    param_d["r"] = "json"
 #   resp = requests_with_caching.get(endpoint,param_d)
    return(resp.json())
        
# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
movie_dict= get_movie_data("Black Panther")
print(json.dumps(movie_dict, indent=2))

# get_movie_data("Baby Mama")

#5
#import requests_with_caching
import json
def get_movie_data(movie):
    endpoint = "http://www.omdbapi.com/"
    param_d = {}
    param_d["t"] = movie
    param_d["r"] = "json"
 #   resp = requests_with_caching.get(endpoint,param_d)
    return(resp.json())

def get_movie_rating (movie_dict):
    ratings_list= movie_dict["Ratings"]
    rt_found=False
    print (ratings_list)
    for each_dict in ratings_list:
        if each_dict["Source"]=="Rotten Tomatoes":
            rt_found=True
            return(int(each_dict["Value"][:-1]))
    if rt_found==False:
        return 0
    
# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
print(get_movie_rating(get_movie_data("Deadpool 2")))


# Final
#import requests_with_caching
import json

def get_movies_from_tastedive(name):
    param_d = {}
    param_d ["q"] = name  
    param_d ["limit"] = 5  
    param_d ["type"] = "movies"  
    # resp = requests_with_caching.get("https://tastedive.com/api/similar", params=param_d)
    return resp.json()

def extract_movie_titles(movies_dict):
    movie_titles=[]
    results= movies_dict["Similar"]["Results"] 
    for d in results:
        movie_titles.append(d['Name'])
    return movie_titles

def get_related_titles(list_movies):
    single_list = []
    for movie in list_movies:
        for title in extract_movie_titles(get_movies_from_tastedive(movie)):
            if title not in single_list:
               single_list.append(title) 
    return single_list    

def get_movie_data(movie):
    endpoint = "http://www.omdbapi.com/"
    param_d = {}
    param_d["t"] = movie
    param_d["r"] = "json"
    # resp = requests_with_caching.get(endpoint,param_d)
    return(resp.json())

def get_movie_rating (movie_dict):
    ratings_list= movie_dict["Ratings"]
    rt_found=False
    for each_dict in ratings_list:
        if each_dict["Source"]=="Rotten Tomatoes":
            rt_found=True
            return(int(each_dict["Value"][:-1]))
    if rt_found==False:
        return 0

def get_sorted_recommendations(mov_list):
    all_titles_list = get_related_titles(mov_list)          
    sorted_values = sorted(all_titles_list,reverse=True,key=lambda title:(get_movie_rating(get_movie_data(title)),title)) 
    
    return sorted_values

get_sorted_recommendations(["Bridesmaids", "Sherlock Holmes"])


