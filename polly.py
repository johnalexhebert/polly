# modified code from
# https://gist.github.com/morion4000/3866374

from datetime import datetime, time

def dateDiffInDays(date1, date2):
  timedelta = date2 - date1
  return timedelta.days

election_date = datetime.strptime('2020-11-03', '%Y-%m-%d')
now = datetime.now()
countdown = dateDiffInDays(now, election_date) + 1
print("%d days until Nov. 3rd." % countdown)
