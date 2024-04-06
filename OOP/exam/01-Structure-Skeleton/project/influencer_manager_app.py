from typing import List

from project.campaigns.base_campaign import BaseCampaign
from project.campaigns.high_budget_campaign import HighBudgetCampaign
from project.campaigns.low_budget_campaign import LowBudgetCampaign
from project.influencers.base_influencer import BaseInfluencer
from project.influencers.premium_influencer import PremiumInfluencer
from project.influencers.standard_influencer import StandardInfluencer


class InfluencerManagerApp:
    __VALID_INFLUENCER_TYPES = {
        "PremiumInfluencer": PremiumInfluencer,
        "StandardInfluencer": StandardInfluencer,
    }

    __VALID_CAMPAIGN_TYPES = {
        "HighBudgetCampaign": HighBudgetCampaign,
        "LowBudgetCampaign": LowBudgetCampaign,
    }

    def __init__(self):
        self.influencers: List[BaseInfluencer] = []
        self.campaigns: List[BaseCampaign] = []

    def register_influencer(self, influencer_type: str, username: str, followers: int, engagement_rate: float):
        try:
            influencer = self.__VALID_INFLUENCER_TYPES[influencer_type](username, followers, engagement_rate)
            next(filter(lambda x: x.username == username, self.influencers))
        except KeyError:
            return f"{influencer_type} is not an allowed influencer type."
        except StopIteration:
            self.influencers.append(influencer)
            return f"{username} is successfully registered as a {influencer_type}."

        return f"{username} is already registered."

    def create_campaign(self, campaign_type: str, campaign_id: int, brand: str, required_engagement: float):
        try:
            campaign = self.__VALID_CAMPAIGN_TYPES[campaign_type](campaign_id, brand, required_engagement)
            next(filter(lambda x: x.campaign_id == campaign_id, self.campaigns))
        except KeyError:
            return f"{campaign_type} is not a valid campaign type."
        except StopIteration:
            self.campaigns.append(campaign)
            return f"Campaign ID {campaign_id} for {brand} is successfully created as a {campaign_type}."
        except ValueError:
            return f"Campaign ID {campaign_id} has already been created."

    def participate_in_campaign(self, influencer_username: str, campaign_id: int):
        try:
            influencer = next(filter(lambda x: x.username == influencer_username, self.influencers))
        except StopIteration:
            return f"Influencer '{influencer_username}' not found."

        try:
            campaign = next(filter(lambda x: x.campaign_id == campaign_id, self.campaigns))
        except StopIteration:
            return f"Campaign with ID {campaign_id} not found."

        if not campaign.check_eligibility(influencer.engagement_rate):
            return f"Influencer '{influencer_username}' does not meet the eligibility criteria for the campaign with ID {campaign_id}."

        payment = influencer.calculate_payment(campaign)
        if payment > 0:
            campaign.approved_influencers.append(influencer)
            campaign.budget -= payment
            influencer.campaigns_participated.append(campaign)
            return f"Influencer '{influencer_username}' has successfully participated in the campaign with ID {campaign_id}."

    def calculate_total_reached_followers(self):
        result = {}
        for campaign in self.campaigns:
            cur_campaign_followers = 0
            for influencer in campaign.approved_influencers:
                cur_campaign_followers += influencer.reached_followers(campaign.type)

            if cur_campaign_followers > 0:
                result[campaign] = cur_campaign_followers
        return result

    def influencer_campaign_report(self, username: str):
        influencer = next(filter(lambda x: x.username == username, self.influencers))
        if not influencer.campaigns_participated:
            return f"{username} has not participated in any campaigns."

        return influencer.display_campaigns_participated()

    def campaign_statistics(self):
        campaign_followers_dict = self.calculate_total_reached_followers()
        sorted_campaigns = sorted(self.campaigns, key=lambda x: (len(x.approved_influencers), -x.budget))
        campaigns_info = [
            f"  * Brand: {c.brand}, Total influencers: {len(c.approved_influencers)}, Total budget: ${c.budget:.2f}, Total reached followers: {campaign_followers_dict[c]}"
            for c in sorted_campaigns]
        return f"$$ Campaign Statistics $$\n{'\n'.join(campaigns_info)}"
