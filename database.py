from sqlalchemy import create_engine, text
import os

strg_connection = os.environ['DB_CONNECTION_STRING']

engine = create_engine(strg_connection,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for dict_row in result.mappings():
      jobs.append(dict(dict_row))
    return jobs


def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(
      text("select * from cassianojs.jobs where id = :val"), {"val": id})
    for dict_row in result.mappings():
      job=dict(dict_row)
      return job
    if len(job) == 0:
      return None
    else:
      return job

def add_application_to_db(job_id, data):
  with engine.connect() as conn:
    query='insert into cassianojs.applications (job_id, full_name, email, github, linkedin) values (:job_id, :full_name, :email, :github, :linkedin)'

    conn.execute(text(query),
                {"job_id":job_id,
                "full_name":data['name'],
                "email":data['email'],
                "github":data['github'],
                "linkedin":data['linkedin']})
