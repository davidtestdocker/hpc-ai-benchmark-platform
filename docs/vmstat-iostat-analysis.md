# VMSTAT 與 IOSTAT 效能分析筆記

## 學習目標

學習使用 Linux 效能分析工具：

* vmstat
* iostat

判斷系統瓶頸來源。

了解：

* CPU Bottleneck
* Disk IO Bottleneck
* IO Wait
* Run Queue

等重要概念。

---

# 為什麼需要 vmstat 與 iostat

很多人看到：

```text
CPU Usage 100%
```

就認為 CPU 壞掉了。

但實際上系統效能問題可能來自：

```text
CPU
Memory
Disk IO
Network
```

因此需要搭配不同工具分析。

常見工具：

```text
top
vmstat
iostat
sar
```

---

# VMSTAT

## 指令

```bash
vmstat 1 5
```

意思：

```text
每 1 秒收集一次
總共收集 5 次
```

---

# VMSTAT 輸出範例

```text
procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu-----
 r  b    swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st
 0  0       0 14500000 120000 500000  0    0     0     0  100  200  0  0 100  0  0
```

---

# 重點欄位

## r (Run Queue)

代表：

```text
等待 CPU 執行的程序數量
```

例如：

```text
r = 0
```

代表：

```text
沒有程序等待 CPU
```

---

如果：

```text
r = 8
```

而系統只有：

```text
4 CPU Core
```

代表：

```text
CPU 已經不夠用
```

有程序在排隊。

---

## b (Blocked)

代表：

```text
被阻塞的程序數量
```

通常在等待：

```text
Disk IO
Network IO
```

---

正常情況：

```text
b = 0
```

---

如果：

```text
b = 10
```

可能表示：

```text
大量程序等待 IO
```

---

## id (Idle)

代表：

```text
CPU 閒置比例
```

例如：

```text
id = 100
```

代表：

```text
CPU 完全沒事做
```

---

如果：

```text
id = 0
```

代表：

```text
CPU 已經滿載
```

---

## wa (IO Wait)

最重要的欄位之一。

代表：

```text
CPU 花多少時間等待 IO 完成
```

例如：

```text
wa = 0
```

表示：

```text
沒有 IO 壓力
```

---

如果：

```text
wa = 25
```

代表：

```text
CPU 有 25% 時間在等磁碟
```

這時候問題通常不是 CPU。

而是：

```text
Storage
```

---

# CPU 壓力測試

## 指令

```bash
yes > /dev/null &
yes > /dev/null &
yes > /dev/null &
yes > /dev/null &
```

---

# yes 指令

用途：

```text
持續輸出字元 y
```

例如：

```bash
yes
```

輸出：

```text
y
y
y
y
y
...
```

永遠不停止。

---

# /dev/null

Linux 黑洞裝置。

所有寫入內容：

```text
直接丟棄
```

例如：

```bash
echo hello > /dev/null
```

結果：

```text
沒有任何輸出
```

---

# &

代表：

```text
背景執行
```

例如：

```bash
sleep 100 &
```

不會阻塞目前 Terminal。

---

# CPU Stress 結果

```text
r = 4
id = 0
wa = 0
```

分析：

```text
4 個程序持續運算
CPU 閒置時間歸零
沒有 IO 等待
```

因此可判斷：

```text
CPU 成為瓶頸
```

---

# IOSTAT

## 指令

```bash
iostat -x 1 5
```

---

# 參數說明

## -x

代表：

```text
Extended Statistics
```

顯示進階磁碟資訊。

例如：

```text
await
svctm
util
```

---

# 重點欄位

## r/s

代表：

```text
每秒讀取次數
```

---

## w/s

代表：

```text
每秒寫入次數
```

---

## await

代表：

```text
平均 IO 延遲時間
```

單位：

```text
毫秒(ms)
```

---

例如：

```text
await = 1ms
```

表示：

```text
磁碟反應很快
```

---

如果：

```text
await = 100ms
```

表示：

```text
磁碟反應非常慢
```

---

## %util

代表：

```text
磁碟使用率
```

---

例如：

```text
util = 10%
```

表示：

```text
磁碟很閒
```

---

如果：

```text
util = 95%
```

表示：

```text
磁碟接近飽和
```

---

# 磁碟壓力測試

## 指令

```bash
dd if=/dev/zero of=testfile2 bs=1M count=8192 oflag=direct status=progress
```

---

# 指令拆解

## if=/dev/zero

代表：

```text
輸入來源
```

內容全部為：

```text
0
```

---

## of=testfile2

代表：

```text
輸出檔案
```

---

## bs=1M

代表：

```text
每次寫入 1MB
```

---

## count=8192

代表：

```text
寫入 8192 次
```

總大小：

```text
8192 MB
=
8 GB
```

---

## oflag=direct

代表：

```text
Direct IO
```

繞過 Linux Page Cache。

可以更真實測試磁碟效能。

---

# 測試結果

```text
wa = 23%
util = 92%
```

分析：

```text
CPU 有 23% 時間等待磁碟

磁碟利用率超過 90%
```

因此可判斷：

```text
Storage 成為瓶頸
```

而不是 CPU。

---

# 效能分析思維

錯誤觀念：

```text
CPU 使用率高
=
CPU 有問題
```

---

正確觀念：

需要同時觀察：

```text
CPU
Memory
Disk
Network
```

---

例如：

```text
CPU 100%
wa 0%
```

可能是：

```text
CPU Bottleneck
```

---

如果：

```text
CPU 30%
wa 40%
```

則可能是：

```text
Disk Bottleneck
```

---

# 本章重點

學會使用：

```text
vmstat
iostat
```

判斷系統瓶頸。

理解：

```text
r
b
id
wa

r/s
w/s
await
util
```

代表的意義。

效能分析不是只看 CPU。

而是要從：

```text
CPU
Memory
Disk
Network
```

四個面向綜合判斷系統問題來源。

