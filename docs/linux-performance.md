# Linux Performance Analysis

## Environment

VM: GCP Compute Engine

Machine Type: e2-standard-4

CPU: 4 vCPU

Memory: 16GB

OS: Ubuntu 22.04

Kernel: 6.8.0-gcp

---

## CPU

查看 CPU 數量：

```bash
nproc
```

結果：

```text
4
```

---

## Memory

查看記憶體：

```bash
free -h
```

重點欄位：

* total
* used
* free
* available

Linux 應優先觀察 available，而非 free。

---

## Load Average

查看：

```bash
uptime
```

範例：

```text
load average: 0.00, 0.00, 0.00
```

代表：

* 1分鐘平均負載
* 5分鐘平均負載
* 15分鐘平均負載

---

## CPU Stress Test

產生 CPU 壓力：

```bash
yes > /dev/null
```

觀察：

```bash
uptime
top
```

結果：

* Load Average 上升
* CPU Idle 下降

---

## Observation

4 vCPU VM：

* Load ≈ 0：系統閒置
* Load ≈ 4：CPU 滿載
* Load > 4：開始出現排隊現象

CPU Usage 與 Load Average 是不同指標。

CPU Usage 表示 CPU 忙碌程度。

Load Average 表示系統中等待執行的工作數量。

