#!/usr/bin/python
# -*- coding: utf-8 -*-

import base64
import json
import os
import re

import boto3
import requests_oauthlib

class TwitterConf():
    uri = 'https://stream.twitter.com/1.1/statuses/filter.json'

    consumer_key = os.environ['CONSUMER_KEY']
    consumer_secret = os.environ['CONSUMER_SECRET']
    access_token = os.environ['ACCESS_TOKEN']
    access_token_secret = os.environ['ACCESS_TOKEN_SECRET']


class KinesisConf():
    client = boto3.client('kinesis', endpoint_url='http://localhost:4567')


def main():
    emoji_pattern = re.compile(u"(\ud83d[\ude00-\ude4f])+", flags=re.UNICODE)

    session = requests_oauthlib.OAuth1Session(
        TwitterConf.consumer_key,
        TwitterConf.consumer_secret,
        TwitterConf.access_token,
        TwitterConf.access_token_secret)

    stream = session.post(TwitterConf.uri, data=dict(track='happy'), stream=True)
    for line in stream.iter_lines():
        status = json.loads(line.decode('utf-8'))
        text = status['text']
        emojis = emoji_pattern.findall(text)
        for e in emojis:
            payload = json.dumps(dict(emoji = e, text = text))
            print(e)

            put_response = KinesisConf.client.put_record(
                StreamName='test-stream',
                Data=base64.b64encode(payload),
                PartitionKey=status['created_at'])

            if put_response['ResponseMetadata']['HTTPStatusCode'] is not 200:
                raise Exception(response)


if __name__ == '__main__':
    main()
