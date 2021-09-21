from datetime import datetime
import time
c_time = time.time()

i = 0
durration = 3
while (a:= time.time() - c_time ) < durration :
    i+=1
    print(a)
print('скорость за %i секунд -> %s' % (durration,i))

