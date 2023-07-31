from structural.adapter.car_example.motorcycle_adapter import MotorcycleAdapter


def main_adapter_car_example():
    bike_adapter = MotorcycleAdapter()

    # Car methods
    try:
        print("Attempting to call client methods with the service object using an adapter\n")
        bike_adapter.assign_driver("Robert")
        bike_adapter.accelerate()
        bike_adapter.apply_brakes()
    except AttributeError:
        print("Oops! bike object cannot access car methods")
