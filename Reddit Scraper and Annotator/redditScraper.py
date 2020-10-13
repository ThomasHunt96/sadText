import praw
import re
import pandas as pd
import csv
import reddit_tools as tools

reddit = praw.Reddit(client_id='XVyMfJI3msk0-g',
                    client_secret='ZGGcc0zAimZgQ8oDZwiwx-zogCo',
                    username='AwkwardDragonfruit1',
                    password='548AJimpGKvRFrF',
                    user_agent='fypscraperv1')


subreddit = reddit.subreddit('depression')
hot_dep = subreddit.hot(limit=100)

reddit_data_list = []

for submission in hot_dep:
    if not submission.stickied:    
        
        #Split selftext into a list prior assigning to data_list 
        text_body = submission.selftext
        
        sentences = re.split('\.|\?|!|\n',text_body)
        sentences = tools.format_string_list(sentences)
        
        reddit_data = {'id':submission.id,'author':submission.name, 'date':submission.created_utc, 'score':submission.score, 'commentno':submission.num_comments, 'text':sentences} 
        reddit_data_list.append(reddit_data)


#csv writer with formatting
filename = input("Please input filename...")
with open (filename, 'w', newline='') as f:
    fieldnames = ['id','date','score','commentno','author','text']
    writer = csv.DictWriter(f, fieldnames = fieldnames)

    writer.writeheader()
    for reddit_data in reddit_data_list:
        
        reddit_id = tools.get_value_tostring(reddit_data, 'id')
        reddit_author = tools.get_value_tostring(reddit_data, 'author')
        reddit_sentence_list = tools.get_value_tolist(reddit_data, 'text')
        date = tools.get_value_tostring(reddit_data, 'date')
        score = tools.get_value_tostring(reddit_data, 'score')
        commentno = tools.get_value_tostring(reddit_data, 'commentno')

        
        
        for sentence in reddit_sentence_list:
            sentence = sentence.encode('ascii','ignore')
            sentence = sentence.decode('ascii')
            sentence = sentence.lower()
            sentence = re.sub("[^a-z'\s]+"," ",sentence)
            
            writer.writerow({'id':reddit_id,'date':date,
                            'score':score,'commentno':commentno,
                            'author':reddit_author,'text':sentence})
