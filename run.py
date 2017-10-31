#启动web服务器脚本
from app import app
import os

if __name__ == '__main__':
    #服务器用
    # port = int(os.environ.get('PORT', 5000))
    # app.run(host='0.0.0.0', port=port)
    #本地调试用
    app.run(debug = True)
