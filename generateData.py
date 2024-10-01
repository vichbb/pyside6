import sqlite3
import pandas as pd
from faker import Faker

fake = Faker(locale='zh_CN')


data = pd.DataFrame([{'name': fake.name(), 'address': fake.address(), 'email': fake.ascii_free_email()} for _ in range(80)])

connect = sqlite3.connect("test.db")

data.to_sql("user", connect, if_exists="replace", index=False)