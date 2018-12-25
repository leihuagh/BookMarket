for g in range(1, 1001):
    obj = Genre(
        name="Genre name {}".format(g),
        description='Genre description {}'.format(g)
    )
    obj.save()
    print('object created')

for g in range(1, 1001):
    obj = Author(
        name="Author name {}".format(g),
        description='Author description {}'.format(g)
    )
    obj.save()
    print('object created')

for g in range(1, 1001):
    obj = Series(
        name="Series name {}".format(g),
        description='Series description {}'.format(g)
    )
    obj.save()
    print('object created')

for g in range(1, 1001):
    obj = Publisher(
        name="Publisher name {}".format(g),
        description='Publisher description {}'.format(g)
    )
    obj.save()
    print('object created')

for g in range(1, 1001):
    obj = Manufacturer(
        name="Manufacturer name {}".format(g),
        description='Manufacturer description {}'.format(g)
    )
    obj.save()
    print('object created')

a_book1 = Book(
    name='test_name',
    price=100,
    series=my_series,
    numbers_of_pages=100,
    binding='test',
    pr_format='test1',
    isbn='111-1-11-1-1',
    weight=100,
    age_limit='test2',
    publisher=my_pub,
    manufacturer=my_man,
    stock=100,
    rating=100)

from random import choice


for g in range(1, 1001):
    series = Series.objects.all()
    obj = Book(
        name="Genre name {}".format(g),
        series=choice(series),
        description='Genre description {}'.format(g)
    )
    obj.save()
    print('object created')





