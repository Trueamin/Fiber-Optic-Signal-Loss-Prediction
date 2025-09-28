import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import joblib

# بارگذاری داده‌ها از فایل CSV
data = pd.read_csv("fiber_optic_dataset.csv")

# جدا کردن ویژگی‌ها (X) و برچسب‌ها (y)
X = data.drop("Signal Loss (dB)", axis=1)
y = data["Signal Loss (dB)"]

# تقسیم داده‌ها به داده‌های آموزش و تست (80% آموزش، 20% تست)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# تعریف مدل رگرسیون خطی
model = LinearRegression()

# آموزش مدل با داده‌های آموزشی
model.fit(X_train, y_train)

# ارزیابی مدل با داده‌های تست
score = model.score(X_test, y_test)
print(f"R^2 Score: {score}")

# ذخیره مدل به فایل
joblib.dump(model, "signal_loss_model.pkl")
