# polly
Updates Slack channel topic with election date countdown and poll numbers

## polly.py
- is a python script that modifies the topic for the #politics channel on sanantoniodevs.slack.com
- it calculates a value showing the number of days until the November 3rd election.
- it scrapes the HTML on the RealClearPolitics.com site showing the poll numbers for Biden and Trump

It uses a crontab entry to run this script once daily.
When the script runs it calls an API on the slack channel to update the topic.
