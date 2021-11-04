num_of_vans, customers = input('Enter Input : ').split('/')
num_of_vans = int(num_of_vans)
customers = list(map(int, customers.split(' ')))

def custom_argmin(iterable):
    for i, ele in enumerate(iterable):
        if ele is None:
            return i

    return min(enumerate(iterable), key=lambda x: x[1])[0]

reservation = [None for _ in range(num_of_vans)]

for i, customer in enumerate(customers):
    idx_van = custom_argmin(reservation)
    
    # update end reservation
    reservation[idx_van] = (reservation[idx_van] if reservation[idx_van] is not None else 0) + customer
    print(f'Customer {i+1} Booking Van {idx_van+1} | {customer} day(s)')


