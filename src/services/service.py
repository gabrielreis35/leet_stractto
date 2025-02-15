from integration.integration import Integration
from models.requests.accounts import Account
from models.requests.fields import Field
import json

requisition = Integration()

class Service:
    def __init__(self):
        pass
    
    def get_platform(self, platform: str):
        total_pages = 1
        page = 1
        str_fields = ""
        all_accounts: list[Account] = []
        all_fields: list[Field] = []
        all_insights = {"insights": []}
        
        while page <= total_pages:
            req_accounts = requisition.get_accounts(platform=platform, page=page)
            all_accounts.extend(req_accounts.accounts)
            
            total_pages = req_accounts.pagination.total
            page += 1
        
        page = 1
        while page <= total_pages:
            req_fields = requisition.get_fields(platform=platform, page=page)
            all_fields.extend(req_fields.fields)
            
            total_pages = req_fields.pagination.total
            page += 1
            
            for field in req_fields.fields:
                str_fields += field.value + ","
        
        for account in all_accounts:
            req_insights = requisition.get_insights(platform=platform, account=account.id, token=account.token, fields=str_fields)
            insight = req_insights["insights"][0]
            save_insight = {
                "Platform": platform,
                "Ad Name": insight.get("ad_name"),
            }
            
            for field in all_fields:
                if field.value != "ad_name":
                    save_insight[field.value] = insight.get(field.value, "")
            
            all_insights["insights"].append(save_insight)
                    
        return all_insights