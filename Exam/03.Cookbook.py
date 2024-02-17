def cookbook(*args):
    book = {}

    for info in args:
        recipe_name = info[0]
        cuisine = info[1]
        ingredients = info[2]

        if cuisine not in book:
            book[cuisine] = []
        book[cuisine].append((recipe_name, ingredients))

    sorted_book = sorted(book.items(), key=lambda x: (-len(x[1]), x[0]))

    result = ""

    for curr_cuisine in sorted_book:
        result += f"{curr_cuisine[0]} cuisine contains {len(curr_cuisine[1])} recipes:\n"
        sorted_recipes = sorted(book[curr_cuisine[0]], key=lambda x: x[0])

        for recipe in sorted_recipes:
            curr_recipe_name = recipe[0]
            curr_ingredients = recipe[1]

            result += f"  * {curr_recipe_name} -> Ingredients: {', '.join(curr_ingredients)}\n"

    return result.strip()




print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"])
))




