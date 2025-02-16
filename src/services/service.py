from integration.integration import Integration
from models.requests.accounts import Account
from models.requests.fields import Field
import json

requisition = Integration()

class Service:
    def __init__(self):
        pass
    
    def get_accounts(self, platform: str):
        all_accounts: list[Account] = []
        page = 1
        total_pages = 1
        
        while page <= total_pages:
            req_accounts = requisition.get_accounts(platform=platform, page=page)
            all_accounts.extend(req_accounts.accounts)
            
            total_pages = req_accounts.pagination.total if req_accounts.pagination else 1
            page += 1
        
        return all_accounts
    
    def get_fields(self, platform:str):
        all_fields: list[Field] = []
        str_fields = ""
        while page <= total_pages:
            req_fields = requisition.get_fields(platform=platform, page=page)
            all_fields.extend(req_fields.fields)
            
            total_pages = req_fields.pagination.total if req_fields.pagination else 1
            page += 1
            
            for field in req_fields.fields:
                str_fields += field.value + ","
        
        return all_fields, str_fields
            
    
    def get_report_platform(self, platform: str):
        str_fields = ""
        all_insights = {"insights": []}
        all_fields: list[Field]
        str_fields: str
        
        all_accounts: list[Account]= self.get_accounts(platform)
        all_fields, str_fields = self.get_fields(platform)
        
        for account in all_accounts:
            req_insights = requisition.get_insights(platform=platform, account=account.id, token=account.token, fields=str_fields)
            insight = req_insights["insights"][0]
            save_insight = {
                "Platform": platform,
                "Ad Name": insight.get("ad_name") if (platform == "meta_ads" or platform == "tiktok_insights") else insight.get("adName"),
            }
            
            for field in all_fields:
                if (field.value != "ad_name" and (platform == "meta_ads" or platform == "tiktok_insights")) or (field.value != "adName" and platform == "ga4"):
                    save_insight[field.value] = insight.get(field.value, "")
            
            all_insights["insights"].append(save_insight)
                    
        return all_insights
    
    def get_general_report(self, page: int, offset: int):
        
        ...