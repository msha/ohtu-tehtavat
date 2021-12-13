from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn,Not,HasFewerThan,Or
from querybuilder import QueryBuilder

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    query = QueryBuilder()
    matcher = (
      query  
        .playsIn("NYR")  
        .hasAtLeast(5, "goals")  
        .hasFewerThan(10, "goals")  
        .build()
    )


#     matcher = And(
#     HasAtLeast(40, "points"),
#     Or(
#         PlaysIn("NYR"),
#         PlaysIn("NYI"),
#         PlaysIn("BOS")
#     )
# )

    for player in stats.matches(matcher):
        print(player)


if __name__ == "__main__":
    main()
