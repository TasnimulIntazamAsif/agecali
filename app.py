from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

def get_zodiac_sign(month, day):
    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Aries"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Taurus"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Gemini"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Cancer"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Leo"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Virgo"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Libra"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Scorpio"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Sagittarius"
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "Capricorn"
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Aquarius"
    else:
        return "Pisces"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate_age():
    birth_date = request.json['birthDate']
    birth_date = datetime.strptime(birth_date, '%Y-%m-%d')
    current_date = datetime.now()
    
    age = current_date.year - birth_date.year
    if current_date.month < birth_date.month or \
        (current_date.month == birth_date.month and current_date.day < birth_date.day):
        age -= 1
    
    days = (current_date - birth_date).days
    months = age * 12 + current_date.month - birth_date.month
    minutes = days * 24 * 60
    
    zodiac = get_zodiac_sign(birth_date.month, birth_date.day)
    
    return jsonify({
        'years': age,
        'months': months,
        'days': days,
        'minutes': minutes,
        'zodiac': zodiac
    })

if __name__ == '__main__':
    app.run(debug=True) 