from data import db_session
from flask import Flask

app = Flask(__name__)
api = Api(app)


def main():
    db_session.global_init("db/mars_explorer.db")
    app.register_blueprint(jobs_api.blueprint)
    app.run()


if __name__ == '__main__':
    main()