import joblib
import pandas as pd

# بارگذاری مدل ذخیره‌شده
model = joblib.load("signal_loss_model.pkl")

# فرض کنید داده‌های جدید دارید (برای پیش‌بینی)
new_data = pd.DataFrame({
    "Input Power (dBm)": [5],
    "Fiber Length (km)": [20],
    "Temperature (°C)": [25],
    "Number of Connectors": [3]
})

# پیش‌بینی با استفاده از مدل
prediction = model.predict(new_data)
print(f"Predicted Signal Loss (dB): {prediction[0]}")
