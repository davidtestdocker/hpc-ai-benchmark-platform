# HPC AI Benchmark Platform

## 專案介紹

本專案為 Linux、Python、Monitoring、Automation、API 與 Infrastructure 技術學習專案。

目標是透過實作方式學習：

* Linux 效能分析
* Shell Script 自動化
* Python 開發
* Monitoring 系統設計
* REST API 開發
* Terraform
* Kubernetes
* GitOps

並逐步建立一套可展示於履歷與面試的作品。

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

支援：

* Log 輸出
* Cron 自動執行

相關文件：

```text
docs/shell-automation.md
```

---

## Python Monitoring

建立：

```text
monitoring/python/system_snapshot.py
```

功能：

* CPU Count
* Memory Available
* Load Average
* Disk Usage
* Disk Status

輸出格式：

```json
{
    "time": "2026-06-08T16:11:31+00:00",
    "hostname": "manual-vm",
    "memory_available": "14510604 kB",
    "load_average": "1.17, 1.08, 1.06",
    "disk_usage": "4%",
    "disk_status": "OK",
    "cpu_count": 4
}
```

相關文件：

```text
docs/python-system-snapshot.md
```

---

# 專案目錄結構

```text
hpc-ai-benchmark-platform
├── api
├── benchmark
├── dashboards
├── docs
├── gitops
├── infra
├── monitoring
└── reports
```

詳細說明請參考：

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

查看結果：

```bash
cat reports/system_snapshot.json
```

---

# 學習重點

本專案目前已學習：

* Linux System Analysis
* Shell Script
* Cron Job
* Git Workflow
* Python Function
* Python Class
* JSON Export
* Monitoring Data Collection

---

# 後續規劃

## Phase 4

FastAPI

預計實作：

```text
GET /
GET /snapshot
GET /health
```

---

## Phase 5

Benchmark Module

預計實作：

* CPU Benchmark
* Memory Benchmark
* Disk Benchmark

---

## Phase 6

Dashboard

預計實作：

* Grafana
* Monitoring Dashboard

---

## Phase 7

Infrastructure

預計實作：

* Terraform
* Kubernetes
* Helm

---

## Phase 8

GitOps

預計實作：

* ArgoCD
* GitOps Workflow

```
```

