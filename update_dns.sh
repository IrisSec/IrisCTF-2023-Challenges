#!/bin/sh
# Script to update a google cloud dns A record to the current ip adress.
# Depends on gcloud being installed and configured (https://cloud.google.com/sdk/docs/quickstarts).
# Relevant gcloud documentation: https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/transaction
set -e

# CONFIG
PROJECT=irisctf
DNS_ZONE=kctf-chal--irisc--tf 
DNS_RECORD=router.chal.irisc.tf

GDNS="gcloud dns --project=$PROJECT record-sets transaction"

echo "Project: $PROJECT\nDNS Zone: $DNS_ZONE\nDNS Record: $DNS_RECORD\n"

CURRENT_IP=$(dig -4 A +short router.chal.irisc.tf | tr -d \")
IP=$(kubectl get services --namespace ingress-nginx ingress-nginx-controller --output jsonpath='{.status.loadBalancer.ingress[0].ip}')

if [ "$IP" ]; then 
  if [ "$CURRENT_IP" != "$IP" ]; then 
    echo "Updating $DNS_ZONE from $CURRENT_IP to $IP"

    $GDNS start --zone $DNS_ZONE
    $GDNS remove --name "$DNS_RECORD." --type=A --ttl=300 --zone $DNS_ZONE $CURRENT_IP
    $GDNS add --name "$DNS_RECORD." --type=A --ttl=300 --zone $DNS_ZONE $IP
    $GDNS execute --zone $DNS_ZONE
  else 
    echo "DNS entry already up to date"
  fi 
else 
  echo "Failed to fetch current IP"
fi

# credit
# https://gist.githubusercontent.com/P4sca1/17729013eb08fcc1671693181af72c05/raw/7b039c77e7d95b63c3d86e257e9da5733a63db48/gcloud-ddns.sh


