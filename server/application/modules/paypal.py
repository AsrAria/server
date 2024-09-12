# -*- coding: utf-8 -*-

# python imports
import requests


class PayPalClient:

    # mark: initialize

    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        self.config = app.config['PAY_PAL_CONFIG']
        self.app = app

    # mark: functions

    def execute_payment(self, payment_id, payer_id):
        try:
            self.update_access_token()

            json = {
                'payer_id': payer_id
            }

            response = requests.post(
                self.config['urls']['execute'] % payment_id,
                headers=self.get_authenticated_request_headers(),
                json=json
            )

            if response.status_code == 200:
                json = response.json()
                if json['state'] == 'approved':
                    return True
        except Exception:
            pass
        return False

    def create_payment(self, name, description, price, tracking_id, return_url, cancel_url):
        try:
            self.update_access_token()

            price = str(price / 100.0)

            json = {
                "intent": "sale",
                "payer": {
                    "payment_method": "paypal"
                },
                "transactions": [{
                    "amount": {
                        "total": price,
                        "currency": "USD",
                        "details": {
                            "subtotal": price
                        }
                    },
                    "description": description,
                    "invoice_number": tracking_id,
                    "payment_options": {
                        "allowed_payment_method": "INSTANT_FUNDING_SOURCE"
                    },
                    "item_list": {
                        "items": [
                            {
                                "name": name,
                                "description": description,
                                "quantity": "1",
                                "price": price,
                                "currency": "USD"
                            }
                        ]
                    }
                }],
                "note_to_payer": "Contact us for any questions on your order.",
                "redirect_urls": {
                    "return_url": return_url,
                    "cancel_url": cancel_url
                }
            }

            response = requests.post(
                self.config['urls']['payment'],
                headers=self.get_authenticated_request_headers(),
                json=json
            )

            if response.status_code == 201:
                json = response.json()
                approval_url = ""
                for item in json['links']:
                    if item['rel'] == 'approval_url':
                        approval_url = item['href']
                return {
                    'url': approval_url,
                    'payment_id': json['id'],
                }
        except Exception:
            pass
        return None

    def update_access_token(self):
        headers = {
            'Accept': 'application/json',
            'Accept-Language': 'en_US',
        }

        data = {
            'grant_type': 'client_credentials'
        }

        response = requests.post(
            self.config['urls']['oauth'],
            headers=headers,
            data=data,
            auth=(self.config['client_id'], self.config['secret'])
        )

        if response.status_code == 200:
            json = response.json()
            self.app_id = json['app_id']
            self.token_type = json['token_type']
            self.access_token = json['access_token']
            return True
        return False

    def get_access_token(self):
        return self.token_type + ' ' + self.access_token

    def get_authenticated_request_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': self.get_access_token(),
        }
