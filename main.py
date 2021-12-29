from flask import Flask, request, jsonify, abort

from config import config
from db import db, Widget


def create_app(config_name: str) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    db.init_app(app)
    with app.app_context():
        db.create_all()

    @app.route('/')
    def hello_world():
        return 'Hello, Docker!'

    @app.route('/widgets', methods=["GET"])
    def get_widgets():
        widgets = Widget.query.all()

        return jsonify([widget.to_dict() for widget in widgets]), 200

    @app.route('/widgets', methods=["POST"])
    def post_widget():
        body = request.get_json()
        wg = Widget(**body)
        db.session.add(wg)
        db.session.commit()
        return "widget created", 200

    @app.route('/widgets/<widget_id>', methods=["DELETE"])
    def delete_widget(widget_id: str):
        widget = Widget.query.filter_by(name=widget_id).first()
        if not widget:
            abort(404, "Record not found")
        db.session.delete(widget)
        db.session.commit()
        return f"widget {widget_id} deleted", 200

    @app.route('/widgets/<name>', methods=["GET"])
    def get_widget_by_name(name: str):
        widget = Widget.query.filter_by(name=name).first()
        if not widget:
            abort(404, "Record not found")
        return jsonify(widget.to_dict()), 200

    return app
