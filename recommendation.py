from database import get_menu
from itertools import product

def categorize_menu(restaurant):
    menu = get_menu(restaurant)

    mains = []
    sides = []
    drinks = []

    for item in menu:
        category = item[3]

        if category == "Main":
            mains.append(item)

        elif category == "Side":
            sides.append(item)

        elif category == "Drink":
            drinks.append(item)

    return mains, sides, drinks


def generate_combinations(restaurant):
    mains, sides, drinks = categorize_menu(restaurant)

    combinations = list(product(mains, sides, drinks))

    return combinations


def recommend_high_protein(restaurant):
    combinations = generate_combinations(restaurant)

    if not combinations:
        return None

    best_meal = None
    highest_protein = -1

    for meal in combinations:
        calories, protein, carbs, fat = calculate_nutrition(meal)

        if protein > highest_protein:
            highest_protein = protein
            best_meal = meal

    return best_meal


def recommend_meal(restaurant, preference):
    combinations = generate_combinations(restaurant)

    if not combinations:
        return None

    best_meal = None
    best_score = None

    for meal in combinations:
        calories, protein, carbs, fat = calculate_nutrition(meal)

        if preference == "High Protein":
            score = protein

        elif preference == "High Carbs":
            score = carbs

        elif preference == "Low Fat":
            score = -fat

        else:
            return None

        if best_score is None or score > best_score:
            best_score = score
            best_meal = meal

    return best_meal



def calculate_nutrition(meal):
    total_calories = 0
    total_protein = 0
    total_carbs = 0
    total_fat = 0

    for item in meal:
        total_calories += item[4]
        total_protein += item[5]
        total_carbs += item[6]
        total_fat += item[7]

    return total_calories, total_protein, total_carbs, total_fat




if __name__ == "__main__":

    preferences = ["High Protein", "High Carbs", "Low Fat"]

    for preference in preferences:
        meal = recommend_meal("Demo Restaurant", preference)

        print(f"\nPreference: {preference}")
        print("-------------------------")

        if meal is None:
            print("No recommendation available.")
            continue

        for item in meal:
            print(item[2])

        calories, protein, carbs, fat = calculate_nutrition(meal)

        print(f"Calories: {calories}")
        print(f"Protein: {protein}g")
        print(f"Carbs: {carbs}g")
        print(f"Fat: {fat}g")


