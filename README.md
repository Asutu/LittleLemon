# README

This is the Capstone project for the Little Lemon web application in the Meta Back-End Developer course.


To run the tests:

```bash
python manage.py test restaurant.tests.test_models
python manage.py test restaurant.tests.test_views
```


To connect to the MySQL database, these credentials are set in the `settings.py` file:

- `'NAME': 'LittleLemon'` : this is the database name where to write the tables from this Django project
- `'USER': 'admindjango'` : mysql username with grants to manage the database
- `'PASSWORD': 'lemon@123!'`: mysql username password
- `'HOST': 'localhost'`: the host address for mysql

Note that any of the above parameters should be changed in the `settings.py` file to work with your database.
For example, in some MySQL setups, `localhost` is not a valid host address and `127.0.0.1` should be used instead.


Test the following:

- make a table reservation using the API: `/restaurant/booking/tables/`
    + `name`, `guest_number`, `reservation_date`, and `reservation_slot` are required fields
    + the user must be authenticated
- see all reservations: `/restaurant/booking/tables/`
    + the user must be authenticated
- see all menu items: `/restaurant/menu/`
    + any user can access this API
- add a new menu item: `/restaurant/menu/`
    + `title` and `price` are required fields
    + `category`, `inventory`, `featured`, and `description` are optional
    + only an admin user is authorized
- change the "featured" status of a menu item: `/restaurant/menu/{id}`
    + only an admin user is authorized
