import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sbn
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from matplotlib import pyplot as plt
from sklearn.preprocessing import StandardScaler



scaler = StandardScaler()

df = pd.read_csv("diamonds.csv").dropna()
df = df.drop(['Unnamed: 0'], axis=1)
features = ["carat", "cut", "color", "clarity"]

clarity_map = {
    'I1': 1,
    'SI2': 2,
    'SI1': 3,
    'VS2': 4,
    'VS1': 5,
    'VVS2': 6,
    'VVS1': 7,
    'IF': 8
}
df['clarity'] = df['clarity'].map(clarity_map)

color_map = {
    'D': 7,  # Best
    'E': 6,
    'F': 5,
    'G': 4,
    'H': 3,
    'I': 2,
    'J': 1  # Worst
}
df['color'] = df['color'].map(color_map)

cut_map = {
    'Fair': 1,
    'Good': 2,
    'Very Good': 3,
    'Premium': 4,
    'Ideal': 5
}
df['cut'] = df['cut'].map(cut_map)

X = df[features]
Y = df["price"]

X.info()

sbn.histplot(data=df, x="price", kde=1)
plt.title("Distribution des prix des diamants")
plt.show()


st.set_page_config(page_title="Diamond Price Predictor", layout="wide")
st.title("💎 Diamond Price Prediction - Feature Selection")

st.text("Select a feature to add : ")

options = st.multiselect(
    "Choose from the following features",
    ["color", "clarity"],

    default=["color", "clarity"]
)

if options != []:
    X = df[options]
X_train, X_test, y_train, y_test = train_test_split(
        X, Y,
        test_size=0.2,
        random_state=42
    )

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(y_test, y_pred, alpha=0.5, edgecolors='k', s=20)

min_val = min(y_test.min(), y_pred.min())
max_val = max(y_test.max(), y_pred.max())
ax.plot([min_val, max_val], [min_val, max_val], 'r--', lw=2, label='Prédiction parfaite')

ax.set_xlabel('Real price  ($)', fontsize=12)
ax.set_ylabel('Predicted price ($)', fontsize=12)
ax.set_title('Predicted vs real price values', fontsize=14, fontweight='bold')
ax.legend()
ax.grid(True, alpha=0.3)

st.pyplot(fig)