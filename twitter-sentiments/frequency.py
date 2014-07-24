import sys
import json
import re

def lines(fp):
    print str(len(fp.readlines()))

def main():
    tweet_file = open(sys.argv[1])

    tokens = {}

    for line in tweet_file:
        tw = json.loads(line)
        if 'text' in tw:
            sentiment = 0
            message = tw['text']
            del tw
            words = re.findall(r"[\w']+|[.,!?;]", message)

            for word in words:
                if word in tokens:
                    tokens[word]['count'] += 1
                else:
                    tokens[word] = {'count':1}
    results = {}
    all_occur = 0

    for item in tokens.items():
        count = item[1]['count']
        all_occur += count

    for item in tokens.items():
        count = item[1]['count']
        word = item[0]
        results[word] = count/float(all_occur)
        print(str(word) +" "+ str(count/float(all_occur)))


if __name__ == '__main__':
    main()
