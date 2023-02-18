from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'São Paulo, BR'
  },
  {
    'id': 2,
    'title': 'Data Engineering',
    'location': 'São Paulo, BR',
    'Salary': '11.000 BRL'
  },
  {
    'id': 3,
    'title': 'Data Scientist',
    'location': 'São Paulo, BR',
    'Salary': '12.000 BRL'
  },
  {
    'id': 1,
    'title': 'Software Engineering',
    'location': 'São Paulo, BR',
    'Salary': '13.000 BRL'
  },
]


@app.route('/')
def hello_world():
  return render_template('home.html', jobs=JOBS, company_name='Cassiano')


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)

# @app.route("/api/json")
