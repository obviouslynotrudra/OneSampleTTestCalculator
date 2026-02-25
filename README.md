# 📊 One Sample T-Test Calculator (Streamlit App)

An interactive web application built using **Streamlit** that performs a **One-Sample T-Test** for hypothesis testing.

This app allows users to:
- Input custom datasets
- Define null hypothesis mean (μ₀)
- Choose significance level (α)
- Select alternative hypothesis (two-sided, greater, less)
- View test statistics and decision instantly

---

## 🚀 Features

- Clean and simple UI
- Manual dataset input (comma-separated values)
- Supports:
  - Two-sided test
  - Right-tailed test
  - Left-tailed test
- Displays:
  - Sample mean
  - Sample standard deviation
  - t-statistic
  - Degrees of freedom
  - p-value
  - Hypothesis decision

---

## 📂 Project Structure

```
├── app1.py
├── README.md
└── requirements.txt
```

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the app

```bash
streamlit run app.py
```

---

## 📦 Requirements

Create a `requirements.txt` file with:

```
streamlit
numpy
scipy
```

---

## 🧠 Statistical Background

The One-Sample T-Test is used to determine whether the sample mean differs significantly from a known or hypothesized population mean.

Test statistic:

$begin:math:display$
t \= \\frac\{\\bar\{x\} \- \\mu\_0\}\{s\/\\sqrt\{n\}\}
$end:math:display$

Where:
- $begin:math:text$ \\bar\{x\} $end:math:text$ = sample mean  
- $begin:math:text$ \\mu\_0 $end:math:text$ = hypothesized mean  
- $begin:math:text$ s $end:math:text$ = sample standard deviation  
- $begin:math:text$ n $end:math:text$ = sample size  

---

## 🎯 Use Cases

- Academic projects
- Statistical learning
- Hypothesis testing practice
- Quick statistical calculations

---

## 🔮 Future Improvements

- CSV file upload support
- Histogram visualization
- T-distribution curve with rejection region
- Two-sample independent t-test
- Paired t-test
- Export results as PDF

---

## 👨‍💻 Author

Developed as a learning project in statistical computing and data science.

