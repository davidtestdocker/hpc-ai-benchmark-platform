# Memory Analysis（記憶體分析）

## 學習目標

了解 Linux 記憶體管理機制，包含：

* Memory Usage
* MemFree
* MemAvailable
* Buffers
* Cached
* OOM Killer

---

## 記憶體資訊查看

### 指令

```bash
free -h
```

### 範例結果

```text
total        15Gi
used        214Mi
free         14Gi
buff/cache  877Mi
available    15Gi
```

---

## 重要欄位說明

| 欄位         | 說明                  |
| ---------- | ------------------- |
| total      | 總記憶體容量              |
| used       | 已使用記憶體              |
| free       | 完全未使用的記憶體           |
| buff/cache | Buffer 與 Page Cache |
| available  | 可提供新程式使用的記憶體        |

---

## 重要觀念

不要只看：

```text
MemFree
```

判斷系統是否缺乏記憶體。

應優先觀察：

```text
MemAvailable
```

原因：

```text
MemAvailable
=
Free Memory
+
Reclaimable Cache
+
Reclaimable Buffers
```

Linux 會利用空閒記憶體作為 Cache 提升效能，需要時可以回收，因此 Cache 不代表真正被佔用。

---

## 查看 Linux 記憶體資訊

### 指令

```bash
cat /proc/meminfo | head -20
```

重要欄位：

```text
MemTotal
MemFree
MemAvailable
Buffers
Cached
```

---

## 記憶體配置實驗

### 指令

```bash
python3 -c "x=' ' * 1024 * 1024 * 1024; input('Press Enter to exit...')"
```

配置約：

```text
1GB RAM
```

---

### 實驗前

```text
MemFree       ~14.5GB
MemAvailable  ~15.1GB
```

### 執行期間

```text
used          ~1.2GB
MemAvailable  ~14GB
```

### 程式結束後

```text
used          ~238MB
MemAvailable  ~15GB
```

### 觀察結果

* 記憶體被程式配置後，MemAvailable 下降
* 程式結束後，記憶體被系統回收
* Linux 會自動管理記憶體資源

---

## OOM Killer

OOM：

```text
Out Of Memory
```

當系統記憶體不足時：

```text
Linux Kernel
↓
OOM Killer
↓
強制終止 Process
```

避免整個系統失去回應。

---

## 檢查 OOM 紀錄

### 指令

```bash
dmesg | grep -i oom
```

用途：

```text
查看 OOM 發生紀錄
查看被終止的 Process
```

---

## OOM Score

### 指令

```bash
cat /proc/$$/oom_score
```

範例：

```text
666
```

說明：

* 分數越高
* 越容易被 OOM Killer 選中

範圍：

```text
0 ~ 1000
```

---

## Kubernetes 關聯

常見錯誤：

```text
OOMKilled
```

發生流程：

```text
Container Memory Usage
↓
超過 Memory Limit
↓
Kernel OOM Killer
↓
Container 被終止
↓
Pod Restart
```

---

## 重點整理

進行 Memory Analysis 時應優先觀察：

* MemAvailable
* Cached
* Buffers
* OOM Events

不要只看：

```text
MemFree
```

因為 Linux 會大量使用記憶體作為 Cache。

---

## 結論

Memory Bottleneck 是下列系統最常見的問題之一：

* Docker
* Kubernetes
* Prometheus
* Grafana
* vLLM
* LLM Inference Service

理解 Linux 記憶體管理機制，是 AI Infrastructure Engineer 與 SRE 必備能力。

