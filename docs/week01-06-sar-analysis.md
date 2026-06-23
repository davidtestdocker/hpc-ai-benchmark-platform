# SAR Analysis（歷史效能監控分析）

## 學習目標

了解 Linux 歷史效能監控工具 `sar`，包含：

* CPU 使用率分析
* 歷史效能資料查詢
* sysstat 資料收集機制
* 即時監控與歷史監控差異
* Time Series Monitoring 概念

---

# SAR 是什麼

SAR（System Activity Reporter）是 Linux 的效能監控工具。

用途：

* 收集系統效能資料
* 查詢歷史資源使用情況
* 分析 CPU、Memory、Disk、Network 趨勢

安裝套件：

```bash
apt install -y sysstat
```

---

# 即時 CPU 監控

## 指令

```bash
sar -u 1 5
```

參數說明：

| 參數 | 說明        |
| -- | --------- |
| -u | CPU Usage |
| 1  | 每秒收集一次    |
| 5  | 共收集五次     |

---

## 範例結果

```text
CPU     %user   %system   %iowait   %idle
all      0.00      0.00      0.00   100.00
```

說明：

* VM 處於閒置狀態
* 沒有 CPU 壓力
* 沒有 IO 等待

---

# CPU 指標說明

| 指標      | 說明                   |
| ------- | -------------------- |
| %user   | User Space CPU 使用率   |
| %system | Kernel Space CPU 使用率 |
| %iowait | 等待 Disk IO 時間        |
| %idle   | CPU 閒置比例             |
| %steal  | Hypervisor 搶占 CPU 時間 |

---

# sysstat 歷史資料

## 查看資料位置

```bash
ls -lh /var/log/sysstat/
```

範例：

```text
sa07
```

說明：

* sa01 = 每月 1 號
* sa07 = 每月 7 號
* sa31 = 每月 31 號

每個檔案都保存當日效能資料。

---

# 查看歷史 CPU 資料

## 指令

```bash
sar -u -f /var/log/sysstat/sa07
```

用途：

* 讀取歷史資料
* 分析過去 CPU 使用情況

---

## 範例結果

```text
09:00:25 LINUX RESTART
```

說明：

* sysstat 剛開始收集資料
* 尚未累積足夠歷史資訊

---

# CPU 壓力測試

## 指令

```bash
yes > /dev/null &
yes > /dev/null &
yes > /dev/null &
yes > /dev/null &
```

目的：

* 將 4 Core VM CPU 使用率拉高
* 模擬高負載情境

---

# 壓力測試結果

## 指令

```bash
sar -u 1 10
```

結果：

```text
Average:
%user    51.59
%system  48.14
%idle     0.00
```

---

# 結果分析

### %user

```text
51.59%
```

代表：

* User Space 程式消耗 CPU
* yes 指令持續執行

---

### %system

```text
48.14%
```

代表：

* Kernel 持續處理 System Call
* write() 呼叫大量發生

---

### %idle

```text
0%
```

代表：

* CPU 完全沒有空閒時間
* 系統已接近 CPU 滿載

---

# 壓力測試結束

停止測試：

```bash
pkill yes
```

確認：

```bash
ps aux | grep yes
```

應只剩下 grep 本身。

---

# 即時監控與歷史監控

## 即時監控工具

```bash
top
vmstat
iostat
```

特性：

* 只能看到現在
* 無法查看過去狀況

---

## 歷史監控工具

```bash
sar
```

特性：

* 可以查詢過去資料
* 可分析效能趨勢

---

# 與 Prometheus 的關係

SAR 的概念與 Prometheus 類似：

```text
定期收集資料
↓
保存歷史紀錄
↓
查詢趨勢
↓
分析問題
```

Prometheus 則提供：

* 更長期保存
* 更細緻指標
* Grafana 視覺化

---

# SRE 實務情境

常見問題：

```text
昨天凌晨 CPU 為什麼飆高？
```

此時：

```bash
top
```

無法回答。

但：

```bash
sar
Prometheus
Grafana
```

可以透過歷史資料分析問題發生時間與原因。

---

# 常用 SAR 指令

查看 CPU：

```bash
sar -u 1 5
```

---

查看 Memory：

```bash
sar -r 1 5
```

重點：

```text
kbmemfree
kbmemused
%memused
```

---

查看 Disk：

```bash
sar -d 1 5
```

重點：

```text
tps
rkB/s
wkB/s
```

---

查看 Network：

```bash
sar -n DEV 1 5
```

重點：

```text
rxkB/s
txkB/s
```

---

查看歷史資料：

```bash
sar -u -f /var/log/sysstat/sa07
```

用途：

```text
分析過去特定時間的系統狀態
```


# 重點整理

常用指令：

```bash
sar -u 1 5
sar -u -f /var/log/sysstat/sa07
ls -lh /var/log/sysstat/
```

重要指標：

* %user
* %system
* %iowait
* %idle

---

# AI Infrastructure 關聯

AI 平台通常需要長時間運行：

* vLLM
* Ollama
* Prometheus
* Grafana
* Kubernetes

因此：

```text
瞬間 CPU 使用率
```

並不足以判斷系統健康度。

更重要的是：

```text
長時間趨勢
```

例如：

```text
CPU 持續上升
Memory 持續增加
Disk Latency 持續惡化
```

這些問題通常需要透過：

```text
SAR
Prometheus
Grafana
```

進行分析。

---

在 HPC 與 AI Infrastructure 領域：

```text
Trend Analysis
```

往往比：

```text
即時監控
```

更重要。

因為許多效能問題是逐漸累積形成的。


# 結論

SAR 是 Linux 重要的歷史效能分析工具。

對於 SRE、Platform Engineer、AI Infrastructure Engineer 而言，了解歷史監控與趨勢分析，比單純查看即時狀態更重要。

它也是未來學習：

* Prometheus
* Grafana
* Observability

的重要基礎。

