from server.models import db, User, Entry

db.connect()
db.create_tables([User, Entry])
