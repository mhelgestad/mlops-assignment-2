from flask import Flask, request, jsonify, render_template
from analyze import get_sentiment, compute_embeddings, classify_email, add_new_email_classes, load_class_file, \
    get_email_classes

app = Flask(__name__, template_folder='templates')

@app.route("/")
def home():
    print("Home page")
    return render_template('index.html')


@app.route("/api/v1/sentiment-analysis/", methods=['POST'])
def analysis():
    if request.is_json:
        data = request.get_json()
        sentiment = get_sentiment(data['text'])
        return jsonify({"message": "Data received", "data": data, "sentiment": sentiment}), 200
    else:
        return jsonify({"error": "Invalid Content-Type"}), 400


@app.route("/api/v1/valid-embeddings/", methods=['GET'])
def valid_embeddings():
    embeddings = compute_embeddings()
    formatted_embeddings = []
    for text, vector in embeddings:
        formatted_embeddings.append({
            "text": text,
            "vector": vector.tolist() if hasattr(vector, 'tolist') else vector
        })
    embeddings = formatted_embeddings
    return jsonify({"message": "Valid embeddings fetched", "embeddings": embeddings}), 200


@app.route("/api/v1/classify/", methods=['POST'])
def classify():
    if request.is_json:
        data = request.get_json()
        text = data['text']
        classifications = classify_email(text)
        return jsonify({"message": "Email classified", "classifications": classifications}), 200
    else:
        return jsonify({"error": "Invalid Content-Type"}), 400


@app.route("/api/v1/classify-email/", methods=['GET'])
def classify_with_get():
    text = request.args.get('text')
    classifications = classify_email(text)
    return jsonify({"message": "Email classified", "classifications": classifications}), 200

@app.route("/api/v1/add-classes/", methods=['POST'])
def add_classes():
    if request.is_json:
        data = request.get_json()
        new_classes = data["classes"]
        add_new_email_classes(new_classes)
        return jsonify({"message": "Classes Added Successfully"}), 200
    else:
        return jsonify({"error": "Invalid Content-Type"}), 400

@app.route("/api/v1/classes/", methods=['GET'])
def get_classes():
    classes = get_email_classes()
    return jsonify({"classes": classes})


if __name__ == "__main__":
    load_class_file()
    app.run(host='0.0.0.0', port=3000, debug=True)