# Monad 测试网自动化工具

该工具用于自动化与 Monad 测试网的交互，支持多种 DeFi 操作和代币交互。  
**教程文档**：<https://star-labs.gitbook.io/star-labs/monad-ru>

## 🚀 功能特性

- 💎 MagicEden NFT平台操作
- 💱 代币兑换交易
- 🏦 在 Apriori/Magma/Kintsu/Shmonad/Bima 质押 MON
- 📄 铸造 NFT：accountable/lilchogstars/demask/monadking/monadking_unlocked
- 🦉 在 Owlto 上部署智能合约
- 🌋 使用 Gaszip 服务
- 🌐 Orbiter 跨链桥
- 📄 交易日志记录
- 📄 Nad 域名服务
- And much more...

## 📖 功能详解
- 使用 Monad 官方测试网水龙头获取测试代币
- 在支持的代币之间进行随机兑换 兑换金额范围：`PERCENT_OF_BALANCE_TO_SWAP` 参数配置
- 质押操作支持自定义金额 
- 智能处理 Gas 费用计算

## 🛠️ 环境要求
- Python 3.11+ 版本
- 推荐使用虚拟环境（venv）

## 📥 安装指南

### 安装仓库

git clone https://github.com/0xStarLabs/StarLabs-Monad.git

cd StarLabs-Monad

### 安装依赖
pip install -r requirements.txt

## ⚙️ 配置文件 (config.yaml)

```yaml
SETTINGS:
  # 并发线程数（建议不超过5）
  THREADS: 1
  # 失败重试次数
  ATTEMPTS: 5  
  # 操作间隔配置（单位：秒）
  PAUSE_BETWEEN_ATTEMPTS: [5, 15]
  # 账户间随机间隔（单位：秒）
  RANDOM_PAUSE_BETWEEN_ACCOUNTS: [3, 10]
  # 账户间随机间隔（单位：秒）
  RANDOM_PAUSE_BETWEEN_ACTIONS: [2, 5]

FLOW:
  # 可用任务列表:
  # "connect_discord" - 绑定 Discord 账户
  # "swaps" - 代币兑换
  # "apriori" - Apriori 质押
  # "magma" - Magma 质押
  # "owlto" - Owlto 合约部署
  # "bima" - Bima 借贷操作
  # 可用任务列表
  TASKS: ["connect_discord", "swaps", "apriori", "magma", "owlto", "bima"]
  # 兑换次数配置 [最小值, 最大值]
  NUMBER_OF_SWAPS: [1, 3]
  # 兑换金额百分比 [最小%, 最大%]
  PERCENT_OF_BALANCE_TO_SWAP: [10, 15]
  ```  
## 🔑 数据文件配置
### data/private_keys.txt
```
0x私钥1...

0x私钥2...

每行一个私钥
```
### data/proxies.txt
```
user:pass@ip:port

user:pass@ip:port

每行一个代理
```
## ▶️ 运行程序
python main.py

## ⚠️ 注意事项
* 代理配置

  * 国内用户必须使用代理访问测试网

  * 推荐使用住宅代理（Residential Proxy）

* 账户安全

  * private_keys.txt 文件必须加密存储

  * 建议使用测试专用账户

* 操作频率

  * 推荐配置间隔时间：RANDOM_PAUSE_BETWEEN_ACCOUNTS: [30, 120]

  * 单账户每日操作不超过20次

* Gas 费用
```yaml
# 建议 Gas 配置（单位：gwei）
GAS_CONFIG:
  MAX_FEE: 25
  PRIORITY_FEE: 2
```

## 🌐 加入社区

**Telegram	@keepCalm88**

**微信公众号	lszgege77**