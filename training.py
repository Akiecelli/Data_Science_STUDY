random_cities_dict = {'Saint-Petersburg':5, 'Moscow':4,'Los-Angeles':5, 'Kiev':3, 'New-Orleans':5, 'Paris':4,'London':4,'New-York':3}
def find_city(cities):
    visit = []
    watch = []
    not_visit = []
    for city in cities:
        rating = cities[city]
        if rating >= 5:
            visit.append(city)
        elif rating == 4:
            watch.append(city)
        else:
            not_visit.append(city)
    print(f'Places you will like: {visit}')
    print(f'Places you will like to watch: {watch}')
    print(f'Places you will not like: {not_visit}')    
find_city(random_cities_dict)