import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Set Streamlit page configuration
st.set_page_config(page_title="🌸 Iris Classifier", layout="centered")

# Title and description
st.title("🌸 Iris Flower Classifier")
st.markdown("""
Enter flower measurements below and click **Predict** to classify the iris species.
This app also vis
            ualizes your prediction against the training data.
""")

# Load and train model
@st.cache_resource
def load_model():
    iris = load_iris()
    X = pd.DataFrame(iris.data, columns=iris.feature_names)
    y = iris.target
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X, y)
    return clf, X, y, iris

model, X_train, y_train, iris = load_model()

# Sidebar input fields
st.sidebar.header("Input Flower Measurements")
def get_user_input():
    return pd.DataFrame([{
        'sepal length (cm)': st.sidebar.slider('Sepal Length (cm)', 4.0, 8.0, 5.8),
        'sepal width (cm)': st.sidebar.slider('Sepal Width (cm)', 2.0, 4.5, 3.0),
        'petal length (cm)': st.sidebar.slider('Petal Length (cm)', 1.0, 7.0, 4.3),
        'petal width (cm)': st.sidebar.slider('Petal Width (cm)', 0.1, 2.5, 1.3)
    }])

input_df = get_user_input()

# Button to trigger prediction
if st.button("🔍 Predict"):
    prediction = model.predict(input_df)[0]
    pred_species = iris.target_names[prediction]
    st.success(f"🌼 Predicted Species: **{pred_species}**")

    # Prepare visualization
    vis_data = X_train.copy()
    vis_data['species'] = [iris.target_names[i] for i in y_train]
    vis_data['is_user_input'] = False

    input_df_vis = input_df.copy()
    input_df_vis['species'] = pred_species
    input_df_vis['is_user_input'] = True

    combined_df = pd.concat([vis_data, input_df_vis], ignore_index=True)

    # 3D plot
    fig = px.scatter_3d(
        combined_df,
        x='sepal length (cm)',
        y='petal length (cm)',
        z='petal width (cm)',
        color='species',
        symbol='is_user_input',
        title="3D Visualization of Your Prediction",
        opacity=0.7
    )
    st.plotly_chart(fig, use_container_width=True)

else:
    st.info("🔎 Adjust values in the sidebar and click **Predict** to classify the flower.")



# App url:- local url:- http://localhost:8501
# network url:- http://192.168.67.215:8501

