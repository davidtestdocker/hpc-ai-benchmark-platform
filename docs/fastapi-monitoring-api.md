# 健康檢查 API（Health Check API）

Health Check 用於確認服務是否正常運作。

第一版實作：

```python
@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
```

此版本只能確認 API Service 是否存活。

---

# 強化版健康檢查（Enhanced Health Check）

隨著 Monitoring 功能增加，Health Check 不應只回傳固定字串，而應具備評估系統狀態的能力。

因此將健康檢查邏輯移至：

```python
SystemSnapshot.health_check()
```

由 Monitoring Service 負責執行健康狀態判斷。

---

# 健康檢查項目

目前 Health Check 會檢查：

* 磁碟使用率（Disk Usage）
* 系統負載（Load Average）
* 可用記憶體（Available Memory）

---

## 磁碟使用率（Disk Usage）

資料來源：

```python
self.get_disk_usage()
```

判斷條件：

```python
if disk_usage > 80:
```

若磁碟使用率超過 80%，系統標記為：

```text
warning
```

---

## 系統負載（Load Average）

資料來源：

```python
self.get_load_average()
```

判斷條件：

```python
if load_average > cpu_count * 2:
```

若 Load Average 超過 CPU Core 數量兩倍，系統標記為：

```text
warning
```

---

## 可用記憶體（Available Memory）

資料來源：

```python
self.get_mem_available_kb()
```

判斷條件：

```python
if mem_available < 1000000:
```

代表：

```text
可用記憶體低於 1 GB
```

系統標記為：

```text
warning
```

---

# get_mem_available_kb() 方法

新增：

```python
def get_mem_available_kb(self) -> int:
    with open("/proc/meminfo", "r") as file:
        for line in file:
            if line.startswith("MemAvailable:"):
                return int(line.split()[1])

    return 0
```

用途：

```text
取得可用記憶體數值
供健康檢查邏輯使用
```

與：

```python
get_mem_available()
```

差異如下：

| 方法                     | 用途     |
| ---------------------- | ------ |
| get_mem_available()    | 顯示監控資料 |
| get_mem_available_kb() | 健康狀態判斷 |

---

# 健康檢查回應格式

第一版：

```json
{
    "status": "healthy"
}
```

僅能確認 API 是否存活。

---

第二版：

```json
{
    "status": "healthy",
    "checks": {
        "disk": "ok",
        "load": "ok",
        "memory": "ok"
    }
}
```

已具備基礎健康檢查能力。

---

目前版本：

```json
{
    "status": "healthy",
    "checks": {
        "disk": {
            "status": "ok",
            "value": "7%"
        },
        "load": {
            "status": "ok",
            "value": "1.11"
        },
        "memory": {
            "status": "ok",
            "value": "14389584 kB"
        }
    }
}
```

除了健康狀態外，同時提供實際監控數值。

---

# 健康狀態判斷流程

目前流程：

```text
磁碟使用率
↓
系統負載
↓
可用記憶體
↓
健康狀態評估
↓
JSON 回應
```

---

# 健康狀態定義

## healthy

所有檢查皆正常：

```json
{
    "status": "healthy"
}
```

---

## degraded

任一檢查項目異常：

```json
{
    "status": "degraded"
}
```

例如：

```json
{
    "status": "degraded",
    "checks": {
        "disk": {
            "status": "warning",
            "value": "92%"
        },
        "load": {
            "status": "ok",
            "value": "1.00"
        },
        "memory": {
            "status": "ok",
            "value": "14389584 kB"
        }
    }
}
```

---

# 健康檢查測試

測試：

```bash
curl http://localhost:8000/health
```

實際結果：

```json
{
    "status": "healthy",
    "checks": {
        "disk": {
            "status": "ok",
            "value": "7%"
        },
        "load": {
            "status": "ok",
            "value": "1.11"
        },
        "memory": {
            "status": "ok",
            "value": "14389584 kB"
        }
    }
}
```

---

# 健康檢查的實際用途

常見應用情境：

* Kubernetes Liveness Probe
* Kubernetes Readiness Probe
* Load Balancer Health Check
* Monitoring System
* Container Platform

架構：

```text
Kubernetes
↓
呼叫 /health
↓
FastAPI
↓
SystemSnapshot
↓
健康狀態評估
↓
healthy
```

若服務異常：

```text
Kubernetes
↓
健康檢查失敗
↓
重新啟動 Pod
```

---

# 本週學習重點

本週學會：

* FastAPI
* Uvicorn
* REST API
* HTTP GET
* JSON Response
* Python Module
* Python Import
* Python Class Reuse
* 健康檢查設計（Health Check Design）
* Dictionary
* Dictionary Update
* int()
* float()
* split()
* Monitoring API 設計

---

# 專案架構演進

Week 3：

```text
SystemSnapshot
↓
JSON File
```

Week 4 初期：

```text
Client
↓
FastAPI
↓
SystemSnapshot
↓
JSON Response
```

Week 4 後期：

```text
Client
↓
HTTP Request
↓
FastAPI
↓
SystemSnapshot
↓
健康狀態判斷邏輯
↓
Linux Metrics
↓
JSON Response
```

---

# 結論

本專案已從單純的 Python Script 發展為具備 Monitoring API 與 Health Check 能力的 Monitoring Service。

目前已完成：

```http
GET /
GET /snapshot
GET /health
```

Health Check 已可檢查：

* 磁碟使用率門檻（Disk Usage Threshold）
* 系統負載門檻（Load Average Threshold）
* 可用記憶體門檻（Available Memory Threshold）

並提供：

* 健康狀態（Health Status）
* 詳細檢查結果（Detailed Check Result）
* 即時監控數值（Real-time Monitoring Values）

後續將持續擴充 Benchmark、Dashboard、Kubernetes 與 GitOps 功能。

