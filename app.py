import streamlit as st
from database import create_table, populate_menu
from recommendation import recommend_meal, calculate_nutrition

# Initialize the database
create_table()
populate_menu()

# Page title
st.title("MagicAteAI")
st.write("Discover meals based on your preferences!")

# Restaurant selection
restaurant = st.selectbox(
    "Choose a restaurant:",
    ["Demo Restaurant"]
)

# Meal preference selection
preference = st.selectbox(
    "What are you looking for?",
    ["High Protein", "High Carbs", "Low Fat"]
)

# Recommendation button
if st.button("Find My Meal"):
    meal = recommend_meal(restaurant, preference)

    if meal is None:
        st.warning("No recommendation available.")

    else:
        st.subheader("Your Recommended Meal")

        for item in meal:
            st.write(item[2])

        calories, protein, carbs, fat = calculate_nutrition(meal)

        st.write("### Nutritional Information")
        st.write(f"Calories: {calories}")
        st.write(f"Protein: {protein}g")
        st.write(f"Carbs: {carbs}g")
        st.write(f"Fat: {fat}g")

        st.caption(
            "Nutrition values are illustrative demo data."
        )
