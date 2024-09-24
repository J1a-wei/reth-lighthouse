import requests
import json
import time

# 定义请求的URL
base_url = 'http://localhost:8080'
headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
}

# 定义100个验证者ID
validator_ids = [str(i) for i in range(1217756, 1217856)]

# 获取最新的信标链高度（epoch）
def get_current_epoch():
    # 模拟请求信标链的最新高度，这里假设请求返回当前高度为313100
    epoch_url = f'{base_url}/eth/v1/beacon/states/head/finality_checkpoints'
    response = requests.get(epoch_url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        finalized_epoch = data['data']['finalized']['epoch']
        return int(finalized_epoch)
    else:
        print(f"Error fetching chainhead: {response.status_code}, {response.text}")
        return 313100  # 返回默认值

# 获取奖励信息
def fetch_rewards(validator_ids, epoch):
    payload = json.dumps(validator_ids)

    # 获取验证奖励的URL
    attestation_rewards_url = f'{base_url}/eth/v1/beacon/rewards/attestations/{epoch}'

    # 记录开始时间
    start_time = time.time()

    response = requests.post(attestation_rewards_url, headers=headers, data=payload)

    # 记录结束时间
    end_time = time.time()
    elapsed_time = end_time - start_time

    if response.status_code == 200:
        print(f"Success: Fetched rewards for epoch {epoch}")
        print("Response data:", response.json())  # 输出请求返回的数据
        return elapsed_time
    else:
        print(f"Error {response.status_code}: {response.text} for epoch {epoch}")
        return elapsed_time

# 依次减少epoch进行请求
def get_rewards_for_epochs(validator_ids, start_epoch, n):
    elapsed_times = []

    for i in range(n):
        current_epoch = start_epoch - i * 1  # 每次减少10个epoch
        print(f"Fetching rewards for epoch {current_epoch}...")

        # 请求奖励信息，并记录耗时
        elapsed_time = fetch_rewards(validator_ids, current_epoch)
        elapsed_times.append((current_epoch, elapsed_time))

    return elapsed_times

# 示例：获取验证者的奖励信息，按指定epoch减少并输出耗时
def main():
    # 获取最新的epoch高度
    current_epoch = get_current_epoch()
    print(f"Current epoch: {current_epoch}")

    # 请求3次，每次减少10个epoch
    n = 25
    elapsed_times = get_rewards_for_epochs(validator_ids, current_epoch, n)

    # 输出每次请求的耗时
    print("\nRequest times:")
    for epoch, elapsed_time in elapsed_times:
        print(f"Epoch {epoch}: {elapsed_time:.2f} seconds")

if __name__ == '__main__':
    main()
