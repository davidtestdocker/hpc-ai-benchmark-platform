# FastAPI Response Model

## 學習目標

本階段目標：

* 學習 Pydantic
* 學習 BaseModel
* 學習 Response Model
* 學習 OpenAPI Schema
* 學習 Swagger UI 與 Schema 整合
* 建立標準化 API Response

---

# 為什麼需要 Response Model

目前 Health API：

```python
@app.get("/health")
def health():
    return snapshot.health_check()
```

回傳：

```json
{
    "status": "healthy",
    "checks": {
        "disk": {
            "status": "ok",
            "value": "7%"
        }
    }
}
```

雖然可以正常運作。

但 FastAPI 不知道：

```text
status 是什麼型別？
checks 裡有哪些欄位？
哪些欄位是必填？
```

因此需要建立 Response Model。

---

# Pydantic

FastAPI 底層使用：

```text
Pydantic
```

進行：

* 資料驗證（Validation）
* 型別檢查（Type Checking）
* API Schema 產生
* OpenAPI 文件生成

---

# BaseModel

Pydantic 的核心類別：

```python
from pydantic import BaseModel
```

建立資料模型：

```python
class User(BaseModel):
    name: str
    age: int
```

---

# 建立 Health Response Model

檔案：

```text
api/models/health.py
```

---

## CheckItem

定義單一檢查項目：

```python
from pydantic import BaseModel


class CheckItem(BaseModel):
    status: str
    value: str
```

代表：

```json
{
    "status": "ok",
    "value": "7%"
}
```

---

## HealthResponse

定義整體 API Response：

```python
class HealthResponse(BaseModel):
    status: str
    checks: dict[str, CheckItem]
```

代表：

```json
{
    "status": "healthy",
    "checks": {
        "disk": {
            "status": "ok",
            "value": "7%"
        }
    }
}
```

---

# 專案結構

建立：

```text
api
├── main.py
└── models
    ├── __init__.py
    └── health.py
```

---

# **init**.py 的用途

用途：

```text
將資料夾標記為 Python Package
```

使 Python 能夠：

```python
from api.models.health import HealthResponse
```

正常載入模組。

---

# Response Model 綁定

在：

```text
api/main.py
```

匯入：

```python
from api.models.health import HealthResponse
```

---

修改：

```python
@app.get("/health")
```

為：

```python
@app.get(
    "/health",
    tags=["Monitoring"],
    response_model=HealthResponse
)
```

---

# Response Model 的作用

FastAPI 會知道：

```text
Health API 回傳格式
```

而不是：

```text
任意 Dictionary
```

---

# OpenAPI Schema

FastAPI 啟動後：

```text
Code
↓
Pydantic Model
↓
OpenAPI Schema
↓
Swagger UI
```

自動產生 API 文件。

---

# OpenAPI

網址：

```text
http://localhost:8000/openapi.json
```

查詢：

```bash
curl http://localhost:8000/openapi.json
```

---

產生：

```json
{
    "components": {
        "schemas": {
            "CheckItem": {},
            "HealthResponse": {}
        }
    }
}
```

---

# Swagger UI

網址：

```text
http://localhost:8000/docs
```

FastAPI 內建。

無需額外安裝 Swagger。

---

# ReDoc

FastAPI 同時提供：

```text
http://localhost:8000/redoc
```

用途：

```text
API 文件展示
```

---

# FastAPI Metadata

設定：

```python
app = FastAPI(
    title="HPC AI Benchmark Platform",
    description="Linux Monitoring and Benchmark API",
    version="1.0.0"
)
```

---

用途：

```text
Swagger 文件標題
版本資訊
API 描述
```

---

# API Tags

設定：

```python
@app.get("/", tags=["System"])
```

```python
@app.get("/snapshot", tags=["Monitoring"])
```

```python
@app.get("/health", tags=["Monitoring"])
```

---

Swagger 顯示：

```text
System
 └ GET /

Monitoring
 ├ GET /snapshot
 └ GET /health
```

---

# 本週學習重點

本週學會：

* FastAPI
* Uvicorn
* REST API
* OpenAPI
* Swagger UI
* ReDoc
* Pydantic
* BaseModel
* Response Model
* API Schema
* Python Package
* **init**.py
* API Metadata
* API Tags

---

# 架構演進

Week 3：

```text
Python Script
↓
JSON File
```

Week 4 初期：

```text
FastAPI
↓
JSON Response
```

Week 4 中期：

```text
FastAPI
↓
Health Check
↓
JSON Response
```

Week 4 後期：

```text
FastAPI
↓
Pydantic Model
↓
OpenAPI Schema
↓
Swagger UI
```

---

# 結論

本階段完成 FastAPI Response Model 建立。

Health API 已具備：

* 標準化 Response Schema
* Pydantic Validation
* OpenAPI Integration
* Swagger Documentation

並建立後續 Snapshot、Benchmark API Schema 的基礎架構。

