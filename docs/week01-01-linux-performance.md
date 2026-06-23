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

## Load Average 與 CPU Usage 的差異

Load Average 不等於 CPU 使用率。

Load Average 代表系統中正在執行或等待執行的工作數量，包含：

- Runnable Tasks（R）：正在使用 CPU 或等待 CPU 排程的工作
- Uninterruptible Tasks（D）：等待磁碟或 I/O 完成而無法被中斷的工作

因此：

CPU 使用率很低，
但 Load Average 很高，

仍然有可能發生。

常見情況：

- 磁碟讀寫效能不足（Disk I/O Bottleneck）
- NFS 網路儲存延遲過高（NFS Latency）
- Storage 負載過重（Storage Congestion）

例如：

大量程式同時等待磁碟讀取資料時，
CPU 可能只有 10% 使用率，

但因為許多程序處於等待狀態（D State），
Load Average 仍然可能超過 CPU 核心數。

因此分析 Linux 效能問題時：

不能只看 CPU Usage，
還必須搭配 Load Average、iostat、vmstat 等工具一起判斷。
