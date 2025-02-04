from flask import Flask, request
from supabase import create_client, Client

app = Flask(__name__)

# Supabase credentials
SUPABASE_URL = 'https://xxjnojhjmjucyomdywzd.supabase.co'
SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inh4am5vamhqbWp1Y3lvbWR5d3pkIiwicm9sZSI6ImFub24iLCJpYXQiOjE3Mzg2ODc1OTgsImV4cCI6MjA1NDI2MzU5OH0.Zh6XefGxfDvahZ5OPSL7hnZRrH3OgxSklYgK1n3nQSc'
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.route('/api/validate-key', methods=['GET', 'POST'])
def validate_key():
    key = request.args.get('key')
    if not key:
        return "invalid", 400

    if request.method == 'GET':  # Validate key
        response = supabase.table('used_keys').select('key').eq('key', key).execute()
        if response.data:
            return "invalid"
        return "valid"
    elif request.method == 'POST':  # Mark key as used
        supabase.table('used_keys').insert({'key': key}).execute()
        return "success"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)