from flask import Blueprint, render_template

bp = Blueprint('property', __name__)


@bp.route('/', methods=['GET'])
def property_list():
    print('[Controller] property_list')
    return render_template('auth/login.html')