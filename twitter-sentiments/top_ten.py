__author__ = 'alex'

import sys
import json
import re

def main():
    tweet_file = open(sys.argv[1])

    res = {}

    for line in tweet_file:
        tw = json.loads(line)
        if 'entities' in tw:
            hashtags = tw['entities']['hashtags']
            del tw
            for tag in hashtags:
                if tag['text'] in res:
                    res[tag['text']] += 1
                else:
                    res[tag['text']] = 1

    top = sorted(res.values(), reverse=True)[0:10]

    exclude = set()

    for ii in top:
        for item in res.items():
            if item[1] == ii and item[0] not in exclude:
                print(str(item[0]) + ' ' + str(item[1]))
                exclude.add(item[0])
                break



if __name__ == '__main__':
    main()
