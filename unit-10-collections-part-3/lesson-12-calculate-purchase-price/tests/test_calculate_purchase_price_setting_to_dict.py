def test_calculate_purchase_price_setting_to_dict():
    purchase = {
        'id': 99,
        'books': [{
            'title': 'The Raven',
            'author': 'Edgar Allan Poe',
            'price': 19.99
        }, {
            'title': 'Ulysses',
            'author': 'James Joyce',
            'price': 23.99
        }, {
            'title': 'The Odyssey',
            'author': 'Homer',
            'price': 7.99
        }],
        'total': 0
    }
    total = calculate_purchase_price(purchase, set_to_dict=True)
    assert total == 51.97
    assert purchase['total'] == 51.97