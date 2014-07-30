import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(document_id):
    # key: document identifier
    # value: document contents
    key =  document_id[1]
    value = [document_id[0], document_id]
    # words = value.split()
    # for w in words:
    mr.emit_intermediate(key, value)

def reducer(key, list_of_values):
    jaz = []
    for item in list_of_values:
        if item[0] == 'order':
            jaz = item[1]
        else:
            mr.emit(jaz+item[1])

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
