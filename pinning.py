import praw,configparser
from time import sleep

print("======================Reading Config file===================")
config = configparser.ConfigParser()
config.read('config.ini')

print("=============Loginging into reddit=========")
reddit = praw.Reddit(    
    username=config['Api_keys']['username'],
    password=config['Api_keys']['password'],
    client_id=config['Api_keys']['client_id'],
    client_secret =config['Api_keys']['secret'],
    user_agent = 'Talimeme pinning bot by u/Purple_scale_boi')

reddit.validate_on_submit = True

sub =  reddit.subreddit(config['msc']['subreddit'])

def main():
    print("=======================Loading sucessful=================================")
    for post in sub.stream.submissions():
        name = post.author.name
        print(name)
        try:
            comment = post.reply(f'Hey! u/{name} Mehhhh....')
            comment = reddit.comment(comment.id)
            comment.mod.distinguish(how="yes",sticky=True)
            
        except:
            print('hit rate limit trying again')
            sleep(5)
            print("=__________________________=")
            print("Trying Again")



main()