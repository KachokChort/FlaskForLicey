from flask_restful import reqparse, abort, Api, Resource
from . import db_session
from .users import User
from flask import jsonify




def abort_if_news_not_found(user_id):
    session = db_session.create_session()
    if type(user_id) == int:
        news = session.query(User).get(user_id)
    if not news:
        abort(404, message=f"User {user_id} not found")


class UsersResource(Resource):
    def get(self, news_id):
        abort_if_news_not_found(news_id)
        session = db_session.create_session()
        user = session.query(User).get(news_id)
        return jsonify({'news': user.to_dict(
            only=('title', 'content', 'user_id', 'is_private'))})

    def delete(self, news_id):
        abort_if_news_not_found(news_id)
        session = db_session.create_session()
        user = session.query(User).get(news_id)
        session.delete(user)
        session.commit()
        return jsonify({'success': 'OK'})
