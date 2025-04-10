
---

```markdown
# Height-to-Weight Predictor 📈

This project is a simple machine learning application that predicts a person's weight based on their height using **Linear Regression**. It also includes a **Tkinter GUI** for user interaction and **Matplotlib** for data visualization.

---

## 💡 Features

- Reads height and weight data from a CSV file
- Trains a Linear Regression model using scikit-learn
- Displays a plot of the data and prediction line
- Provides a user-friendly graphical interface for predictions
- Error handling for invalid inputs

---

## 📁 Dataset

The dataset is a CSV file named `info.csv` and must contain two columns:

- `Height`: Person's height
- `Weight`: Corresponding weight

### Example format:

```csv
Height,Weight
150,55
160,60
170,70
180,80
```

---

## 🧪 How It Works

1. The program reads the data from `info.csv`.
2. It trains a `LinearRegression` model from **scikit-learn** using the height and weight data.
3. It plots:
   - Original data points as **orange dots**
   - Regression line as a **purple line**
4. A simple **Tkinter GUI** allows users to enter a height and get a predicted weight.

---

## 🖥️ GUI Preview

- **Input**: Enter a height (in cm or inches, depending on dataset).
- **Output**: Displays the predicted weight.
- **Buttons**:
  - `Predict`: Triggers the model to generate the weight.
  - `Done`: Closes the application.

---

## 🔧 Requirements

- Python 3.x
- Libraries:
  - `numpy`
  - `pandas`
  - `matplotlib`
  - `scikit-learn`
  - `tkinter` (comes pre-installed with Python)

You can install missing packages using:

```bash
pip install numpy pandas matplotlib scikit-learn
```

---

## 🚀 How to Run

1. Clone this repository:

```bash
git clone https://github.com/your-username/height-weight-predictor.git
cd height-weight-predictor
```

2. Make sure `info.csv` is in the same directory.
3. Run the Python script:

```bash
python predictor.py
```

---

## 📸 Output Sample

![Scatter Plot with Regression Line](https://via.placeholder.com/600x300?text=Sample+Plot)

*(Replace the above with a real screenshot if you'd like)*

---

## 📌 Notes

- Make sure the `info.csv` file is correctly formatted.
- This app is ideal for learning basic machine learning, GUI design, and data visualization with Python.

---

## ⚠️ Disclaimer

This project is a **simple practice exercise** and is not intended for production use. The dataset used is **very limited**, which results in **high prediction error**. The purpose of this code is purely educational — to demonstrate basic concepts in machine learning, data visualization, and GUI development with Python.

---

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 💬 Author

Created by [**Fahimeh**] 💻  
Feel free to contribute or ask questions!
```