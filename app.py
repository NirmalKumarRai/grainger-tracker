from flask import Flask, jsonify, request
from backend.models import ProductResult
from backend import db

app = Flask(__name__)
# CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///database.db'

@app.route('/search', methods=['GET'])
def search_by_mpn():
    mpn = request.args.get('mpn')
    if mpn:
        results = ProductResult.query.filter_by(mpn=mpn).all()
        if results:
            return jsonify([result.serialize() for result in results]), 200
        else:
            return jsonify({'message': 'No results found'}), 404
    else:
        return jsonify({'message': 'MPN parameter is required'}), 400

if __name__ == '__main__':
    app.run(debug=True)
