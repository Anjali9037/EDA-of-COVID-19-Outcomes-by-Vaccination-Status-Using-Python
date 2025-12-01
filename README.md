# COVID-19 Vaccination Outcomes – Exploratory Data Analysis (EDA)

This project performs a comprehensive data analytics study on COVID-19 vaccination outcomes, systematically executing the complete data analysis pipeline using Python. The analysis examines vaccine effectiveness across different demographic groups, time periods, and outcome types to provide data-driven insights for public health decision-making.

## Project Structure
```
COVID-19-Vaccination-Outcomes-EDA/
│
├── README.md                          <-- You are here
├── data/
│   ├── raw/                           <-- Original dataset (not uploaded due to size)
│   └── cleaned/                       <-- COVID19_Vaccination_Outcomes_Cleaned.csv
├── notebooks/                         <-- Jupyter/Colab notebooks with complete analysis
├── scripts/                           <-- data_cleaning.py and visualization_utils.py
├── reports/
│   └── analysis_report           <-- Comprehensive findings document(Colab notebooks with complete analysis_report)
└── visuals/                           <-- Generated charts and graphs
```

## Project Objectives

This project aims to:

- Quantify vaccine effectiveness in reducing COVID-19 cases, hospitalizations, and deaths
- Analyze demographic patterns in vaccination coverage and outcomes
- Examine temporal trends in vaccine performance across pandemic phases
- Identify age-specific risk reduction from vaccination
- Compare effectiveness of primary vaccination vs. booster doses
- Provide data-driven recommendations for public health strategies

## Phase 1 — Problem Definition & Dataset Selection

### Problem Statement
The COVID-19 pandemic required rapid evaluation of vaccine effectiveness across diverse populations. Public health officials needed evidence-based insights to:

- Optimize vaccination strategies and resource allocation
- Target interventions to high-risk demographic groups
- Monitor vaccine performance over time and against new variants
- Inform public health communication and policy decisions

### Dataset Details
- **Source**: Public health surveillance systems
- **Time Period**: April 2021 - December 2023
- **Records**: 2,320 weekly observations
- **Features**: 21 variables including derived metrics
- **Outcomes**: Cases, Hospitalizations, Deaths stratified by vaccination status
- **Demographics**: Age groups from 0-4 to 80+ years

## Phase 2 — Data Cleaning & Pre-processing

### Dataset Issues Identified and Handled:
✔ **Missing Values Treatment**
- Rate columns preserved NaN values for accurate analysis
- Population columns replaced zeros with NaN (representing missing data)
- Outcome counts kept zeros (representing actual zero cases)

✔ **Data Standardization**
- Consolidated age group coding (80+ vs 80-200, 999 for "All")
- Standardized date formatting for temporal analysis
- Created consistent categorical labels

✔ **Feature Engineering**
- **Age Group Categories**: 0-10 Years, 11-24 Years, 25-50 Years, 50-80 Years, 80+ Years
- **Temporal Features**: Year, Month, Week_Number for time-series analysis
- **Vaccination Periods**: Early, Mid, Late Vaccination phases
- **Effectiveness Metrics**: Risk reduction percentages, comparative ratios

✔ **Data Validation**
- Checked for negative values in rates (none found)
- Validated rate vs outcome count consistency
- Ensured logical relationships between columns

### Output
The cleaned dataset is saved at: `/data/cleaned/COVID19_Vaccination_Outcomes_Cleaned.csv`

## Phase 3 — Exploratory Data Analysis (EDA)

Performed Univariate, Bivariate, and Multivariate analysis with 15+ visualizations.

### 🔹 Univariate Analysis
- Outcome type distribution (Cases, Hospitalizations, Deaths)
- Age group distribution across records
- Vaccination status percentage composition
- Rate distributions by vaccination category

### 🔹 Bivariate Analysis
- Death rates comparison: Vaccinated vs Unvaccinated
- Vaccination percentage by age group
- Risk ratios across different outcome types
- Temporal trends in vaccine effectiveness

### 🔹 Multivariate Analysis
- Correlation heatmap of key vaccination metrics
- Faceted scatter plots by outcome type and age group
- Time-series analysis of multiple variables
- Demographic and temporal interaction effects

### Visualizations Created
15+ comprehensive plots using:
- **Matplotlib** for custom charts and layouts
- **Seaborn** for statistical visualizations
- **Plotly** for interactive exploration
- **Statistical summaries** for quantitative validation

## Key Insights

### Vaccine Effectiveness Evidence:
- **44.2% reduction in COVID-19 mortality** among vaccinated individuals
- **Sustained protection** across all outcome types (Cases 41.9%, Hospitalizations 36.6%, Deaths 44.2%)
- **Consistent effectiveness** maintained through different pandemic phases

### Demographic Patterns:
- **Highest vaccination coverage**: 50-80 age group (75.1%) - risk-based prioritization success
- **Lowest vaccination coverage**: 0-10 age group (17.1%) - reflects eligibility timeline
- **Unexpected pattern**: 80+ group (56.4%) lower than middle-aged - potential access barriers

### Temporal Trends:
- **Peak vaccination period**: October 2021 - aligned with widespread availability
- **Study duration**: 33 months covering multiple variant waves
- **Stable effectiveness**: Protection persisted despite evolving virus

### Public Health Implications:
- Vaccines demonstrated strongest impact on mortality reduction
- All age groups benefited from vaccination
- Protection maintained across the entire monitoring period

## Conclusion

This project demonstrates a complete end-to-end data analytics pipeline:

- **Clear public health problem framing** with real-world relevance
- **Professional-level data cleaning and preprocessing** handling real surveillance data complexities
- **Comprehensive exploratory analysis** using multiple statistical approaches
- **Actionable insights** directly applicable to public health decision-making
- **Robust visualization portfolio** suitable for academic and policy audiences

The analysis provides strong evidence supporting COVID-19 vaccination as a critical public health intervention, highlighting skills in Python, statistical analysis, data visualization, and domain-specific insight generation.

## How to Use This Project

1. **Clone the repository**
   ```bash
   git clone https://github.com/Anjali9037/EDA-of-COVID-19-Outcomes-by-Vaccination-Status-Using-Python
   ```

2. **Install requirements**
   ```bash
   pip install -r requirements.txt
   ```

3. **Explore the analysis**
   - Complete analysis available in: `/notebooks/`
   - Data cleaning scripts in: `/scripts/`
   - Generated insights in: `/reports/`

## Technical Skills Demonstrated

- **Python Programming**: Pandas, NumPy, Matplotlib, Seaborn
- **Data Cleaning & Preprocessing**: Missing value handling, feature engineering, data validation
- **Statistical Analysis**: Descriptive statistics, correlation analysis, trend analysis
- **Data Visualization**: Multiple chart types, effective storytelling, professional presentation
- **Domain Knowledge**: Public health, epidemiology, vaccination strategies
- **Project Management**: End-to-end pipeline execution, documentation, reproducibility

## Author

ANJALI KRISHNA SURESH
GitHub:https://github.com/Anjali9037

---

*This project serves as a comprehensive demonstration of data analytics capabilities suitable for academic evaluation, job portfolios, and public health research applications.*
