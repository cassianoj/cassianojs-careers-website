from flask import Flask, render_template, jsonify, request
from database import load_jobs_from_db, load_job_from_db, add_application_to_db
import requests
import os
import xml.etree.ElementTree as ET

app = Flask(__name__)
content = os.environ['LOMADEE_CONTENT']
LOMADEESOURCEIDSITE = os.environ['LOMADEESOURCEIDSITE']


@app.route('/')
def hello_world():
  jobs = load_jobs_from_db()
  return render_template('home.html',
                         jobs=jobs,
                         company_name='Cassiano',
                         content=content)


@app.route("/api/jobs")
def list_jobs():
  jobs = load_jobs_from_db()
  return jsonify(jobs, company_name='Cassiano')


# O <id> vai pegar o número que será colocado no navegador e trazer como variável,
# que jogará esse número dentro da função que está definida no database.py
@app.route("/job/<id>")
def show_job(id):
  job = load_job_from_db(id)
  return render_template('jobpage.html', job=job, company_name='Cassiano')


@app.route("/job/<id>/apply", methods=['post'])
def apply_to_job(id):
  data = request.form
  job = load_job_from_db(id)
  add_application_to_db(id, data=data)
  return render_template('apply.html', data=data, job=job)


@app.route('/catfacts')
def catfacts():
  req = requests.get(
    'https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount=1')
  data = req.json()
  return jsonify(data)


@app.route('/lomadee/nike')
def get_xml_data():
  # Make the API request and get the response
  response = requests.get('https://api.lomadee.com/xml/5901.xml')

  root = ET.fromstring(response.content)

  # Extract the data from the XML file
  data = []
  for child in root.findall('offer'):
    item = {}
    item['name'] = child.find('name').text
    item['price'] = child.find('price').text
    item['link'] = child.find('link').text
    item['imgsrc'] = child.find('thumbnail').text
    data.append(item)

  for my_dict in data:
    my_dict["link"] = my_dict["link"].replace("LOMADEESOURCEID",
                                              LOMADEESOURCEIDSITE)
  # Return the data as a JSON object
  return render_template("lomadeenike.html",
                         offers=data,
                         company_name='Cassiano')


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
