# 專案架構說明

## 專案目標

本專案目標為建立一套簡易 Monitoring 與 Benchmark 平台。

透過實作方式學習：

* Linux
* Python
* Monitoring
* REST API
* Dashboard
* Infrastructure as Code

相關技術。

---

# 整體架構

```text
Linux VM
│
├─ System Metrics
│
▼
Monitoring Collector
(Shell / Python)
│
▼
JSON Report
│
▼
FastAPI
│
▼
Dashboard
│
▼
Infrastructure Automation
```

---

# 架構說明

## 第一層：Linux 系統

資料來源：

```text
/proc/meminfo
/proc/loadavg
/proc/cpuinfo
```

以及：

```bash
free
df
uptime
```

等系統指令。

---

## 第二層：Monitoring Collector

目前有兩種版本。

### Shell Script

位置：

```text
monitoring/scripts
```

用途：

```text
快速收集系統資訊
```

---

### Python

位置：

```text
monitoring/python
```

用途：

```text
建立可維護的監控程式
```

目前採用：

```python
class SystemSnapshot
```

作為監控資料收集器。

---

## 第三層：Report

位置：

```text
reports
```

用途：

```text
保存監控結果
```

格式：

```text
.log
.json
```

---

## 第四層：API

位置：

```text
api
```

規劃：

透過 FastAPI 提供：

```text
GET /snapshot
GET /health
```

讓其他系統取得監控資料。

---

## 第五層：Dashboard

位置：

```text
dashboards
```

用途：

```text
監控資料視覺化
```

未來規劃：

* Grafana
* Custom Dashboard

---

## 第六層：Infrastructure

位置：

```text
infra
```

內容：

```text
Terraform
Kubernetes
Helm
```

用途：

```text
Infrastructure as Code
```

---

## 第七層：GitOps

位置：

```text
gitops
```

未來規劃：

```text
ArgoCD
GitOps Deployment
```

---

# 目前完成進度

已完成：

```text
Linux Analysis
Shell Monitoring
Cron Automation
Python Monitoring
JSON Export
Git Workflow
```

進行中：

```text
FastAPI
```

未來規劃：

```text
Dashboard
Benchmark
Terraform
Kubernetes
GitOps
```

---

# 設計理念

本專案不是單純練習 Python。

而是模擬真實環境中的：

```text
資料收集
↓
資料整理
↓
API 提供
↓
視覺化展示
↓
自動化部署
```

流程。

透過逐步擴充功能，建立一套完整的 Monitoring 與 Platform Engineering 學習平台。

