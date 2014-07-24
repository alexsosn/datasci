import sys
import json
import re

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    # lines(sent_file)
    # lines(tweet_file)

    scores = {} # initialize an empty dictionary
    for line in sent_file:
      term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
      scores[term] = int(score)  # Convert the score to an integer.

    # print(scores)

    for line in tweet_file:
        tw = json.loads(line)
        if 'text' in tw:
            sentiment = 0
            message = tw['text']
            del tw
            words = re.findall(r"[\w']+|[.,!?;]", message)
            for word in words:
                if word in scores:
                    sentiment += scores[word]
            print(sentiment)


if __name__ == '__main__':
    main()
