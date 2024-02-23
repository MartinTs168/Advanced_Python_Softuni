def team_lineup(*args):
    country_players_dict = {}

    for player_info in args:
        country = player_info[1]
        player_name = player_info[0]
        if country not in country_players_dict.keys():
            country_players_dict[country] = []
        country_players_dict[country].append(player_name)

    country_players_list = sorted(country_players_dict.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))
    result = ""
    for info in country_players_list:
        country, country_players = info[0], info[1]
        result += f"{country}:\n"
        for player in country_players:
            result += f"  -{player}\n"

    return result


print(team_lineup(
    ("Harry Kane", "England"),
    ("Manuel Neuer", "Germany"),
    ("Raheem Sterling", "England"),
    ("Toni Kroos", "Germany"),
    ("Cristiano Ronaldo", "Portugal"),
    ("Thomas Muller", "Germany")))
