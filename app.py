from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# بارگذاری مدل ذخیره‌شده
model = joblib.load("signal_loss_model.pkl")

@app.route('/predict', methods=['POST'])
def predict():
    # دریافت داده‌های ورودی از درخواست
    data = request.get_json()
    new_data = pd.DataFrame(data, index=[0])

    # پیش‌بینی با استفاده از مدل
    prediction = model.predict(new_data)
    return jsonify({"Predicted Signal Loss (dB)": prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)
