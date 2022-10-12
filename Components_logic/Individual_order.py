class IndividualOrder:
    def __init__(self, restaurant_id, items, priority, max_wait):
        self.restaurant_id = restaurant_id
        self.items = items
        self.priority = priority
        self.max_wait = max_wait
        self.created_time = None
