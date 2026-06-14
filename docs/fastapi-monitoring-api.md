# Health Check API

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

# Enhanced Health Check

隨著 Monitoring 功能增加，Health Check 需要能夠評估系統狀態，而不只是回傳固定字串。

因此將 Health Check 邏輯移至：

```python
SystemSnapshot.health_check()
```

由 Monitoring Service 負責判斷系統健康狀態。

---

# 檢查項目

目前 Health Check 檢查：

## Disk Usage

來源：

```python
self.get_disk_usage()
```

判斷條件：

```python
if disk_usage > 80:
```

狀態：

```text
warning
```

---

## Load Average

來源：

```python
self.get_load_average()
```

判斷條件：

```python
if load_average > cpu_count * 2:
```

狀態：

```text
warning
```

---

## Available Memory

來源：

```python
self.get_mem_available_kb()
```

判斷條件：

```python
if mem_available < 1000000:
```

約等於：

```text
Available Memory < 1GB
```

狀態：

```text
warning
```

---

# get_mem_available_kb()

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
供 Health Check 判斷使用
```

與：

```python
get_mem_available()
```

的差異：

| Method                 | 用途   |
| ---------------------- | ---- |
| get_mem_available()    | 顯示資料 |
| get_mem_available_kb() | 邏輯判斷 |

---

# Health Check Response

目前回傳：

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

若其中一項異常：

```json
{
    "status": "degraded",
    "checks": {
        "disk": "warning",
        "load": "ok",
        "memory": "ok"
    }
}
```

---

# Health Check 測試

測試：

```bash
curl http://localhost:8000/health
```

結果：

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

---

# Health Check 的用途

實務上常用於：

* Kubernetes Liveness Probe
* Kubernetes Readiness Probe
* Load Balancer Health Check
* Monitoring System
* Container Platform

架構：

```text
Kubernetes
↓
GET /health
↓
FastAPI
↓
SystemSnapshot
↓
Health Evaluation
↓
healthy
```

若服務異常：

```text
Kubernetes
↓
偵測失敗
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
* Health Check Design
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
Health Check Logic
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

* Disk Usage
* Load Average
* Available Memory

後續將持續擴充 Benchmark、Dashboard、Kubernetes 與 GitOps 功能。

