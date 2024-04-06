from project.campaigns.base_campaign import BaseCampaign


class HighBudgetCampaign(BaseCampaign):
    USED_IDS = []

    @property
    def type(self):
        return "HighBudgetCampaign"

    __BUDGET = 5000

    def __init__(self, campaign_id: int, brand: str, required_engagement: float):
        super().__init__(campaign_id, brand, self.__BUDGET, required_engagement)

    def check_eligibility(self, engagement_rate: float):
        if self.required_engagement * 1.2 <= engagement_rate:
            return True
        return False
