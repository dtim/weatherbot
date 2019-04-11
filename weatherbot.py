from flask import Flask, request, jsonify
from forecast import ForecastService


app = Flask(__name__)
fs = ForecastService(user_agent="dtim.weatherbot")

BEAUFORT_SCALE = {
    0: 'calm',
    1: 'light air',
    2: 'light breeze',
    3: 'gentle breeze',
    4: 'moderate breeze',
    5: 'fresh breeze',
    6: 'strong breeze',
    7: 'high wind',
    8: 'fresh gale',
    9: 'severe gale',
    10: 'storm',
    11: 'violent storm',
    12: 'hurricane'
}


@app.route('/action', methods=['POST'])
def action():
    content = request.json
    if content:
        query_result = content.get('queryResult')
        if query_result:
            intent = query_result.get('intent')
            parameters = query_result.get('parameters')
            reply = produce_reply(intent, parameters)
            if reply:
                return jsonify(reply)
    return jsonify({'error': 'Invalid payload'}), 400


def produce_reply(intent_dict, parameters_dict):
    answer = "I don't know."

    intent = intent_dict.get('displayName') if intent_dict else None
    if intent == 'weather':
        if parameters_dict:
            city = parameters_dict.get('geo-city')
            prop = parameters_dict.get('weather-property')
            if city:
                weather = fs.weather(city)
                temp_data = weather['location']['temperature']
                wind_data = weather['location']['windSpeed']
                temp_message = '{}°'.format(temp_data['@value'])
                wind_message = BEAUFORT_SCALE.get(int(wind_data['@beaufort']))
                if prop:
                    if prop == 'temperature':
                        answer = temp_message
                    elif prop == 'wind':
                        answer = wind_message
                else:
                    answer = '{}, {}'.format(temp_message, wind_message)
    return {'fulfillmentText': answer}
