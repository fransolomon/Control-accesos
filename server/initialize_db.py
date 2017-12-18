from config import DB
from server.models import User, Entry

DB.connect()
DB.create_tables([User, Entry])
