# Linux Process Analysis

## Objective

學習 Linux Process 的基本概念：

* PID
* PPID
* Process Tree
* CPU Usage
* Process State
* Process Termination

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

| Column  | Description      |
| ------- | ---------------- |
| PID     | Process ID       |
| %CPU    | CPU Usage        |
| %MEM    | Memory Usage     |
| STAT    | Process State    |
| COMMAND | Executed Command |

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

Process 之間存在 Parent / Child 關係。

---

## Background Process

建立背景工作：

```bash
sleep 300 &
```

查看：

```bash
ps aux | grep sleep
```

結果：

```text
sleep 300
```

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

---

## Process State

常見狀態：

| State | Meaning               |
| ----- | --------------------- |
| R     | Running               |
| S     | Sleeping              |
| D     | Uninterruptible Sleep |
| Z     | Zombie                |

本次實驗：

```text
yes → R
sleep → S
```

---

## Kill Process

停止：

```bash
kill PID
```

驗證：

```bash
ps aux | grep process_name
```

---

## Observation

SRE 排障流程：

1. 找出高 CPU Process
2. 查看 PID
3. 查看 PPID
4. 查看 Process Tree
5. 確認 Root Cause
6. 終止或修復 Process

```
```

