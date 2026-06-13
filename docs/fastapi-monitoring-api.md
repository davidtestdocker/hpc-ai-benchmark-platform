# FastAPI Monitoring API 學習筆記

## 學習目標

本章節目標：

* 了解什麼是 API
* 了解 REST API 基礎概念
* 學習 FastAPI 開發
* 學習 Uvicorn Server
* 學習 Python Module Import
* 將 Python Monitoring Tool 整合為 API Service

---

# 什麼是 API

API（Application Programming Interface）是一種讓程式彼此溝通的介面。

傳統程式：

```text
使用者
↓
Terminal
↓
Python Script
```

例如：

```bash
python3 monitoring/python/system_snapshot.py
```

結果直接輸出到檔案：

```json
{
    "hostname": "manual-vm"
}
```

---

API 模式：

```text
Client
↓
HTTP Request
↓
API Server
↓
JSON Response
```

例如：

```bash
curl http://localhost:8000/snapshot
```

取得：

```json
{
    "hostname": "manual-vm"
}
```

---

# REST API

REST（Representational State Transfer）是一種常見 API 設計風格。

本專案使用：

```http
GET
```

方法取得資料。

範例：

```http
GET /
GET /snapshot
```

---

# FastAPI

FastAPI 是 Python Web Framework。

特色：

* 開發速度快
* 效能高
* 自動產生 API 文件
* 支援 Type Hint

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

建立：

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

# FastAPI 基本語法

## 建立 Application

```python
app = FastAPI()
```

建立 FastAPI 應用程式物件。

---

## Route

```python
@app.get("/")
```

代表：

```text
HTTP GET /
```

當使用者存取：

http://localhost:8000/

就會執行：

```python
root()
```

---

## Response

```python
return {
    "message": "Hello"
}
```

FastAPI 會自動轉換成：

```json
{
    "message": "Hello"
}
```

---

# Uvicorn

Uvicorn 為 FastAPI 的 ASGI Server。

啟動：

```bash
uvicorn api.main:app --host 0.0.0.0 --port 8000
```

---

# 指令拆解

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

允許所有網路介面連線。

---

## --port 8000

監聽：

```text
TCP 8000
```

---

# curl 測試

測試 API：

```bash
curl http://localhost:8000/
```

結果：

```json
{
    "message": "HPC AI Benchmark Platform"
}
```

---

# Python Module Import

本專案將 Monitoring Collector 與 API 分離。

目錄：

```text
monitoring/python/system_snapshot.py

api/main.py
```

透過：

```python
from monitoring.python.system_snapshot import SystemSnapshot
```

匯入 Class。

---

# SystemSnapshot 整合

原本：

```text
Python Script
↓
輸出 JSON 檔案
```

改為：

```text
FastAPI
↓
呼叫 SystemSnapshot
↓
回傳 JSON
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

# 建立 Monitoring API

新增：

```python
@app.get("/snapshot")
def get_snapshot():
    snapshot = SystemSnapshot()

    return snapshot.generate_snapshot()
```

---

# API 測試

測試：

```bash
curl http://localhost:8000/snapshot
```

結果：

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

# 本週學習重點

學會：

* FastAPI
* Uvicorn
* REST API
* HTTP GET
* JSON Response
* Python Module
* Python Import
* Python Class Reuse
* Monitoring API 設計

理解：

```text
Script
↓
Tool
↓
Service
```

的差異。

本專案正式從 Python Script 進化為 Monitoring API Service。

