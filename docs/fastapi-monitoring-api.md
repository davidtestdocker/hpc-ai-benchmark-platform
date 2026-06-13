# FastAPI Monitoring API

## 學習目標

本階段目標：

* 學習 REST API 基礎概念
* 學習 FastAPI 開發
* 學習 Uvicorn Server
* 學習 Python Module Import
* 將 Monitoring Collector 整合為 API Service
* 建立 Health Check Endpoint

---

# 什麼是 API

API（Application Programming Interface）是一種讓程式之間交換資料的介面。

傳統 Python Script：

```text
使用者
↓
Terminal
↓
Python Script
↓
輸出結果
```

例如：

```bash
python3 monitoring/python/system_snapshot.py
```

---

API Service：

```text
Client
↓
HTTP Request
↓
FastAPI
↓
Python Logic
↓
JSON Response
```

例如：

```bash
curl http://localhost:8000/snapshot
```

---

# REST API

本專案使用 REST API 設計。

目前使用：

```http
GET
```

取得資料。

已實作：

```http
GET /
GET /snapshot
GET /health
```

---

# FastAPI

FastAPI 是 Python Web Framework。

特色：

* 高效能
* 開發快速
* 支援 Type Hint
* 自動產生 API 文件
* 適合 Microservice

安裝：

```bash
pip3 install fastapi uvicorn
```

驗證：

```bash
pip3 show fastapi
```

---

# 建立第一個 API

檔案：

```text
api/main.py
```

內容：

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {
        "message": "HPC AI Benchmark Platform"
    }
```

---

# FastAPI Route

範例：

```python
@app.get("/")
```

代表：

```http
GET /
```

當 Client 存取：

```text
http://localhost:8000/
```

FastAPI 會執行：

```python
root()
```

並回傳結果。

---

# JSON Response

Python：

```python
return {
    "message": "hello"
}
```

FastAPI：

```json
{
    "message": "hello"
}
```

自動轉換為 JSON。

---

# Uvicorn

Uvicorn 為 FastAPI 的 ASGI Server。

啟動方式：

```bash
uvicorn api.main:app --host 0.0.0.0 --port 8000
```

---

# 指令解析

## api.main

代表：

```text
api/main.py
```

---

## app

代表：

```python
app = FastAPI()
```

---

## --host 0.0.0.0

允許所有網路介面存取。

---

## --port 8000

監聽：

```text
TCP 8000
```

---

# Python Import

專案結構：

```text
api/main.py

monitoring/python/system_snapshot.py
```

透過：

```python
from monitoring.python.system_snapshot import SystemSnapshot
```

載入 Class。

---

# SystemSnapshot 整合

原本：

```text
Python Script
↓
產生 JSON
```

現在：

```text
Client
↓
FastAPI
↓
SystemSnapshot
↓
JSON Response
```

---

# generate_snapshot()

建立共用方法：

```python
def generate_snapshot(self) -> dict:
```

用途：

```text
集中管理所有監控資料收集邏輯
```

回傳：

```python
{
    "hostname": "...",
    "cpu_count": 4
}
```

---

# Snapshot API

實作：

```python
@app.get("/snapshot")
def get_snapshot():
    snapshot = SystemSnapshot()

    return snapshot.generate_snapshot()
```

---

# Snapshot API 測試

測試：

```bash
curl http://localhost:8000/snapshot
```

範例輸出：

```json
{
    "time": "2026-06-13 11:08:46.203933+00:00",
    "hostname": "manual-vm",
    "memory_available": "14306020 kB",
    "load_average": "1.03, 1.05, 1.01",
    "disk_usage": "7%",
    "disk_status": "OK",
    "cpu_count": 4
}
```

---

# Health Check API

Health Check 用於確認服務是否正常運作。

實作：

```python
@app.get("/health")
def health():
    return {
        "status": "healthy"
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
    "status": "healthy"
}
```

---

# Health Check 的用途

實務上常用於：

* Kubernetes Liveness Probe
* Kubernetes Readiness Probe
* Load Balancer Health Check
* Monitoring System

架構：

```text
Kubernetes
↓
GET /health
↓
API Service
↓
healthy
```

若服務異常：

```text
Kubernetes
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
* Health Check Endpoint
* Monitoring API 設計

---

# 專案架構演進

Week 3：

```text
SystemSnapshot
↓
JSON File
```

Week 4：

```text
Client
↓
HTTP Request
↓
FastAPI
↓
SystemSnapshot
↓
Linux Metrics
↓
JSON Response
```

---

# 結論

本專案已從單純的 Python Script 發展為可透過 HTTP 存取的 Monitoring API Service。

目前已完成：

```http
GET /
GET /snapshot
GET /health
```

後續將持續擴充 Benchmark、Dashboard、Kubernetes 與 GitOps 功能。

