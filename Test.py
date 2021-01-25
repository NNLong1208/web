from flask import Flask,render_template,jsonify
import random
import base64
from datetime import datetime
app = Flask(__name__)

data = []

name_ = ['Bằng', 'Chi', 'Đức', 'Đức Anh', 'Duy', 'Hiền', 'Dương Phương', 'Đinh Phương', 'Minh Anh', 'unknown', 'hiếu']
check_ = ['Fake','Real']
def create():
    data.clear()
    name = random.choice(name_)
    check = random.choice(check_) #Real/Face
    now = datetime.now().strftime("%H:%M:%S")
    with open(r"static\img\building.jpg", "rb") as image_file:
        img = base64.b64encode(image_file.read()).decode("utf-8")
    data.append(name)
    data.append(now)
    data.append(img)
    data.append(check)


@app.route('/update_table', methods=['POST', 'GET'])
def updatetable():
    create()
    if len(data) > 0:
        return jsonify(data = data)

@app.route('/')
def main():
    return render_template('test.html', data = data, date = datetime.now().strftime("%d/%m/%Y"))

if __name__ == "__main__":
    app.run(debug=True)