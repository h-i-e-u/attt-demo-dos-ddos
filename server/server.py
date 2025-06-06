"""
Description: A simple server for DDoS demonstration
Author: github.com/h-i-e-u
Version: 1.0
"""

from flask import Flask, render_template_string, request
import time

app = Flask(__name__)

# Simple HTML template for rendering the status page
template = """
<!doctype html>
<html>
<head>
  <title>DDOS Demo Server</title>
  <style>
    body { font-family: Arial; text-align: center; padding: 50px; background-color: #f2f2f2; }
    .status { font-size: 24px; margin-top: 30px; }
    .info { margin-top: 20px; font-size: 16px; color: #666; }
  </style>
</head>
<body>
  <h1>🚀 Server is on</h1>
  <div class="status">
    Đã xử lý {{ count }} request tại routes<code> / </code>
  </div>
  <div class="info">
    IP: {{ ip }} <br>
    Thời gian xử lý: {{ elapsed }} giây
  </div>
</body>
</html>
"""

counter = 0



@app.route("/")
def slow():
    global counter
    start = time.time()
    time.sleep(1)  # Simulate a slow response
    counter += 1
    elapsed = round(time.time() - start, 2)
    ip = request.remote_addr
    return render_template_string(template, count=counter, elapsed=elapsed, ip=ip)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
