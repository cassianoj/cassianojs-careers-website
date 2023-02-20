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
    data = []
    for dict_row in result.mappings():
      data.append(dict(dict_row))
    return data


def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(
      text("select * from cassianojs.jobs where id = :val"), {"val": id})
    data = []
    for dict_row in result.mappings():
      data.append(dict(dict_row))
    return data
    if len(data) == 0:
      return None
    else:
      data
