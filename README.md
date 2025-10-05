# Kaká Impact Analysis

An analysis of how Brazilian midfielder Ricardo Kaká's presence affected AC Milan's match outcomes using historical match data from the European Soccer Database.

## 📊 Project Overview

This project analyzes AC Milan matches to determine whether Kaká's presence on the roster had a statistically significant impact on the team's performance and goal-scoring ability.

## 🔍 Key Findings

- **Correlation**: -0.011 (very weak correlation between Kaká's presence and goals scored)
- **T-Test Result**: P-value of 0.845 (no significant difference in goals with/without Kaká)
- **Logistic Regression Accuracy**: 47.5% (limited predictive power using only Kaká's presence)
- The analysis suggests that using only a single player's presence is insufficient to predict match outcomes

## 🛠️ Technologies Used

- **Python** - Data analysis and processing
- **SQL** - Querying the European Soccer Database (SQLite)
- **Pandas** - Data manipulation and analysis
- **Matplotlib** - Data visualization
- **scikit-learn** - Logistic regression modeling
- **Jupyter Notebook** - Development environment

## 📈 Methodology

1. Connected to European Soccer Database (SQLite)
2. Filtered AC Milan matches from the Match table
3. Identified matches where Kaká played by checking player IDs
4. Performed statistical analysis:
   - T-test to compare goals with/without Kaká
   - Correlation analysis
   - Logistic regression for win prediction
5. Visualized results using bar charts
