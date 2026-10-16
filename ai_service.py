from ollama import chat


def explain_meal(meal, preference, nutrition):

    # Unpack the meal's nutritional information
    calories, protein, carbs, fat = nutrition

    # Extract the names of the menu items
    item_names = [item[2] for item in meal]

    # Create the prompt for our AI model
    prompt = f"""
    You are a restaurant meal recommendation assistant.

    The customer's preference is: {preference}

    Recommended meal:
    {", ".join(item_names)}

    Nutritional information:
    Calories: {calories}
    Protein: {protein}g
    Carbohydrates: {carbs}g
    Fat: {fat}g

    Explain why this meal matches the customer's preference.

    Use only the information provided.
    Do not invent nutritional information.
    Keep the explanation brief (2-3 sentences).

    Do not include your reasoning process.
    Do not use <think> tags.
    Output only the final explanation.
    """

    # Send the prompt to Ollama
    response = chat(
    model="qwen3:4b",
    messages=[
        {"role": "user", "content": prompt}
    ],
    think=False,
    options={"num_predict": 500}
    
)

    explanation = response.message.content or ""

    # Keep only the text after the final reasoning block
    if "</think>" in explanation:
        explanation = explanation.rsplit("</think>", 1)[-1]

    return explanation.strip()

# Test

if __name__ == "__main__":

    from recommendation import recommend_meal, calculate_nutrition

    # Retrieve a recommended meal
    meal = recommend_meal("Demo Restaurant", "High Protein")

    if meal is not None:

        # Calculate the meal's nutrition
        nutrition = calculate_nutrition(meal)

        # Generate an AI explanation
        explanation = explain_meal(
            meal,
            "High Protein",
            nutrition
        )

        print("AI EXPLANATION:")
        print(explanation)

    else:
        print("No meal recommendation available.")
