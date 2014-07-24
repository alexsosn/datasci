__author__ = 'alex'

states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}

states_dict = dict(zip(states.values(), states.keys()))

import sys
import json
import re

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    scores = {} # initialize an empty dictionary
    for line in sent_file:
      term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
      scores[term] = int(score)  # Convert the score to an integer.

    # print(scores)

    res = {}

    for line in tweet_file:
        tw = json.loads(line)
        if 'text' in tw:
            sentiment = 0
            message = tw['text']
            # del tw
            words = re.findall(r"[\w']+|[.,!?;]", message)
            for word in words:
                if word in scores:
                    sentiment += scores[word]
            # print(sentiment)


            if tw['place']:
                if tw['place']['country_code'] == 'US':
                    state_name = tw['place']['name']
                    if state_name in states_dict :
                        if state_name in res :
                            res[state_name]['sum'] += sentiment
                            res[state_name]['num'] += 1
                        else :
                            res[state_name] = {'sum':sentiment, 'num':1.}
                    # print(tw['place']['name'])

    res2 = {}

    for item in res.items():
        res2[str(item[1]['sum']/item[1]['num'])] = str(states_dict[item[0]])

    print(res2[max(res2.keys())])

if __name__ == '__main__':
    main()
