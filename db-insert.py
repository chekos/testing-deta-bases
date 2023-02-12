from deta import Deta
from dotenv import dotenv_values

import os
import time
from datetime import datetime as dt

config = {**dotenv_values(), **os.environ}
deta = Deta(config["PROJECT_KEY"])
db = deta.Base("demo_db")

db.put(int(time.time()), expire_in=120)

my_bd = dt(2000,10,9)
another_bd = dt(2005,2,19)
db.put({"key": str(int(my_bd.timestamp())), "info": "2rs"}, expire_in=120)
db.put({"key": str(int(another_bd.timestamp())), "info": "secoond"}, expire_in=120)
