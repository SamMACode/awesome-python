# “Build a list of Unicode codepoints from a string"
symbols = '$¢£¥€¤'
codes = []
for symbol in symbols:
    codes.append(ord(symbol))
# “more readable because its intent is explicit”
sort_codes = [ord(symbol) for symbol in symbols]
print(f"all items in codes are: {codes}, sort_codes value: {sort_codes}")

# listcomps do everything the map and filter functions do
beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
print(f"all the character which beyond 127 are: {beyond_ascii}")
# use python lambda expression
beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))
print(f"use lambda expression to filter character which beyond 127 are: {beyond_ascii}")

# “Cartesian product using a list comprehension”
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]
print(f"use Cartesian operators, value: {tshirts}")
# “uses a genexp with a Cartesian product to print out a roster of T-shirts of two colors in three sizes”
for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
    print(f"{tshirt}")

# "Tuples used as records, for loop statement"
lax_coordinates = (33.9425, -118.408056)
# tuple unpacking
latitude, longitude = lax_coordinates
print(f"latitude: {latitude}, longitude: {longitude}")
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
traveler_ids = [('USA', '31195885'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]
for passport in sorted(traveler_ids):
    print('%s/%s' % passport)
for country, _ in traveler_ids:
    print(country)
