# Marvin
This project is named after the android from The Hitchhikers Guide to Galaxy. https://en.wikipedia.org/wiki/Marvin_(character).

## Purpose
To track the mood of a Slack channel either in real time or historically. Using a sentiment analysis algorithm from https://algorithmia.com
each comment is rated for it's general tone or sentiment.

# Setup
```
virtualenv .
source bin/activate
pip install -r requirements.txt
cp python-rtmbot-master/rtmbot.conf.example python-rtmbot-master/rtmbot.conf
```

Update python-rtmbot-master/rtmbot.conf with your API keys from Slack and Algorithmia.

```
DEBUG: True
TALK: True

SLACK_TOKEN: "YOUR_SLACK_TOKEN"
ALGORITHMIA_KEY: "YOUR_ALGORITHMIA_KEY"
```

# Usage
Marvin uses the algorithm https://algorithmia.com/algorithms/nlp/SocialSentimentAnalysis to analyse a message in the Slack channel.
The results from the analysis are in the form of:

* Negative
* Neutral
* Postitive

For more detail check out the algorithm's page https://algorithmia.com/algorithms/nlp/SocialSentimentAnalysis.

## Historical Analysis
Provided in the ```historical``` directory is a script that will review the last 24 hours of your Slack channel.

To run the historical analysis first you need your channel id. Running the following to get a list from your checkout directory.

```
$ python historical/channel_review.py -l

Channel Name    Slack ID
--------------  ----------
home            C0MUSFS49
random          C0ASDF34R
general         C056STSWB
```

Copy the id for the required channel and do the following:

```
$ python historical/channel_review.py -c C056STSWB
  %positive    %neutral    %negative
-----------  ----------  -----------
         30          48           22
```

## Realtime Slack Channel Monitoring

Inside the ```python-rtmbot-master``` directory is all the code need to run a Slack bot. To start the bot:

```
$ cd python-rtmbot-master
$ python rtmbot.py
```

Check your Slack channel and your bot will appear online.

### Bot Commands
Currently there is only a single command:

```current mood?```

This will display the current averages:

```
marvin BOT [7:45 PM]
Positive: 20.0% (2)
Neutral: 60.0% (6)
Negative: 20.0% (2)
```
