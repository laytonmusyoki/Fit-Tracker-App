from flask import Flask, render_template, redirect, request, flash

app = Flask(__name__)
app.secret_key = "layton"

@app.route('/home', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        weight = request.form['weight']
        height = request.form['height']
        age = request.form['age']
        gender = request.form['gender']
        
        if weight == '' or height == '' or age == '' or gender == '':
            flash('All fields are required...')
            return render_template('home.html', weight=weight, height=height, age=age, gender=gender)
        
        else:
            weight = float(weight)
            height = float(height)
            age = float(age)

            if gender == "male":
                calories = 10 * weight + 6.25 * height - 5 * age + 5
                return render_template('home.html', content="Your calories is " + str(calories))
            else:
                calories = 10 * weight + 6.25 * height - 5 * age - 161
                return render_template('home.html', content="Your calories is " + str(calories))

    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)

