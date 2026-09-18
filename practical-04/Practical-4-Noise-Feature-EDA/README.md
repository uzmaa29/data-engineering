# Practical 4 – Noise Elimination, Feature Selection and EDA

## Aim

To perform **Noise Elimination, Feature Selection, and Exploratory Data Analysis (EDA)** using Python with Pandas, NumPy, Matplotlib, and Scikit-learn.

## Libraries Used

- Pandas – data loading and manipulation
- NumPy – numerical operations
- Matplotlib – visualization
- Scikit-learn – feature selection

## Dataset

The sample student dataset contains `Age`, `Marks`, `Attendance`, and `Constant`. The value `Age = 100` is included as a potential outlier/noisy value. `Constant` is deliberately constant to demonstrate zero-variance feature removal.

## 1. Noise Elimination

The program uses the Interquartile Range (IQR) method to identify potential outliers in `Age`.

```text
IQR = Q3 - Q1
Lower Bound = Q1 - 1.5 × IQR
Upper Bound = Q3 + 1.5 × IQR
```

Values outside the boundaries are removed.

## 2. Feature Selection

`VarianceThreshold(threshold=0.0)` removes features having zero variance. Since `Constant` contains the same value in every row, it is removed.

Selected features after cleaning:

```text
Age
Marks
Attendance
```

## 3. Exploratory Data Analysis

The program performs:

- `info()` for dataset structure and data types
- `describe()` for statistical summary
- `corr()` for numerical correlations
- Histogram for feature distributions
- Boxplot for spread and potential outliers

## How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Run from the repository root:

```bash
python practical_4.py
```

## Repository Structure

```text
Practical-4-Noise-Feature-EDA/
├── README.md
├── practical_4.py
├── requirements.txt
└── data/
    └── sample_student_data.csv
```

## Result

The dataset is cleaned using IQR-based noise elimination, zero-variance features are removed using `VarianceThreshold`, and EDA is performed using descriptive statistics, correlation analysis, histogram, and boxplot.

## Conclusion

Noise elimination improves data quality, feature selection removes unnecessary variables, and EDA helps understand the structure, distribution, and relationships within the cleaned dataset.
