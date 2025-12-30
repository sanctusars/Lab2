from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/currency")
def get_currency_by_header():
    data = {"currency": "EUR", "rate": "49,6"}
    
    content_type = request.headers.get('Content-Type')

    if content_type == 'application/json':
        return jsonify(data)
    
    elif content_type == 'application/xml':
        xml_data = f"""<?xml version="1.0" encoding="UTF-8"?>
<root>
    <currency>{data['currency']}</currency>
    <rate>{data['rate']}</rate>
</root>"""
        return xml_data, 200, {'Content-Type': 'application/xml'}
    return f"Currency: {data['currency']}, Rate: {data['rate']}"

if __name__ == '__main__':
    app.run(port=8000)