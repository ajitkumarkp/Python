punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
def strip_punctuation (word):
    for char in punctuation_chars:
       word = word.replace(char, "")
    return word

positive_words = []
with open("C:\\Users\\akottopa\\Desktop\\InsideIn\\IoTG\\Training\\coursera\\Python3-specialization\\Funcs_Dict_files\\sentiment\\positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

def get_pos (sentence1):
    num_pos=0
    words_list1 = sentence1.split()
    for word1 in words_list1:
        if strip_punctuation(word1).lower() in positive_words:
            num_pos+=1
    return num_pos

negative_words = []
with open("C:\\Users\\akottopa\\Desktop\\InsideIn\\IoTG\\Training\\coursera\\Python3-specialization\\Funcs_Dict_files\\sentiment\\negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def get_neg (sentence2):
    num_neg=0
    words_list2 = sentence2.split()
    for word2 in words_list2:
        if strip_punctuation(word2).lower() in negative_words:
            num_neg=num_neg+1
    return num_neg

twitter_data={}

with open("C:\\Users\\akottopa\\Desktop\\InsideIn\\IoTG\\Training\\coursera\\Python3-specialization\\Funcs_Dict_files\\sentiment\\project_twitter_data.csv") as infile_h:
    data= infile_h.read()
    lines_list = data.split("\n")
    for line in lines_list:
        columns= line.split(",")
        twitter_data[columns[0]]=[columns[1], columns[2]]

for tweet in twitter_data:
    if tweet=="tweet_text":
        twitter_data[tweet].append("num_pos")
        twitter_data[tweet].append("num_neg")
        twitter_data[tweet].append("net")
    else:
        twitter_data[tweet].append(get_pos(tweet))
        twitter_data[tweet].append(get_neg(tweet))
        twitter_data[tweet].append(get_pos(tweet)-get_neg(tweet))

with open("C:\\Users\\akottopa\\Desktop\\InsideIn\\IoTG\\Training\\coursera\\Python3-specialization\\Funcs_Dict_files\\sentiment\\resulting_data.csv", "w") as outfile_h:
    for tweet in twitter_data:
        outfile_h.write(str(twitter_data[tweet][0]) + "," + str(twitter_data[tweet][1]) + "," + str(twitter_data[tweet][2]) + "," + str(twitter_data[tweet][3]) + "," + str(twitter_data[tweet][4]) + "\n")

        






