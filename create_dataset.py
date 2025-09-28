import pandas as pd
import numpy as np

# تعیین تعداد داده‌ها
num_samples = 1000

# تولید داده‌های تصادفی برای ویژگی‌ها
np.random.seed(42)
input_power = np.random.uniform(0, 10, num_samples)  # توان ورودی (dBm)
fiber_length = np.random.uniform(1, 50, num_samples)  # طول فیبر (km)
temperature = np.random.uniform(-10, 50, num_samples)  # دما (°C)
num_connectors = np.random.randint(1, 6, num_samples)  # تعداد اتصالات

# مدل سازی اتلاف سیگنال (dB) به عنوان تابعی از ویژگی‌ها
signal_loss = (input_power * 0.5) + (fiber_length * 0.1) + (temperature * 0.2) + (num_connectors * 0.3) + np.random.normal(0, 1, num_samples)

# ایجاد دیتافریم از داده‌ها
data = pd.DataFrame({
    "Input Power (dBm)": input_power,
    "Fiber Length (km)": fiber_length,
    "Temperature (°C)": temperature,
    "Number of Connectors": num_connectors,
    "Signal Loss (dB)": signal_loss
})

# ذخیره دیتاست در فایل CSV
data.to_csv("fiber_optic_dataset.csv", index=False)

print("Dataset created and saved as 'fiber_optic_dataset.csv'")
