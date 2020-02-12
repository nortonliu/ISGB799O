
import tweepy as tw
import json

atoken = "1190313339857129472-vF3xCNFF5iUbZ121CrbUpfbvSVKsPT"
asecret = "sASLT28UrnJLp0RwzsSK4skN65WJ82cOWjsvcaiIG07sH"
ckey = "zZzCv8jSBYqdv4cdwGs4DsbuN"
csecret = "4m0icZKFl0aSUG7dNrOkaNo2I3vYqLsmjrYaNdTyVOsveCpPzI"

auth = tw.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

api = tw.API(auth)

n = 1

word_list = ['impossible whopper','beyond burger','impossible burger']

full_data = tw.Cursor(api.search, tweet_mode='extended', q = 'impossible burger' ,lang = 'en').items()

for all_data in full_data:
    #print('Tweet by: @' + tweet.user.screen_name + ':::' + str(tweet.text.encode('UTF-8')))
    try:
        tweet1 = all_data.full_text
        tweet = tweet1.encode('UTF-8')
        location = all_data.user.location
        username = all_data.user.screen_name
        id_str = all_data.user.id_str
        followers_count = all_data.user.followers_count
        friends_count = all_data.user.friends_count
        favourites_count = all_data.user.favourites_count
        time_zone = all_data.user.time_zone

        out = open('full_records_impossible_burger.txt', 'a')
        out.write(str(username)+'::'+str(location)+'::'+str(id_str)+'::'+str(followers_count)+'::'+str(friends_count)+'::'+str(favourites_count)+'::'+str(time_zone)+'::'+str(tweet))
        out.write('\n')
        out.close()
        print (str(n) + "@" + username, " :: ", tweet)
        n += 1
    except:
        print ('failed ondata')
