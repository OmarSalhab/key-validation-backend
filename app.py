from flask import Flask, request

app = Flask(__name__)

# In-memory storage for used keys (use a database in production)
used_keys = set()

@app.route('/api/validate-key', methods=['GET', 'POST'])
def validate_key():
    key = request.args.get('key')
    if not key:
        return "invalid", 400

    if request.method == 'GET':  # Validate key
        if key in used_keys:
            return "invalid"
        return "valid"
    elif request.method == 'POST':  # Mark key as used
        used_keys.add(key)
        return "success"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
