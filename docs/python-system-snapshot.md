# Python System Snapshot 學習筆記

## 學習目標

使用 Python 取代 Shell Script，建立一個可重複使用的 Linux 系統監控工具。

---

# 為什麼從 Shell Script 改成 Python

Week2 我們使用：

```bash
free -h
uptime
df -h
```

取得系統資訊。

Shell Script 適合簡單任務：

```bash
MEM=$(free -h | awk ...)
```

但當功能變多：

* CPU
* Memory
* Disk
* Network
* Process
* GPU

程式會越來越難維護。

因此實務上常見架構：

```text
Linux System
↓
Python
↓
JSON
↓
REST API
↓
Dashboard
```

---

# Linux 系統資訊來源

Linux 會透過：

```text
/proc
```

提供系統資訊。

常見檔案：

```text
/proc/meminfo
/proc/loadavg
/proc/cpuinfo
```

Python 其實只是讀取這些檔案。

---

# Function

## 語法

```python
def get_mem_available():
```

用途：

```text
把功能封裝起來
重複使用
```

---

## Return

語法：

```python
return value
```

範例：

```python
return "14510604 kB"
```

執行流程：

```text
Function
↓
return
↓
呼叫者取得結果
```

例如：

```python
mem = get_mem_available()
```

---

# String Method

## startswith()

用途：

```text
判斷字串是否以指定內容開頭
```

範例：

```python
line.startswith("MemAvailable:")
```

結果：

```python
True
```

或：

```python
False
```

---

## split()

用途：

```text
切割字串
```

範例：

```python
line = "MemAvailable: 14510604 kB"

line.split()
```

結果：

```python
[
    "MemAvailable:",
    "14510604",
    "kB"
]
```

---

## replace()

用途：

```text
字串取代
```

範例：

```python
"4%".replace("%", "")
```

結果：

```python
"4"
```

---

# List

split() 回傳：

```python
list
```

例如：

```python
data = [
    "1.17",
    "1.08",
    "1.06"
]
```

取得資料：

```python
data[0]
```

結果：

```python
1.17
```

---

# Dictionary

用途：

```text
儲存結構化資料
```

語法：

```python
snapshot = {
    "hostname": hostname,
    "cpu_count": cpu_count
}
```

取得資料：

```python
snapshot["hostname"]
```

結果：

```python
manual-vm
```

---

# JSON

JSON 是跨語言資料交換格式。

範例：

```json
{
    "hostname": "manual-vm",
    "cpu_count": 4
}
```

常用於：

* API
* Dashboard
* Monitoring
* Microservices

---

# json.dumps()

語法：

```python
json.dumps(snapshot)
```

用途：

```text
Python Object
↓
轉成 JSON 字串
```

範例：

```python
json.dumps(snapshot)
```

結果：

```python
'{"hostname":"manual-vm"}'
```

注意：

```text
結果是字串
不是檔案
```

---

# json.dump()

語法：

```python
json.dump(snapshot, file, indent=4)
```

用途：

```text
Python Object
↓
直接寫入檔案
```

流程：

```text
Dictionary
↓
json.dump()
↓
system_snapshot.json
```

---

# indent=4

用途：

```text
格式化 JSON
增加可讀性
```

沒有：

```json
{"hostname":"manual-vm"}
```

有：

```json
{
    "hostname": "manual-vm"
}
```

---

# with open()

語法：

```python
with open("file.txt", "w") as file:
```

用途：

```text
開啟檔案
自動關閉檔案
```

優點：

```text
避免忘記 close()
```

---

# Class

原本：

```python
get_mem_available()
get_load_average()
get_disk_usage()
```

都是獨立 Function。

重構後：

```python
class SystemSnapshot:
```

變成：

```python
snapshot.get_mem_available()
snapshot.get_load_average()
```

優點：

```text
程式結構更清楚
容易擴充
```

---

# Object

建立物件：

```python
snapshot = SystemSnapshot()
```

概念：

```text
Class
↓
設計圖

Object
↓
實際建立出來的實體
```

例如：

```text
汽車設計圖
↓
Class

Toyota Camry
↓
Object
```

---

# Method

Class 裡面的 Function 稱為：

```text
Method
```

例如：

```python
def get_disk_usage(self):
```

---

# self

語法：

```python
def get_disk_status(self):
```

用途：

```text
代表目前物件自己
```

例如：

```python
self.get_disk_usage()
```

意思：

```text
呼叫同一個物件內的 get_disk_usage()
```

---

# CPU Count

語法：

```python
os.cpu_count()
```

用途：

```text
取得 CPU 核心數
```

等價於：

```bash
nproc
```

本機結果：

```text
4
```

---

# UTC Time

原本：

```python
datetime.utcnow()
```

新版 Python 不建議使用。

改成：

```python
from datetime import datetime, timezone

datetime.now(timezone.utc)
```

結果：

```text
2026-06-08 16:11:31+00:00
```

優點：

```text
帶有時區資訊
適合分散式系統
```

---

# Relative Path 問題

錯誤範例：

```python
../../reports/system_snapshot.json
```

如果執行位置改變：

```bash
python3 monitoring/python/system_snapshot.py
```

可能找不到路徑。

原因：

```text
相對路徑是依據目前工作目錄
不是程式檔案位置
```

---

# 最終輸出

產生：

```text
reports/system_snapshot.json
```

內容：

```json
{
    "time": "2026-06-08 16:11:31.012554+00:00",
    "hostname": "manual-vm",
    "memory_available": "14510604 kB",
    "load_average": "1.17, 1.08, 1.06",
    "disk_usage": "4%",
    "disk_status": "OK",
    "cpu_count": 4
}
```

---

# 本章重點

這週真正學到的不是 Python 語法而已。

而是理解：

```text
Linux
↓
取得系統資訊

Python
↓
封裝邏輯

Dictionary
↓
建立資料模型

JSON
↓
標準化輸出

API
↓
提供服務
```

這就是監控系統與平台工程最基礎的架構概念。

