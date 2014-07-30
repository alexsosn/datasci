__author__ = 'alex'
import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents

    mr.emit_intermediate(str(sorted(record)), record)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    total = 0
    if len(list_of_values) == 1:
        mr.emit(tuple(list_of_values[0]))
        mr.emit(tuple(list_of_values[0][::-1]))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
