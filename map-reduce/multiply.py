import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    matrix = record[0]
    i=record[1]
    j=record[2]
    mvalue=record[3]

    for k in range(5):

        if matrix=='a':
           mr.emit_intermediate((i,k),(matrix, i,j,mvalue))
        else:
           mr.emit_intermediate((k,j),(matrix, j,i,mvalue))


def reducer(key, list_of_values):
    i = key[0]
    j = key[1]
    print (list_of_values)
    print (key)


    value = 0
    a = [0,0,0,0,0]
    b = [0,0,0,0,0]

    for ent in list_of_values:
        m = ent[0]
        if m == 'a':
            a[ent[2]] = ent[3]
        else:
            b[ent[2]] = ent[3]

    for ind in xrange(len(a)):
        value += a[ind] * b[ind]
    mr.emit((i,j,value))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
