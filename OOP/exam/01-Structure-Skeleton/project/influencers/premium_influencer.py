from project.influencers.base_influencer import BaseInfluencer


class PremiumInfluencer(BaseInfluencer):
    @property
    def type(self):
        return "PremiumInfluencer"

    @property
    def payment_percentage(self):
        return 0.85

    def reached_followers(self, campaign_type: str):
        multiplier = 0
        if campaign_type == "HighBudgetCampaign":
            multiplier = 1.5
        elif campaign_type == "LowBudgetCampaign":
            multiplier = 0.8

        return int(self.followers * self.engagement_rate * multiplier)

