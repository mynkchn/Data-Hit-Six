
# 🏏 Data Hit Six – T20 World Cup Analysis & Score Prediction

This project explores and analyzes T20 cricket match data, identifying key insights such as top-performing players, team strengths, and more. It also builds predictive models to estimate a batsman's total runs based on their boundary counts (4s and 6s). The data is sourced from various CSV files and the workflow includes EDA, feature engineering, model building, evaluation, and deployment preparation.

---

## 📁 Project Structure

```
.
├── Data/
│   ├── fact_bating_summary.csv
│   ├── fact_bowling_summary.csv
│   ├── dim_match_summary.csv
│   └── dim_players.csv
├── model.pkl
├── scaler.pkl
└── main.py / notebook.ipynb
```

---

## 🔍 Step-by-Step Overview

### 1. **Data Loading & Preprocessing**
- Load batting, bowling, match, and player data.
- Handle missing or inconsistent values (`SR`, `margin`, etc.).
- Drop irrelevant columns (`image` from players).
- Convert `SR` to float and handle non-numeric placeholders.

### 2. **Data Merging**
- Merge `batting`, `bowling`, and `match` data using `match_id` to prepare for deeper analysis.

### 3. **Exploratory Data Analysis (EDA)**
- Distribution of runs per player per match.
- Top scorers and consistent batsmen based on strike rate and batting position.
- Team performance (most wins, average score, economy).
- Venue-based average scores.
- Wicket distribution and top bowlers.

### 4. **Feature Engineering**
- Aggregate batting data: total 4s, 6s, and runs per player.
- Selected features for modeling: `4s`, `6s`.

### 5. **Model Development**
- **Linear Regression** model to predict runs from boundary stats.
- **Ridge Regression** with hyperparameter tuning using `GridSearchCV`.

### 6. **Model Evaluation**
- Visual comparison of actual vs predicted runs.
- R² scores and Mean Squared Error for both models.
- Cross-validation for performance estimation.

### 7. **Model Saving**
- Serialize trained `LinearRegression` model and `StandardScaler` using `joblib`.

---

## 📊 Key Findings

- Most batsmen score under 40; only a few are consistent top scorers.
- England, Pakistan, Sri Lanka, and India are the most successful teams.
- Stadiums have varied average first innings scores.
- Top bowlers consistently take 2–3 wickets per match, but 5-wicket hauls are rare.
- Strong correlation between 4s/6s and total runs, enabling simple predictive modeling.

---

## 🧠 Tech Stack

- **Languages**: Python
- **Libraries**: `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`, `joblib`
- **Modeling**: Linear & Ridge Regression
- **Data**: T20 World Cup match, player, and performance summaries

---

## 🚀 How to Run

1. Clone the repo:
   ```bash
   git clone https://github.com/mynkchn/Data-Hit-Six.git
   cd Data-Hit-Six
   ```

2. Ensure the data is located in the `Data/` directory.

3. Run the analysis script or notebook:
   ```bash
   python main.py
   ```

4. Predict scores using the trained model (`model.pkl`, `scaler.pkl`).

---

## 🏁 Future Improvements

- Integrate Streamlit or Flask app for interactive predictions.
- Expand features (e.g., opponent, venue, recent form).
- Use advanced models (Random Forest, XGBoost, etc.).
- Time series forecasting for match outcomes.

---

## 👨‍💻 Author

**Mayank Chouhan**  
Cricket Data Enthusiast & ML Developer  
🔗 [GitHub](https://github.com/mynkchn)
