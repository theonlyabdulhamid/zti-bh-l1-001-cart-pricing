from cart_pricing import calculate_order_summary as COS

order={
        "customer": {"id": "C-101", "name": "Jane", "tier": ""},
        "items": [
            {
                "id": "SKU-1",
                "name": "Wireless Mouse",
                "price": 25.00,
                "quantity": 1,
                "category": "electronics",
                "is_discountable": True
            },
            {
                "id": "SKU-1",
                "name": "Gift Card",
                "price": 50.00,
                "quantity": 1,
                "category": "electronics",
                "is_discountable": True
            }
        ]
    }

total=COS(order)
for key,value in total.items():
    print(f"{key:<20}----------- ${value:<4}")
