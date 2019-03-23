from flask import Flask
import os

app = Flask(__name__)

port = int(os.getenv("PORT", 8080))

@app.route('/')
def python_task():
  page = "<head><style type='text/css'> body {font-size: 56px;font-weight: bold; background-color: #95ff93; text-align: center;}</style></head>\n<body>CONGRATULATIONS<br>you just completed basic task #1</body>"
  return page

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
