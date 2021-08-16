# Adds 1 star, then 2 stars, then 3 stars, and 4 stars
stars = ""
for i in range(0, 5, 1):
    for j in range(0, i, 1):
        stars += "*"
    print(stars)