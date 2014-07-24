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

    tokens = {}

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
            for word in words:
                if not word in scores:
                    if word in tokens:
                        tokens[word]['sentiment'] += float(sentiment)
                        tokens[word]['count'] += 1
                    else:
                        tokens[word] = {'sentiment':float(sentiment), 'count':1}
    results = {}
    for item in tokens.items():
        count = item[1]['count']
        sentiment = item[1]['sentiment']
        word = item[0]
        results[word] = sentiment/float(count)
        # print(str(word) +" "+ str(sentiment/float(count)))

    maxs = max(list(results.values()))
    mins = min(list(results.values()))

    for result in results.items():
        if result[1] >= maxs-1 or result[1] <= mins+1:
            print (result)

if __name__ == '__main__':
    main()
