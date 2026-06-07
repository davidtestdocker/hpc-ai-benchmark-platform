# Shell Automation（Shell 自動化）

## 學習目標

了解 Linux Shell Script 的基本概念，並建立自動化監控腳本。

本週內容包含：

* Shell Variable
* Command Substitution
* if / else
* Output Redirect
* Cron Job
* System Monitoring Script

---

# Shell Variable

變數用來儲存資料。

範例：

```bash
HOST="manual-vm"
```

代表：

```text
建立 HOST 變數
內容為 manual-vm
```

---

# Command Substitution

Command Substitution 可以取得指令執行結果並存入變數。

範例：

```bash
HOST=$(hostname)
```

執行流程：

```text
hostname
↓
取得主機名稱
↓
存入 HOST
```

結果：

```text
HOST=manual-vm
```

---

# 常見範例

取得時間：

```bash
NOW=$(date)
```

取得主機名稱：

```bash
HOST=$(hostname)
```

取得 Load Average：

```bash
LOAD=$(uptime | awk -F'load average:' '{print $2}')
```

---

# if / else

條件判斷語法：

```bash
if [ 條件 ]; then
    指令
else
    指令
fi
```

範例：

```bash
if [ "$DISK_NUM" -gt 80 ]; then
    echo "WARNING"
else
    echo "OK"
fi
```

---

# Shell 整數比較

| 語法  | 說明   |
| --- | ---- |
| -eq | 等於   |
| -ne | 不等於  |
| -gt | 大於   |
| -lt | 小於   |
| -ge | 大於等於 |
| -le | 小於等於 |

---

# Output Redirect

輸出重新導向。

---

## 覆蓋

```bash
echo hello > test.log
```

效果：

```text
清空舊內容
寫入新內容
```

---

## 追加

```bash
echo hello >> test.log
```

效果：

```text
保留舊內容
追加新內容
```

---

# System Snapshot Script

建立：

```text
monitoring/scripts/system_snapshot.sh
```

功能：

* 顯示時間
* 顯示主機名稱
* 顯示 Uptime
* 顯示 Load Average
* 顯示 Available Memory
* 顯示 Disk Usage
* 顯示 Disk Status

---

# 範例輸出

```text
===== System Snapshot =====

Time: Sun Jun 7 13:00:28 UTC 2026
Hostname: manual-vm
Uptime: up 3 days, 21 hours
Available Memory: 15Gi
Load Average: 0.10, 0.03, 0.01
Disk Usage: 3%
Disk Status: OK
```

---

# Cron

Cron 是 Linux 排程工具。

用途：

```text
定期執行工作
```

---

## Crontab 格式

```text
* * * * * command
│ │ │ │ │
│ │ │ │ └ 星期
│ │ │ └── 月
│ │ └──── 日
│ └────── 小時
└──────── 分鐘
```

---

## 每分鐘執行

```cron
* * * * * command
```

---

# 自動收集系統資訊

設定：

```cron
* * * * * /root/hpc-ai-benchmark-platform/monitoring/scripts/system_snapshot.sh >> /root/hpc-ai-benchmark-platform/reports/system_snapshot.log
```

效果：

```text
每分鐘執行一次
並將結果寫入 Log
```

---

# 學習成果

本週完成：

* Shell Variable
* Command Substitution
* if / else
* Redirect
* Cron
* System Monitoring Script

並建立第一個可自動執行的 Linux Monitoring Tool。

