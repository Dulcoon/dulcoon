import statistics
import math

node = [47, 21, 76]
c = []
def avg():
    b = statistics.mean(node)
    return b

def totalSellisihKuadrat():
    for i in node:
        c.append((i - avg())**2)
    jmlh = sum(c)
    return jmlh

def devasi():
    # a = math.sqrt
    akar =  math.sqrt(totalSellisihKuadrat()/len(node))
    return akar

print(devasi())

            
    

