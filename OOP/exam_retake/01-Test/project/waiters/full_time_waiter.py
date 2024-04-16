from project.waiters.base_waiter import BaseWaiter


class FullTimeWaiter(BaseWaiter):
    def calculate_earnings(self):
        return 15.0 * self.hours_worked

    def report_shift(self):
        return f"{self.name} worked a full-time shift of {self.hours_worked} hours."