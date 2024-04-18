from app import db, app
from app.models import User, Post


app_context = app.app_context()
app_context.push()
db.drop_all()
db.create_all()

u1 = User(username='john', email='john@example.com', role='user')
u2 = User(username='susan', email='susan@example.com', role='user')
u1.set_password("P@ssw0rd")
u2.set_password("P@ssw0rd")
db.session.add(u1)
db.session.add(u2)
u1.follow(u2)
u2.follow(u1)

au1 = User(username='admin', email='admin@example.com', role='admin' about_me='Phone:1234-5678\nemail:admin@example.com')
au1.set_password('admin')
db.session.add(au1)

p1 = Post(body='my first post!', author=u1)
p2 = Post(body='my first post!', author=u2)
db.session.add(p1)
db.session.add(p2)

db.session.commit()
