#!/usr/bin/env bash
curl -H "Content-Type: application/json" -X POST -d @subscription_webhook.json http://localhost:8000/subscriptions_webhook
