#!/bin/bash 
echo "beacon inbound peer"
curl "localhost:8080/eth/v1/node/peers?state=connected&direction=inbound" -H 'Content-Type: application/json' | jq '.data[] | select(.last_seen_p2p_address  | startswith("/ip4/172.1.")| not)' 

echo "excution inbound peer"
curl localhost:8545 -H 'Content-Type: application/json' -d '{"jsonrpc":"2.0","method":"admin_peers","params":[],"id":1}' |jq '.result[] | select(.network.inbound == true) |  select(.network.remoteAddress | startswith("172.1.")| not)'