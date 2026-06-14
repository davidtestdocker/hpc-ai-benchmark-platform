# HPC AI Benchmark Platform

## 專案介紹

本專案是一個以 Linux、Python、Monitoring、Automation、REST API 與 Infrastructure 為主軸的學習型工程專案。

目標是透過實作方式，逐步建立一套可展示於履歷與面試的 Monitoring / Benchmark Platform。

目前已完成：

* Linux 效能分析
* Shell Script 自動化監控
* Cron 自動執行
* Python Monitoring Collector
* JSON Report 輸出
* FastAPI Monitoring API
* Enhanced Health Check

---

# 學習路線

```text
Linux
↓
Shell Automation
↓
Python Monitoring
↓
REST API
↓
Dashboard
↓
Infrastructure as Code
↓
GitOps
```

---

# 目前完成項目

## Linux 效能分析

已完成：

* Process Analysis
* Memory Analysis
* Network Analysis
* vmstat Analysis
* iostat Analysis
* SAR Analysis

相關文件：

```text
docs/linux-performance.md
docs/process-analysis.md
docs/memory-analysis.md
docs/network-analysis.md
docs/vmstat-iostat-analysis.md
docs/sar-analysis.md
```

---

## Shell Automation

建立：

```text
monitoring/scripts/system_snapshot.sh
```

功能：

* 取得主機名稱
* 取得可用記憶體
* 取得 Load Average
* 取得磁碟使用率
* 判斷磁碟狀態
* 輸出 Log
* 使用 Cron 自動執行

相關文件：

```text
docs/shell-automation.md
```

---

## Python Monitoring Collector

建立：

```text
monitoring/python/system_snapshot.py
```

功能：

* Hostname
* CPU Count
* Memory Available
* Load Average
* Disk Usage
* Disk Status
* UTC Timestamp
* JSON Export

輸出範例：

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

相關文件：

```text
docs/python-system-snapshot.md
```

---

## FastAPI Monitoring API

建立：

```text
api/main.py
```

目前已完成 API：

```http
GET /
GET /snapshot
GET /health
```

功能：

* API Service
* 即時監控資料查詢
* 健康狀態檢查
* Monitoring API 設計

相關文件：

```text
docs/fastapi-monitoring-api.md
```

---

# API 使用方式

## 啟動 API Server

```bash
uvicorn api.main:app --host 0.0.0.0 --port 8000
```

---

## GET /

用途：

```text
確認 API Server 正常運作
```

測試：

```bash
curl http://localhost:8000/
```

Response：

```json
{
    "message": "HPC AI Benchmark Platform"
}
```

---

## GET /snapshot

用途：

```text
取得即時系統監控資料
```

測試：

```bash
curl http://localhost:8000/snapshot
```

Response：

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

## GET /health

用途：

```text
評估系統健康狀態
```

檢查項目：

* 磁碟使用率（Disk Usage）
* 系統負載（Load Average）
* 可用記憶體（Available Memory）

測試：

```bash
curl http://localhost:8000/health
```

Response：

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

## Health Check 判斷邏輯

### Disk Usage

```text
Disk Usage > 80%
```

狀態：

```text
warning
```

---

### Load Average

```text
Load Average > CPU Core × 2
```

狀態：

```text
warning
```

---

### Available Memory

```text
Available Memory < 1GB
```

狀態：

```text
warning
```

---

### Health Status

#### healthy

所有檢查皆正常。

#### degraded

任一檢查項目異常。

---

# 專案目錄結構

```text
hpc-ai-benchmark-platform
├── api
│   └── main.py
├── benchmark
├── dashboards
├── docs
├── gitops
├── infra
├── monitoring
│   ├── scripts
│   │   └── system_snapshot.sh
│   └── python
│       └── system_snapshot.py
└── reports
```

詳細架構說明：

```text
docs/project-architecture.md
```

---

# 如何執行

## Shell Monitoring

```bash
bash monitoring/scripts/system_snapshot.sh
```

---

## Python Monitoring

```bash
python3 monitoring/python/system_snapshot.py
```

查看 JSON 輸出：

```bash
cat reports/system_snapshot.json
```

---

## FastAPI Monitoring API

```bash
uvicorn api.main:app --host 0.0.0.0 --port 8000
```

測試：

```bash
curl http://localhost:8000/
curl http://localhost:8000/snapshot
curl http://localhost:8000/health
```

---

# 學習重點

本專案目前已學習：

* Linux System Analysis
* Process Analysis
* Memory Analysis
* Network Analysis
* vmstat
* iostat
* sar
* Shell Script
* Cron Job
* Git Workflow
* Python Function
* Python Class
* Python Import
* JSON Export
* FastAPI
* REST API
* Monitoring API Design
* Health Check Design
* Dictionary
* Service Layer Concept

---

# 後續規劃

## Phase 4：FastAPI Monitoring API

已完成：

* [x] GET /
* [x] GET /snapshot
* [x] GET /health
* [x] Enhanced Health Check
* [x] Disk Usage Health Check
* [x] Load Average Health Check
* [x] Memory Health Check

進行中：

* [ ] Swagger API Documentation
* [ ] API Metadata
* [ ] API Tags
* [ ] Response Model

---

## Phase 5：Benchmark Module

預計實作：

* CPU Benchmark
* Memory Benchmark
* Disk Benchmark

---

## Phase 6：Dashboard

預計實作：

* Grafana
* Monitoring Dashboard

---

## Phase 7：Infrastructure

預計實作：

* Terraform
* Kubernetes
* Helm

---

## Phase 8：GitOps

預計實作：

* ArgoCD
* GitOps Workflow

---

# 專案定位

本專案不是單純練習指令或撰寫 Script。

目標是從 Linux 基礎開始，逐步建立一套具備以下能力的工程作品：

```text
Metrics Collection
↓
Automation
↓
Python Collector
↓
REST API
↓
Monitoring Service
↓
Dashboard
↓
Infrastructure Automation
```

可作為：

* SRE
* DevOps Engineer
* Platform Engineer
* MLOps Engineer
* AI Infrastructure Engineer

相關職位的學習與面試作品。

