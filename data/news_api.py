import flask
from . import db_session
from .all import all
from .cat import cat
from .delivery import delivery
from flask import request as req
from flask import jsonify

blueprint = flask.Blueprint(
    'news_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/category_correct_post', methods=['POST'])
def category_correct_pos():
    db_sess = db_session.create_session()
    news = db_sess.query(cat).get(req.json['cat'])
    db_sess.delete(news)
    db_sess.commit()
    user = cat()
    user.category = req.json['cat']
    user.category_new = req.json['cat_new']
    db_sess.add(user)
    db_sess.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/category_new_post', methods=['POST'])
def category_new_post():
    print(type(req.json))
    user = cat()
    user.category = req.json['cat']
    user.category_new = req.json['cat_new']
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/position_new_post', methods=['POST'])
def position_new_post():
    db_sess = db_session.create_session()
    try:
        e = req.json['category']
        name = req.json['name']
        photo = req.json['photo']
        description = req.json['description']
        cost = req.json['cost']
        fi = db_sess.query(cat).filter(cat.category_new == e).first()
        fi2 = db_sess.query(all).filter(all.category == fi.category).first()
        fi2 = dict(fi2.position)
        news = db_sess.query(all).get(fi.category)
        db_sess.delete(news)
        db_sess.commit()
        user = all()
        user.category = fi.category
        if name not in fi2.keys():
            fi2[name] = {"photo": photo, "description": description, "cost": cost}
            user.position = fi2
        else:
            user.position = fi2

    except Exception:
        fi = db_sess.query(cat).filter(cat.category_new == e).first()
        db_sess.commit()
        user = all()
        user.category = fi.category
        user.position = {name: {"photo": photo, "description": description, "cost": cost}}
    db_sess.add(user)
    db_sess.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/position_correct_posit_name_post', methods=['POST'])
def position_correct_posit_name_post():
    cat_old = req.json['cat_old']
    posit = req.json['posit']
    new_pos = req.json['new_pos']
    db_sess = db_session.create_session()
    fi2 = db_sess.query(all).filter(all.category == cat_old).first()
    val = dict(fi2.position)[posit]
    news = db_sess.query(all).get(cat_old)
    db_sess.delete(news)
    db_sess.commit()
    user = all()
    user.category = cat_old
    user.position = {new_pos: val}
    db_sess.add(user)
    db_sess.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/position_correct_posit_photo_post', methods=['POST'])
def position_correct_posit_photo_post():
    cat_old = req.json['cat_old']
    posit = req.json['posit']
    encoded = req.json['encoded']
    db_sess = db_session.create_session()
    fi2 = db_sess.query(all).filter(all.category == cat_old).first()
    val = dict(fi2.position)[posit]['description']
    val1 = dict(fi2.position)[posit]['cost']
    news = db_sess.query(all).get(cat_old)
    db_sess.delete(news)
    db_sess.commit()

    user = all()
    user.category = cat_old
    user.position = {posit: {'photo': encoded, 'description': val, 'cost': val1}}
    db_sess.add(user)
    db_sess.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/position_correct_posit_description_post', methods=['POST'])
def position_correct_posit_description_post():
    cat_old = req.json['cat_old']
    posit = req.json['posit']
    description = req.json['description']
    db_sess = db_session.create_session()
    fi2 = db_sess.query(all).filter(all.category == cat_old).first()
    val = dict(fi2.position)[posit]['photo']
    val1 = dict(fi2.position)[posit]['cost']
    news = db_sess.query(all).get(cat_old)
    db_sess.delete(news)
    db_sess.commit()

    user = all()
    user.category = cat_old
    user.position = {posit: {'photo': val, 'description': description, 'cost': val1}}
    db_sess.add(user)
    db_sess.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/position_correct_posit_cost_post', methods=['POST'])
def position_correct_posit_cost_post():
    cat_old = req.json['cat_old']
    posit = req.json['posit']
    cost = req.json['cost']
    db_sess = db_session.create_session()
    fi2 = db_sess.query(all).filter(all.category == cat_old).first()
    val = dict(fi2.position)[posit]['photo']
    val1 = dict(fi2.position)[posit]['description']
    news = db_sess.query(all).get(cat_old)
    db_sess.delete(news)
    db_sess.commit()

    user = all()
    user.category = cat_old
    user.position = {posit: {'photo': val, 'description': val1, 'cost': cost}}
    db_sess.add(user)
    db_sess.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/delete_category_post', methods=['POST'])
def delete_category_post():
    db_sess = db_session.create_session()
    fi = db_sess.query(cat).filter(cat.category_new == req.json['cat_old']).first()
    news = db_sess.query(cat).get(fi.category)
    db_sess.delete(news)
    db_sess.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/sorted_keys', methods=['GET'])
