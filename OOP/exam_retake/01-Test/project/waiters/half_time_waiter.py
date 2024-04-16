from project.waiters.base_waiter import BaseWaiter


class HalfTimeWaiter(BaseWaiter):
    def calculate_earnings(self):
        return 12.0 * self.hours_worked

    def report_shift(self):
        return f"{self.name} worked a half-time shift of {self.hours_worked} hours."