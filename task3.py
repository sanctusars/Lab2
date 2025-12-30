from flask import Flask, request
app = Flask(__name__)

@app.route("/currency")
def get_currency():
    has_today = 'today' in request.args
    key_value = request.args.get('key')
    
    if has_today and key_value == 'eur':
        return "EUR - 49,6"
    else:
        return "Error. Correct format: /currency?today&key=eur", 400

if __name__ == '__main__':
    app.run(port=8000)