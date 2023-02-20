from flask import Flask, render_template, jsonify
from database import load_jobs_from_db, load_job_from_db

app = Flask(__name__)


@app.route('/')
def hello_world():
  jobs = load_jobs_from_db()
  return render_template('home.html', jobs=jobs, company_name='Cassiano')


@app.route("/api/jobs")
def list_jobs():
  jobs = load_jobs_from_db()
  return jsonify(jobs)


# O <id> vai pegar o número que será colocado no navegador e trazer como variável,
# que jogará esse número dentro da função que está definida no database.py
@app.route("/job/<id>")
def show_job(id):
  job = load_job_from_db(id)
  return render_template('jobpage.html',job=job)
  # return render_template('jobpage.html', jobs=jobs)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
