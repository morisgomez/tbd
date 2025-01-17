#list of years in no particular order:
years = [1925, 1943, 1968, 1937, 1975, 1912, 1989, 1954, 1920, 1996]

years.sort() #organizes in ascending order.
#years.reverse() would produce an error bc last index is less than first. needs to be the opposite.
#what does reverse() do to a list?

print(years)

assert years[0] <= years[-1], "First element is greater than last element."
#is the first value less than the or equal to the last? how is index -1 last in list?
