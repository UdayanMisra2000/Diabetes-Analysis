# Diabetes Data Analysis

## Overview
This project analyzes a diabetes dataset using statistical methods and visualization techniques to answer a specific research question. The report is written in **LaTeX**, and includes descriptive statistics, correlation analysis, hypothesis testing, and graphical representations.

## Dataset Information
- **Source**: Pima Indians Diabetes Dataset
- **Attributes**:
  - Pregnancies
  - Glucose
  - BloodPressure
  - SkinThickness
  - Insulin
  - BMI
  - DiabetesPedigreeFunction
  - Age
  - Outcome (0: No Diabetes, 1: Diabetes)

## Research Question
"What are the key factors that influence diabetes, and how strongly are they correlated with the outcome?"

## Analysis Performed
1. **Descriptive Statistics**:
   - Mean, Median, Mode
   - Standard Deviation, Variance
   - Skewness & Kurtosis
2. **Correlation Analysis**:
   - Pearson Correlation Matrix
3. **Hypothesis Testing**:
   - T-tests & Chi-square tests for feature significance
4. **Data Visualization**:
   - Histograms, Box Plots, Scatter Plots, Heatmaps

## How to Use
1. **Clone the Repository** (if applicable):
   ```bash
   git clone https://github.com/UdayanMisra2000/Diabetes-Analysis
   ```
2. **Run the Python Code** to generate statistical results and figures.
   ```bash
   python analysis.py
   ```
3. **Compile the LaTeX Report**:
   - Open `report.tex` in Overleaf or a local LaTeX editor.
   - Ensure the images are in the correct path.
   - Compile the document to generate the final PDF.

## File Structure
```
├── data/
│   ├── diabetes.csv
├── figures/
│   ├── glucose_histogram.png
│   ├── correlation_heatmap.png
├── report/
│   ├── report.tex
│   ├── references.bib
├── scripts/
│   ├── analysis.py
├── README.md
```

## Dependencies
- Python Libraries: `pandas`, `numpy`, `seaborn`, `matplotlib`, `scipy`
- LaTeX Packages: `graphicx`, `float`, `booktabs`

## Acknowledgments
This analysis is based on the Pima Indians Diabetes Dataset and aims to provide statistical insights into diabetes risk factors.

