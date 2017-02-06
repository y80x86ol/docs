from flask import Flask
from config import web

# 初始化flask
app = Flask(__name__)

# 基础配置
app.debug = web.config['debug']
