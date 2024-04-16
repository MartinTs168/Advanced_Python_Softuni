from typing import List

from project.clients.base_client import BaseClient
from project.clients.regular_client import RegularClient
from project.clients.vip_client import VIPClient
from project.waiters.base_waiter import BaseWaiter
from project.waiters.full_time_waiter import FullTimeWaiter
from project.waiters.half_time_waiter import HalfTimeWaiter


class SphereRestaurantApp:

    VALID_WAITER_TYPE = {
        "FullTimeWaiter": FullTimeWaiter,
        "HalfTimeWaiter": HalfTimeWaiter
    }

    VALID_CLIENT_TYPES = {
        "VIPClient": VIPClient,
        "RegularClient": RegularClient
    }

    def __init__(self):
        self.waiters: List[BaseWaiter] = []
        self.clients: List[BaseClient] = []

    def hire_waiter(self, waiter_type: str, waiter_name: str, hours_worked: int):
        try:
            waiter = self.VALID_WAITER_TYPE[waiter_type](waiter_name, hours_worked)
            next(filter(lambda x: x.name == waiter_name, self.waiters))
            return f"{waiter_name} is already on the staff."
        except KeyError:
            return f"{waiter_type} is not a recognized waiter type."
        except StopIteration:
            self.waiters.append(waiter)
            return f"{waiter_name} is successfully hired as a {waiter_type}."

    def admit_client(self, client_type: str, client_name: str):
        try:
            client = self.VALID_CLIENT_TYPES[client_type](client_name)
            next(filter(lambda x: x.name == client_name, self.clients))
            return f"{client_name} is already a client."
        except KeyError:
            return f"{client_type} is not a recognized client type."
        except StopIteration:
            self.clients.append(client)
            return f"{client_name} is successfully admitted as a {client_type}."

    def process_shifts(self, waiter_name: str):
        try:
            waiter = next(filter(lambda x: x.name == waiter_name, self.waiters))
            return waiter.report_shift()
        except StopIteration:
            return f"No waiter found with the name {waiter_name}."

    def process_client_order(self, client_name: str, order_amount: float):
        try:
            client = next(filter(lambda x: x.name == client_name, self.clients))
            return f"{client_name} earned {client.earning_points(order_amount)} points from the order."
        except StopIteration:
            return f"{client_name} is not a registered client."

    def apply_discount_to_client(self, client_name: str):
        try:
            client = next(filter(lambda x: x.name == client_name, self.clients))
            info = client.apply_discount()
            return f"{client_name} received a {info[0]}% discount. Remaining points {info[1]}"
        except StopIteration:
            return f"{client_name} cannot get a discount because this client is not admitted!"

    def generate_report(self):
        total_earnings = sum([waiter.calculate_earnings() for waiter in self.waiters])
        total_client_points = sum([client.points for client in self.clients])
        clients_count = len(self.clients)
        sorted_waiters = sorted(self.waiters, key=lambda x: -x.calculate_earnings())
        waiters_info = "\n".join([str(waiter) for waiter in sorted_waiters])
        return (f"$$ Monthly Report $$\n"
                f"Total Earnings: ${total_earnings:.2f}\n"
                f"Total Clients Unused Points: {total_client_points}\n"
                f"Total Clients Count: {clients_count}\n"
                f"** Waiter Details **\n" + waiters_info)
