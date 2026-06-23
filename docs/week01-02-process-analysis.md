# Linux Process Analysis

## Objective

學習 Linux Process 的基本概念：

* PID
* PPID
* Process Tree
* CPU Usage
* Process State
* Process Termination
* Signal
* Zombie Process

---

## Process List

查看 Process：

```bash
ps aux
```

查看前幾筆：

```bash
ps aux | head
```

重要欄位：

| Column  | Description         |
| ------- | ------------------- |
| PID     | Process ID          |
| %CPU    | CPU Usage           |
| %MEM    | Memory Usage        |
| VSZ     | Virtual Memory Size |
| RSS     | Resident Memory     |
| STAT    | Process State       |
| COMMAND | Executed Command    |

---

## PID 1

查看：

```bash
ps -p 1 -f
```

結果：

```text
/sbin/init
```

或：

```text
/usr/lib/systemd/systemd
```

PID 1 為 Linux 啟動後的第一個 Process。

所有 Process 最終都會追溯到 PID 1。

---

## Parent Process

查看目前 Shell：

```bash
echo $$
```

查看詳細資訊：

```bash
ps -fp <PID>
```

查看 Parent PID：

```bash
echo $PPID
```

Process 之間存在 Parent / Child 關係。

---

## Process Tree

安裝：

```bash
apt install -y psmisc
```

查看：

```bash
pstree -p
```

範例：

```text
systemd
 └── sshd
      └── bash
```

Process 之間存在樹狀結構。

當 Parent Process 建立新的 Process 時，

新的 Process 稱為 Child Process。

---

## Background Process

建立背景工作：

```bash
sleep 300 &
```

查看：

```bash
jobs
```

或：

```bash
ps aux | grep sleep
```

結果：

```text
sleep 300
```

背景程序會持續執行，不會占用目前 Shell。

---

## CPU Stress Test

建立 CPU Burner：

```bash
yes > /dev/null &
```

查看：

```bash
ps aux --sort=-%cpu | head
```

結果：

```text
yes
CPU ≈ 99%
```

可用來模擬高 CPU 使用率情境。

---

## Process State

常見狀態：

| State | Meaning               |
| ----- | --------------------- |
| R     | Running               |
| S     | Sleeping              |
| D     | Uninterruptible Sleep |
| Z     | Zombie                |
| T     | Stopped               |

本次實驗：

```text
yes → R
sleep → S
```

---

## STAT 欄位說明

實際環境中常看到：

```text
Ss
Sl
Ssl
R+
```

STAT 可能由多個字母組成。

範例：

```text
S
```

代表：

```text
Sleeping
```

```text
Ss
```

代表：

```text
Sleeping
+
Session Leader
```

```text
R+
```

代表：

```text
Running
+
Foreground Process Group
```

因此 STAT 不一定只有單一字母。

---

## Zombie Process

Zombie Process：

```text
Child Process 已結束，

但 Parent Process 尚未回收 Exit Status。
```

查看：

```bash
ps aux | grep Z
```

範例：

```text
STAT = Z
```

Zombie Process 幾乎不消耗 CPU 與 Memory。

但如果大量累積：

```text
代表程式設計或 Process 管理可能有問題。
```

---

## RSS 與 VIRT

查看：

```bash
top
```

或：

```bash
ps aux
```

常見欄位：

### RSS

Resident Set Size

```text
Process 實際使用的實體記憶體大小。
```

---

### VIRT

Virtual Memory

```text
Process 可存取的虛擬記憶體空間。
```

通常：

```text
VIRT > RSS
```

因為並非所有虛擬記憶體都已實際配置到 RAM。

---

## Kill Process

停止：

```bash
kill PID
```

預設為：

```text
SIGTERM (15)
```

代表：

```text
要求程式正常結束。
```

---

強制終止：

```bash
kill -9 PID
```

代表：

```text
SIGKILL (9)
```

直接由 Kernel 終止 Process。

---

建議順序：

```text
先使用 SIGTERM

若無法結束

再使用 SIGKILL
```

---

## Observation

SRE 排障流程：

1. 找出高 CPU Process
2. 查看 PID
3. 查看 PPID
4. 查看 Process Tree
5. 查看 Process State
6. 確認 Root Cause
7. 終止或修復 Process

---

## Interview Notes

### PID 是什麼？

Process 的唯一識別碼。

---

### PID 1 是什麼？

Linux 啟動後的第一個 Process。

通常是：

```text
systemd
```

---

### Zombie Process 是什麼？

Child Process 已結束，

但 Parent Process 尚未回收資源。

---

### RSS 與 VIRT 差異？

RSS：

```text
實際佔用的實體記憶體。
```

VIRT：

```text
Process 可使用的虛擬記憶體空間。
```

---

### kill 與 kill -9 差異？

SIGTERM：

```text
要求程式正常結束。
```

SIGKILL：

```text
直接由 Kernel 強制終止。
```

```
```

