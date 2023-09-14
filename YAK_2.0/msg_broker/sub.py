import subprocess
import random
broker_id=random.sample(range(1, 100), 3)
broker_array=['broker1.py','broker2.py','broker3.py']

max_index=broker_id.index(max(broker_id))
broker_id.pop(max_index)
maxindex_broker=broker_array.pop(max_index)
subprocess.run(["python", maxindex_broker])
