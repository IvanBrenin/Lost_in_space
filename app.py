from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)
d = {}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/count/results', methods=['POST'])
def count_results():
    answ = str(request.form.get('answers_list')) + '3:4'
    global d
    e = []
    d = {}
    while '[' in answ:
        answ = answ[answ.find('[') + 1:]
        e.append(answ[:answ.find(']')])
        if answ[answ.find(':') - 1] in '1234567890' and answ[answ.find(':') + 1] in '1234567890':
            answ = answ[answ.find(':') + 1:]

    while e:
        for nickname in e:
            d[nickname] = e.count(nickname)
            while nickname in e:
                e.remove(nickname)

    return redirect(url_for('result'))


@app.route('/result')
def result():
    return render_template('result.html', d=d)


if __name__ == '__main__':
    app.run(port=5001, debug=False)