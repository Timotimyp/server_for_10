from flask import redirect, Flask
from data import db_session, news_api
from data.all import all
from data.cat import cat
from data.delivery import delivery


app = Flask(__name__)

app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
def logout():
    return redirect("Вcё работает как шведцарские часы")


def main():
    db_session.global_init("db/users.db")
    app.register_blueprint(news_api.blueprint)
    app.run(port=5000, host='127.0.0.1')
    # db_sess = db_session.create_session()
    # user = delivery()
    # user.delivery = "Порог"
    # user.cost = 1000
    # db_sess.add(user)
    # user = delivery()
    # user.delivery = "Самовывоз"
    # user.cost = 1000
    # db_sess.add(user)
    # user = delivery()
    # user.delivery = "Доставка"
    # user.cost = 1000
    # db_sess.add(user)
    # db_sess.commit()


if __name__ == '__main__':
    main()