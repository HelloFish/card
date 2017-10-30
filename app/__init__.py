from flask import Flask
from flask_bootstrap import Bootstrap  
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager 
from flask_moment import Moment
#from config import config
from flask_pagedown import PageDown
from flask_pagedown.fields import PageDownField
# 为markdown的显示支持
import markdown
from flaskext.markdown import Markdown
from datetime import datetime


app = Flask(__name__) 

app.config.from_object('config') #使Flask读取使用Flaks-WTF
bootstrap = Bootstrap(app) #实例化
  
#flask_login的初始化
loginmanager=LoginManager()
loginmanager.init_app(app)
loginmanager.session_protection='strong' 
loginmanager.login_view='login' 

db = SQLAlchemy(app) #初始数据库
pagedown = PageDown(app)
Markdown(app)
moment = Moment(app)
from app import views, models