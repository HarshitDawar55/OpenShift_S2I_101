from flask import Flask

app = Flask("OpenShift S2I 101")

@app.route("/", methods = ["GET"])
def main():
  return "This is OpenShift Source 2 Image demo by Mr. Harshit Dawar!"

app.run(host="0.0.0.0", port=8080)
