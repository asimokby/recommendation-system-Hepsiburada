from flask import Flask, request, jsonify
import json
from recommendation_methods import cb_m1_recommend
app = Flask(__name__)



@app.route('/get_related_products', methods=["POST"])
def recommend_products():
    data = json.loads(request.get_data())
    product_id = data['product_id']
    product_ids, similarities = cb_m1_recommend(product_id, 10)
    return jsonify({'ids': product_ids, 'sims': similarities})




if __name__ == '__main__':
    app.run(debug=True)