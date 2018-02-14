import sys
from argparse import ArgumentParser
from tut.models.astronomy import Planet
from tut.services import conversion


def homework_not_okay():
    """
    Convert the distances of planets from AU to Millions of KM
    """
    # 1 AU = 149,597,870.7 KM
    mkm_per_au = 141.6
    mercury = 0.39
    venus = 0.723
    earth = 1.0
    mars = 1.524
    print(mercury * mkm_per_au)
    print(venus * mkm_per_au)
    print(earth * mkm_per_au)
    print(mars * mkm_per_au)


def homework_lazy():
    """
    Convert the distances of planets from AU to Millions of KM
    """
    planet_names = ['Mercury', 'Venus', 'Earth', 'Mars']
    planet_dists = [0.39, 0.723, 1.0, 1.524]
    # 1 AU = 149,597,870.7 KM
    mkm_per_au = 141.6

    for i in range(4):
        print(planet_names[i] + " " + str(planet_dists[i] * mkm_per_au))


def homework_okay():
    """
    Convert the distances of planets from AU to Millions of KM
    """
    planets = [('Mercury', 0.39), ('Venus', 0.723), ('Earth', 1.0), ('Mars', 1.524)]
    mkm_per_au = 141.6

    for planet in planets:
        name, dist = planet
        print("%10s: %8.3fkm" % (name, dist * mkm_per_au))


def homework_try_hard():
    """
    Convert the distances of planets from AU to Millions of KM
    """
    planets = [
        Planet('Mercury', 0.39),
        Planet('Venus', 0.723),
        Planet('Earth', 1.0),
        Planet('Mars', 1.524)
    ]

    for planet in map(lambda p: (p.name, conversion.au_to_mkm(p.dist)), planets):
        print("%10s: %8.3fkm" % planet)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('version', action='store', help='Options: Bad, Lazy, Good, Overkill', default='bad')
    args = parser.parse_args(sys.argv[1:])

    version = args.version.lower()

    if version == 'bad':
        homework_not_okay()
    elif version == 'lazy':
        homework_lazy()
    elif version == 'good':
        homework_okay()
    elif version == 'overkill':
        homework_try_hard()
