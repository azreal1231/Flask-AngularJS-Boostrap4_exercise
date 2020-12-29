import decimal


def returnUsers(request, _params):
    print(_params)
    records = \
        [
            {'id': 'f4d8c6d7-58f0-4ad6-b26c-8716392be9af', 'name': 'user-1', 'email': 'user1@gmail.com',
             'number': '1234567890', 'status': 'single', 'risk': 'low', 'cash': '5000.00'},
            {'id': '1a2e537b-8e60-4c09-8566-906bb9f4ddea', 'name': 'user-2', 'email': 'user2@gmail.com',
             'number': '1234567890', 'status': 'single', 'risk': 'low', 'cash': '6620.0'},
            {'id': '3b55bdcb-cdea-4609-898c-347a57e2910c', 'name': 'user-3', 'email': 'user3@gmail.com',
             'number': '1234567890', 'status': 'single', 'risk': 'medium', 'cash': '5050.0'},
            {'id': '258f5ada-b27d-448e-ab34-13e83accd4fd', 'name': 'lowerance', 'email': 'loweranceTheDude@gmail.com',
             'number': '1234567890', 'status': 'married', 'risk': 'high', 'cash': '-770.00'},
            {'id': 'c58c038b-1a12-430d-8681-359ff0fd560e', 'name': 'user-5', 'email': 'user5@gmail.com',
             'number': '1234567890', 'status': 'unemployed', 'risk': 'medium', 'cash': '900.0'},
            {'id': 'e690e8ad-cd08-421f-be80-1405433565ad', 'name': 'user-6', 'email': 'user6@gmail.com',
             'number': '1234567890', 'status': 'homeless', 'risk': 'high', 'cash': '0.00'},
            {'id': 'e690e8ad-cd08-421f-be80-1405433565ad', 'name': 'user-12', 'email': 'user12@gmail.com',
             'number': '1234567890', 'status': 'homeless', 'risk': 'high', 'cash': '6546321'}

        ]
    return records
