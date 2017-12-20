from config import DB
from data.models import User, Entry

DB.connect()
DB.create_tables([User, Entry])
