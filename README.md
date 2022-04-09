
# Twitter Bot.

This project was written to support automated twitter posts.

In the api.py module there are methods written using the tweepy library:
- tweepy.Client
- Client.search_all_tweets
- Client.get_tweet
- Client.create_tweet

## Roadmap

- Put the project into your virtual environment

- Fill the fields with your keys in the settings.ini file (Required for authentication on Twitter)
  https://developer.twitter.com/en/docs/authentication/overview

- Install the necessary libraries (requirements.txt)
  

## How to Use
- Main method -> api.tweet_to_publish(text, query)
- This method that makes the post expects two parameters. 
- Text -> Content of your post
- Query -> e.g 'search tweet with this phrase  -is:retweet'

This query is interesting when you want to check if there are already posts with the subject of the new post, 
because from there you can create sequential posts, passing the old post ID at the time of creating the post.

```bash
  python .\main.py 
```

