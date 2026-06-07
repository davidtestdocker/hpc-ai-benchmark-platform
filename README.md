# HPC AI Benchmark Platform

以 Cloud Native 架構打造的 AI Benchmark Platform。

本專案目標為學習與實作：

* Linux Performance Analysis
* Docker
* Kubernetes
* Terraform
* GitHub Actions
* ArgoCD
* Prometheus
* Grafana
* vLLM
* GPU Monitoring
* AI Benchmarking

最終目標為建置一套可部署、可監控、可壓測的 AI Infrastructure Platform。

---

# 學習進度

## Week 1 Linux Performance Analysis

### Day 1

主題：

* CPU
* Memory
* Load Average

文件：

* docs/linux-performance.md

---

### Day 2

主題：

* PID
* PPID
* Process Tree
* Process Monitoring

文件：

* docs/process-analysis.md

---

### Day 3

主題：

* vmstat
* iostat
* CPU Bottleneck
* Disk IO Bottleneck

文件：

* docs/vmstat-iostat-analysis.md

---

# 專案結構

```text
hpc-ai-benchmark-platform

├── docs
├── api
├── benchmark
├── monitoring
├── infra
├── dashboards
└── README.md
```

---

# 最終架構規劃

```text
GitHub
   │
   ▼

GitHub Actions
   │
   ▼

Docker Registry
   │
   ▼

ArgoCD
   │
   ▼

Kubernetes

├── FastAPI
├── Benchmark Worker
├── vLLM
├── Prometheus
├── Grafana
└── DCGM Exporter

   │
   ▼

Benchmark Report

- TPS
- TTFT
- Latency
- GPU Utilization
```

---

# 預計學習內容

## Infrastructure

* Linux
* Docker
* Kubernetes
* Terraform
* Helm
* GitOps

## Observability

* Prometheus
* Grafana
* DCGM Exporter

## AI Infrastructure

* LLM
* vLLM
* Transformer
* Benchmark
* GPU Monitoring

## HPC

* CUDA
* NCCL
* RDMA
* Distributed Training

---

# 目前進度

* Week 1 Day 1 完成
* Week 1 Day 2 完成
* Week 1 Day 3 完成

專案持續開發中。