def sorted_keys():
    db_sess = db_session.create_session()
    q = [prof.category_new for prof in db_sess.query(cat).all()]
    q = sorted(q)
    return jsonify({'q': q})


@blueprint.route('/api/delete_position_post', methods=['POST'])
def delete_position_post():
    position1 = req.json['position1']
    position2 = req.json['position2']
    db_sess = db_session.create_session()
    fi2 = db_sess.query(all).filter(all.category == position1).first()
    fi2 = fi2.position
    dict(fi2.pop(position2))
    news = db_sess.query(all).get(position1)
    db_sess.delete(news)
    db_sess.commit()
    user = all()
    user.category = position1
    user.position = fi2
    db_sess.add(user)
    db_sess.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/self_delivery_post', methods=['POST'])
def self_delivery_post():
    cost = req.json['cost']
    db_sess = db_session.create_session()
    news = db_sess.query(delivery).get("Самовывоз")
    db_sess.delete(news)
    db_sess.commit()

    user = delivery()
    user.delivery = "Самовывоз"
    user.cost = cost
    db_sess.add(user)
    db_sess.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/delivery_delivery_post', methods=['POST'])
def delivery_delivery_post():
    cost = req.json['cost']
    db_sess = db_session.create_session()
    news = db_sess.query(delivery).get("Доставка")
    db_sess.delete(news)
    db_sess.commit()

    user = delivery()
    user.delivery = "Доставка"
    user.cost = cost
    db_sess.add(user)
    db_sess.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/porog_delivery_post', methods=['POST'])
def porog_delivery_post():
    cost = req.json['cost']
    db_sess = db_session.create_session()
    news = db_sess.query(delivery).get("Порог")
    db_sess.delete(news)
    db_sess.commit()

    user = delivery()
    user.delivery = "Порог"
    user.cost = cost
    db_sess.add(user)
    db_sess.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/get_first_fi2/<string:category>', methods=['GET'])
def get_first_fi2(category):
    db_sess = db_session.create_session()
    fi = db_sess.query(cat).filter(cat.category_new == category).first()
    fi2 = db_sess.query(all).filter(all.category == fi.category).first()
    if fi2 == None:
        fi2 = {}
    else:
        fi2 = sorted(dict(fi2.position).keys())
    return jsonify({'fi2': fi2})


@blueprint.route('/api/get_fi/<category>', methods=['GET'])
def get_fi(category):
    db_sess = db_session.create_session()
    fi = db_sess.query(cat).filter(cat.category_new == category).first()
    return jsonify({'fi': fi.category})


@blueprint.route('/api/0_4', methods=['POST'])
def zero_four():
    db_sess = db_session.create_session()
    fi = db_sess.query(cat).filter(cat.category_new == req.json['1']).first()
    fi2 = db_sess.query(all).filter(all.category == fi.category).first()
    fi2 = fi2.position.replace(req.json['2'], "")
    news = db_sess.query(all).get(fi.category)
    db_sess.delete(news)
    db_sess.commit()
    user = all()
    user.category = fi.category
    user.position = fi2
    db_sess.add(user)
    db_sess.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/get_position/<category>', methods=['GET'])
def get_position(category):
    db_sess = db_session.create_session()
    fi = db_sess.query(cat).filter(cat.category_new == category).first()
    fi2 = db_sess.query(all).filter(all.category == fi.category).first()
    return jsonify({'position': fi2.position})


@blueprint.route('/api/get_info/<category>/<position>', methods=['GET'])
def get_info(category, position):
    db_sess = db_session.create_session()
    fi = db_sess.query(cat).filter(cat.category_new == category).first()
    fi2 = db_sess.query(all).filter(all.category == fi.category).first()
    fi2 = dict(fi2.position)[position]
    return jsonify({'info': fi2})


@blueprint.route('/api/get_porog', methods=['GET'])
def get_porog():
    db_sess = db_session.create_session()
    fi = db_sess.query(delivery).filter(delivery.delivery == "Порог").first()
    return jsonify({'porog': fi.cost})


@blueprint.route('/api/get_samdelivery', methods=['GET'])
def get_samdelivery():
    db_sess = db_session.create_session()
    fi = db_sess.query(delivery).filter(delivery.delivery == "Самовывоз").first()
    return jsonify({'samdelivery': fi.cost})


@blueprint.route('/api/get_delivery', methods=['GET'])
def get_delivery():
    db_sess = db_session.create_session()
    fi = db_sess.query(delivery).filter(delivery.delivery == "Доставка").first()
    return jsonify({'delivery': fi.cost})

