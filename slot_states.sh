export SLOT=10000160
curl -H "Accept: application/octet-stream" "https://api.chainup.net/ethereum2-archive/mainnet/dc59a7e90f05424a81d825d033d0f2de/eth/v2/debug/beacon/states/$SLOT" > state.ssz
curl -H "Accept: application/octet-stream" "https://api.chainup.net/ethereum2-archive/mainnet/dc59a7e90f05424a81d825d033d0f2de/eth/v2/beacon/blocks/$SLOT" > block.ssz
curl -H "Accept: application/octet-stream" "https://api.chainup.net/ethereum2-archive/mainnet/dc59a7e90f05424a81d825d033d0f2de/eth/v1/beacon/blob_sidecars/$SLOT" > blobs.ssz
