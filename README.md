# CrisisCast 🚨

CrisisCast is a real-time disaster alert bot that uses **AWS Lambda**, **EventBridge**, and the **USGS earthquake API** to automatically send alerts to Telegram.

## 🔧 Built With:
- AWS Lambda (Python 3.11)
- AWS EventBridge
- Telegram Bot API
- USGS Earthquake GeoJSON Feed

## 🌍 How it Works
- Lambda pulls significant earthquake data every hour from USGS.
- If an earthquake is found, it sends a Telegram alert with magnitude and location.
- EventBridge schedules this check every hour — fully serverless!

## 🧪 How to Test:
1. Clone the repo
2. Create a Telegram bot via @BotFather
3. Set your Bot Token and Chat ID in the code
4. Deploy to AWS Lambda
5. Schedule with EventBridge to run every hour

## 📽️ Demo Video
[Add your YouTube link here]

## 💡 Why it Matters
- Helps people get disaster alerts instantly
- Fully automated, zero cost using AWS Free Tier
- Can be expanded to floods, storms, or wildfire alerts
