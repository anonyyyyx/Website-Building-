from flask import Flask
namanwears = Flask(__name__)

@namanwears.route("/")
def main():
  return "MAIN PAGE"
