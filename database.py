import sqlalchemy
# establish connectivity
from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv
load_dotenv()
# from sqlalchemy import create_engine
# engine = create_engine("mysql+pymysql://user:pass@some_mariadb/dbname?charset=utf8mb4")

db_connection_string = os.environ.get("DB_CONNECTION_STRING")
print(db_connection_string)

engine = create_engine(db_connection_string, pool_recycle=3600)

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))

        jobs = []
        for row in result.all():
            jobs.append(row._asdict())
        return jobs

def load_job_from_db(id):
    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT * FROM jobs WHERE id = :id"),
            {"id" : id}
        )
        rows = result.all()
        if len(rows) == 0:
            return None
        else:
            return rows[0]._asdict() 


# from sqlalchemy import text
# with engine.connect() as conn:
#     result = conn.execute(text("select * from jobs"))

#     result_dicts = []
#     for row in result.all():
#         result_dicts.append(row._asdict())

    # print(result_dicts)

    # print("type(result):",type(result))
    # result_all = result.all()
    # print("type(result_all):",type(result_all))
    # print("len(result_all):",len(result_all))
    # first_result = result_all[0]._asdict()
    # print("type(first_result):",type(first_result))
    # print(result_all)

    





