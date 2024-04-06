from project.influencers.base_influencer import BaseInfluencer


class StandardInfluencer(BaseInfluencer):
    @property
    def type(self):
        return "StandardInfluencer"

    @property
    def payment_percentage(self):
        return 0.45

    def reached_followers(self, campaign_type: str):
        multiplier = 0
        if campaign_type == "HighBudgetCampaign":
            multiplier = 1.2
        elif campaign_type == "LowBudgetCampaign":
            multiplier = 0.9

        return int(self.followers * self.engagement_rate * multiplier)

