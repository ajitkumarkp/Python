## Twitter Sentiment classifier

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

def get_pos (sentence):
    num_pos=0
    words_list = sentence.split()
    for word in words_list:
        if strip_punctuation(word).lower() in positive_words:
            # print ("POS-"+strip_punctuation(word).lower())
            num_pos+=1
    return num_pos

negative_words = []
with open("C:\\Users\\akottopa\\Desktop\\InsideIn\\IoTG\\Training\\coursera\\Python3-specialization\\Funcs_Dict_files\\sentiment\\negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def get_neg (sentence):
    num_neg=0
    words_list = sentence.split()
    for word in words_list:
        if strip_punctuation(word).lower() in negative_words:
            # print ("        NEG-"+strip_punctuation(word).lower())
            num_neg=num_neg+1
    return num_neg


with open("C:\\Users\\akottopa\\Desktop\\InsideIn\\IoTG\\Training\\coursera\\Python3-specialization\\Funcs_Dict_files\\sentiment\\project_twitter_data.csv", "r") as infile_h:
    with open("C:\\Users\\akottopa\\Desktop\\InsideIn\\IoTG\\Training\\coursera\\Python3-specialization\\Funcs_Dict_files\\sentiment\\resulting_data.csv", "w") as outfile_h:
        line1= True
        for line in infile_h.readlines():
            if line1: 
                outfile_h.write("{}, {}, {}, {}, {}\n".format("Number of Retweets", "Number of Replies", "Positive Score", "Negative Score", "Net Score"))
                line1 = False
                continue

            tweet_text, retweet_count, reply_count= line.strip().split(",")
            pos_score = get_pos(tweet_text)
            neg_score = get_neg(tweet_text)
            net_score = pos_score-neg_score
            outfile_h.write("{},{},{},{},{}\n".format(retweet_count, reply_count, pos_score, neg_score, net_score))




