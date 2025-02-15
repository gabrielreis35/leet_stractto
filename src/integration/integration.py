from typing import List
import requests
import json

from models.requests.accounts import AccountsRequest
from models.requests.fields import FieldsRequest

class Integration():
    def __init__(self):
        self.url = "https://sidebar.stract.to/api"
        self.token = "ProcessoSeletivoStract2025"

    def get_platforms(self):
        uri = "/platforms"
        
        url_request = self.url + uri
        header = {"Authorization": f"Bearer {self.token}",
                  "Content-Type": "application/json"}
        
        data = requests.get(url=url_request, headers=header)
        
        platform = json.loads(data.content)
        
        return platform 
        
    def get_accounts(self, platform: str, page: int=1) -> AccountsRequest:
        uri = "/accounts"
        
        url_request = self.url + uri
        header = {"Authorization": f"Bearer {self.token}",
                  "Content-Type": "application/json"}
        parameters = {
            "platform": platform,
            "page": page
            }
        data = requests.get(url=url_request, headers=header, params=parameters)
        accounts = AccountsRequest.model_validate_json(data.content)
        
        return accounts
    
    def get_fields(self, platform: str, page:int=1) -> FieldsRequest:
        uri = "/fields"
        
        url_request = self.url + uri
        header = {"Authorization": f"Bearer {self.token}",
                  "Content-Type": "application/json"}
        parameters = {
            "platform": platform,
            "page": page
            }
        data = requests.get(url=url_request, headers=header, params=parameters)
        fields = FieldsRequest.model_validate_json(data.content)
        
        return fields
    
    def get_insights(self, platform: str, account: str, token: str, fields):
        uri = "/insights"
        
        url_request = self.url + uri
        header = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
            }
        parameters = {
            "platform": platform,
            "account": account,
            "token": token,
            "fields": fields
            }
        data = requests.get(url=url_request, headers=header, params=parameters)
        insights = json.loads(data.content)
        
        return insights
    