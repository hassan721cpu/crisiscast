import requests

def lambda_handler(event, context):
    token = 'YOUR_BOT_TOKEN'
    chat_id = 'YOUR_CHAT_ID'

    url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/significant_hour.geojson"
    data = requests.get(url).json()

    if not data['features']:
        message = "✅ No significant earthquakes in the last hour."
    else:
        quake = data['features'][0]
        place = quake['properties']['place']
        mag = quake['properties']['mag']
        message = f"🚨 Earthquake Alert: {mag} magnitude near {place}."

    telegram_url = f"https://api.telegram.org/bot{token}/sendMessage"
    requests.post(telegram_url, data={'chat_id': chat_id, 'text': message})

    return {'statusCode': 200, 'body': message}
