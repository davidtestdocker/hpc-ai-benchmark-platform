# CPU Benchmark 學習筆記

## 學習目標

本階段目標：

* 了解 Benchmark 與 Monitoring 的差異
* 建立第一個 CPU Benchmark 工具
* 使用 Python 執行 CPU 運算測試
* 計算執行時間
* 計算每秒運算次數
* 將 Benchmark 結果輸出為 JSON Report

---

# Benchmark 是什麼

Benchmark 是用來主動測試系統效能的方法。

Monitoring 是觀察目前系統狀態：

```text
系統正在做什麼
目前 CPU / Memory / Disk 狀態如何
```

Benchmark 是主動施加負載並測量結果：

```text
系統在指定工作下可以跑多快
每秒可以完成多少運算
耗時多久
```

---

# Monitoring 與 Benchmark 差異

| 類型         | 說明          |
| ---------- | ----------- |
| Monitoring | 被動觀察系統狀態    |
| Benchmark  | 主動執行測試並量測效能 |

---

# CPU Benchmark 目標

本專案第一版 CPU Benchmark 目標：

```text
執行大量 CPU 運算
計算總耗時
計算每秒運算次數
輸出 JSON Report
```

---

# 檔案位置

```text
benchmark/python/cpu_benchmark.py
```

---

# 程式架構

```text
CPUBenchmark
↓
run()
↓
CPU 運算迴圈
↓
計算 duration
↓
計算 operations_per_second
↓
輸出 JSON
```

---

# CPUBenchmark Class

建立：

```python
class CPUBenchmark:
```

用途：

```text
封裝 CPU Benchmark 執行邏輯
```

---

# run() 方法

```python
def run(self, iterations: int = 10_000_000) -> dict:
```

說明：

* `iterations` 代表測試迴圈次數
* 預設執行 10,000,000 次
* 回傳 Benchmark 結果 Dictionary

---

# CPU 運算邏輯

```python
result = 0

for i in range(iterations):
    result += i * i
```

用途：

```text
透過大量整數乘法與加法製造 CPU 負載
```

這是一種簡單的 CPU-bound workload。

---

# time.time()

使用：

```python
start_time = time.time()
```

以及：

```python
end_time = time.time()
```

計算：

```python
duration = end_time - start_time
```

用途：

```text
測量 Benchmark 執行耗時
```

---

# operations_per_second

計算：

```python
operations_per_second = round(iterations / duration, 2)
```

代表：

```text
每秒完成多少次迴圈運算
```

範例：

```text
8,940,110.93 operations/sec
```

---

# JSON 輸出

使用：

```python
json.dumps(benchmark_result, indent=4)
```

將 Python Dictionary 轉成 JSON 字串。

---

# JSON Report

Benchmark 結果會寫入：

```text
reports/cpu_benchmark.json
```

範例：

```json
{
    "benchmark": "cpu",
    "hostname": "manual-vm",
    "iterations": 10000000,
    "duration_seconds": 1.1186,
    "operations_per_second": 8940110.93,
    "result": 333333283333335000000
}
```

---

# 欄位說明

| 欄位                    | 說明             |
| --------------------- | -------------- |
| benchmark             | Benchmark 類型   |
| hostname              | 執行測試的主機名稱      |
| iterations            | 測試迴圈次數         |
| duration_seconds      | 執行耗時           |
| operations_per_second | 每秒運算次數         |
| result                | 運算結果，用於避免迴圈被忽略 |

---

# 為什麼 result 要保留

```python
result += i * i
```

最後會產生：

```text
333333283333335000000
```

這個值本身不是效能指標。

保留原因是：

```text
確保 CPU 真的有執行運算
避免程式邏輯看起來像空迴圈
```

---

# 執行方式

```bash
python3 benchmark/python/cpu_benchmark.py
```

---

# 查看結果

```bash
cat reports/cpu_benchmark.json
```

---

# 本階段學習重點

本階段學會：

* Benchmark 基本概念
* CPU-bound Workload
* Python Class
* for loop
* range()
* time.time()
* duration 計算
* operations_per_second 計算
* json.dumps()
* json.dump()
* JSON Report 輸出

---

# 專案架構演進

原本：

```text
Monitoring
↓
System Snapshot
↓
JSON Report
```

新增：

```text
Benchmark
↓
CPU Benchmark
↓
JSON Report
```

---

# 後續規劃

下一步會將 CPU Benchmark 整合進 FastAPI：

```http
GET /benchmark/cpu
```

讓 Benchmark 結果可以透過 API 查詢。

