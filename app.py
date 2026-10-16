import streamlit as st
from database import create_table, populate_menu
from recommendation import recommend_top_meals, calculate_nutrition
from ai_service import explain_meal

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
    meals = recommend_top_meals(restaurant, preference)

    if not meals:
        st.warning("No recommendations available.")

    else:
        st.subheader("Your Top Meal Recommendations")

        for i, meal in enumerate(meals, start=1):
            st.write(f"### Recommendation #{i}")

            for item in meal:
                st.write(item[2])

            calories, protein, carbs, fat = calculate_nutrition(meal)

            st.write(f"Calories: {calories}")
            st.write(f"Protein: {protein}g")
            st.write(f"Carbs: {carbs}g")
            st.write(f"Fat: {fat}g")

            # Generate an AI explanation for the recommended meal
            nutrition = (calories, protein, carbs, fat)

            with st.spinner("Generating AI explanation..."):
                explanation = explain_meal(meal, preference, nutrition)

            st.write("**Why this meal?**")
            st.write(explanation)

            st.divider()

        st.caption("Nutrition values are illustrative demo data.")