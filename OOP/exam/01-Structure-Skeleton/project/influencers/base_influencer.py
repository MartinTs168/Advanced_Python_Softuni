from abc import ABC, abstractmethod

from project.campaigns.base_campaign import BaseCampaign


class BaseInfluencer(ABC):
    def __init__(self, username: str, followers: int, engagement_rate: float):
        self.username = username
        self.followers = followers
        self.engagement_rate = engagement_rate
        self.campaigns_participated = []

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if value.strip() == '':
            raise ValueError("Username cannot be empty or consist only of whitespace!")
        self.__username = value

    @property
    def followers(self):
        return self.__followers

    @followers.setter
    def followers(self, value):
        if value < 0:
            raise ValueError("Followers must be a non-negative integer!")
        self.__followers = value

    @property
    def engagement_rate(self):
        return self.__engagement_rate

    @engagement_rate.setter
    def engagement_rate(self, value):
        if not 0.0 <= value <= 5.0:
            raise ValueError("Engagement rate should be between 0 and 5.")

        self.__engagement_rate = value

    @property
    @abstractmethod
    def type(self):
        ...

    @property
    @abstractmethod
    def payment_percentage(self):
        ...

    @abstractmethod
    def reached_followers(self, campaign_type: str):
        ...

    def calculate_payment(self, campaign: BaseCampaign):
        return campaign.budget * self.payment_percentage

    def display_campaigns_participated(self):
        if not self.campaigns_participated:
            return f"{self.username} has not participated in any campaigns."
        campaigns_info = [f"  - Campaign ID: {c.campaign_id}, Brand: {c.brand}, Reached followers: {self.reached_followers(c.type)}"
                          for c in self.campaigns_participated]
        return f"{self.type} :) {self.username} :) participated in the following campaigns:\n{'\n'.join(campaigns_info)}"