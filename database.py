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