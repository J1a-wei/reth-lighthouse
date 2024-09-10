#!/bin/bash
curl localhost:8545 -H 'Content-Type: application/json' -d '{"jsonrpc":"2.0","method":"eth_syncing","params":[],"id":1}'

curl localhost:8080/eth/v1/node/syncing -H 'Content-Type: application/json' 