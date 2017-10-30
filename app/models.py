from werkzeug.security import generate_password_hash, check_password_hash
#User模型继承UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import db
#from . import login_manager
from markdown import markdown
from flaskext.markdown import Markdown
from datetime import datetime

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)

    def __init__(self, name):
        self.name = name

    # users = db.relationship('User',backref='role',lazy='dynamic')
#__repr__ 方法告诉 Python 如何打印这个类的对象,用它来调试。
    def __repr__(self):
        return '<Role %r>' % self.name

class User(db.Model,UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))

    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    role = db.relationship('Role', backref=db.backref('user_set', lazy='dynamic'))
    cards = db.relationship('Card', backref = 'author', lazy = dynamic)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def confirm_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __init__(self, username, password, role):
        self.username = username
        self.password = password

    def is_authenticated(self):
        return True

    def is_active():
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def __repr__(self):
        return '%s' % self.username
'''
class Post(db.Model):
    __tablename__ = 'Post'
    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post %r>' % (self.body)

    def confirm_password(self,password):
        return check_password_hash(self.hash_password,password)
  '''


#创建卡片数据库对象模型
class Card(db.Model):
    __tablename__ = 'cards'
    id = db.Column(db.Integer , primary_key = True)
    title = db.Column(db.String(60))
    body = db.Column(db.String(350))
    timestamp = db.Column(db.DateTime, index=True)
    #创建时得到Markdown的HTML代码缓存到数据库这个列中。
    body_html = db.Column(db.Text)
    author_id = db. Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, title, body):
        self.title = title
        self.body = body
        self.timestamp = datetime.utcnow()
        #创建时得到Markdown的HTML代码缓存到数据库这个列中。
        self.body_html = markdown(self.body, output_format='html')
        # self.body_html = body
#这个好难,没有看懂，参考flask开发书P126
#     @staticmethod
#     def on_changed_body(target, value, oldvalue, initiator):
#         allowed_tags = ['a', 'abbr', 'acronym', 'b', 'blockquote', 'code',
#                         'em', 'i', 'li', 'ol', 'pre', 'strong', 'ul',
#                         'h1', 'h2', 'h3', 'p']
#         target.body_html = bleach.linkify(bleach.clean(
#             markdown(value, output_format='html'),
#             tags=allowed_tags, strip=True))
#
# db.event.listen(Card.body, 'set', Card.on_changed_body)
