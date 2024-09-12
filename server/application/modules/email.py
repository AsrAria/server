# -*- coding: utf-8 -*-

# python imports
import requests


class EmailClient:

    # mark: initialize

    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        self.config = app.config['EMAIL_SETTINGS']
        self.on = app.config.get('EMAIL_ON', True)
        self.app = app

    # mark: functions

    def send(self, email, name, subject, content, check_limit=True):
        if not self.on:
            return False

        if check_limit and not self.check_limit(email):
            return False

        body = {
            "personalizations": [
                {
                    "to": [
                        {
                            "email": email,
                            "name": name
                        }
                    ],
                    "subject": subject
                }
            ],
            "content": [
                {
                    "type": "text/plain",
                    "value": content
                }
            ],
            "from": {
                "email": self.config['sender_address'],
                "name": self.config['sender_name']
            }
        }

        headers = {
            'authorization': self.config['api_key']
        }

        try:
            response = requests.post(
                self.config['address'],
                json=body,
                headers=headers,
                timeout=self.config['timeout']
            )
            return response.status_code == 202
        except Exception:
            pass
        return False

    def check_limit(self, email):
        from application.extensions import redis
        key = 'ecl:%s' % email
        value = 1
        if redis.exists(key):
            value = int(redis.get(key).decode()) + 1
        if value > self.config['limit']:
            return False
        redis.set(key, str(value))
        return True
