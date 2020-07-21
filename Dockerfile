FROM python:3
# add crontab command
ADD polly.py /
RUN pip install beautifulsoup4
CMD [ "python3", "polly.py" ]
