# Network Analysis（網路分析）

## 學習目標

了解 Linux 網路連線狀態與 Port 監聽機制，包含：

* TCP
* UDP
* Port
* Listen Socket
* Established Connection
* TIME-WAIT
* Process 與 Port 對應關係

---

## 查看網路監聽狀態

### 指令

```bash
ss -tulnp
```

用途：

* 查看 TCP/UDP Port
* 查看 Listen Port
* 查看對應 Process
* 查看 PID

---

## 範例結果

```text
tcp LISTEN 0 128 0.0.0.0:22
users:(("sshd",pid=766))
```

說明：

* SSHD 正在監聽 Port 22
* PID 為 766
* 接受所有 IP 的連線

---

## Local Address

### 0.0.0.0

```text
0.0.0.0:22
```

代表：

* 所有網路介面
* 所有 IP
* 外部可以連線

---

### 127.0.0.1

```text
127.0.0.1:8080
```

代表：

* 僅限本機存取
* 外部無法連線

常見於：

* 開發環境
* 測試服務
* 本機 API

---

## 建立測試服務

### 指令

```bash
python3 -m http.server 8000
```

建立一個簡單 HTTP Server。

---

## 查看服務監聽狀態

### 指令

```bash
ss -tulnp | grep 8000
```

結果：

```text
tcp LISTEN 0 5 0.0.0.0:8000
users:(("python3",pid=22859))
```

說明：

* Python HTTP Server 正在監聽 Port 8000
* PID 為 22859

---

## 驗證服務是否正常

### 指令

```bash
curl http://localhost:8000
```

結果：

```text
Directory listing for /
```

表示：

* HTTP Service 正常運作
* Port 可正常存取

---

## 查看 TCP Connection

### 指令

```bash
ss -tan
```

用途：

* 查看 TCP 連線狀態
* 查看目前所有 Connection

---

## 常見 TCP State

### LISTEN

```text
LISTEN
```

說明：

```text
服務正在等待 Client 連線
```

常見服務：

* SSH
* FastAPI
* Prometheus
* Grafana
* Kubernetes API Server

---

### ESTABLISHED

```text
ESTAB
```

說明：

```text
TCP 連線已建立
```

範例：

```text
10.140.0.2:22
↓
124.218.x.x
```

代表：

* 使用者已透過 SSH 連線到 VM

---

### TIME-WAIT

```text
TIME-WAIT
```

說明：

```text
TCP 連線已結束
但 Kernel 暫時保留連線資訊
```

目的：

* 避免舊封包影響新連線
* 確保 TCP 正確關閉

---

### SYN-SENT

```text
SYN-SENT
```

說明：

```text
Client 已送出 TCP SYN 封包，

正在等待 Server 回應。
```

流程：

```text
Client
↓ SYN
Server
```

若長時間停留在：

```text
SYN-SENT
```

可能代表：

* Server 未啟動
* Firewall 阻擋
* Network Routing 問題

---

### SYN-RECV

```text
SYN-RECV
```

說明：

```text
Server 已收到 SYN，

並回覆 SYN-ACK，

等待 Client 回覆 ACK。
```

流程：

```text
Client
↓ SYN

Server
↓ SYN-ACK

等待 ACK
```

大量 SYN-RECV 可能代表：

* SYN Flood Attack
* Client 異常中斷
* 網路異常

---

### CLOSE-WAIT

```text
CLOSE-WAIT
```

說明：

```text
對方已關閉連線，

但本地程式尚未關閉 Socket。
```

大量 CLOSE-WAIT 通常代表：

```text
Application Bug
```

例如：

* Socket 未正確關閉
* Connection Leak

---

### FIN-WAIT

```text
FIN-WAIT-1
FIN-WAIT-2
```

說明：

```text
本地端已準備關閉 TCP Connection，

等待對方回應。
```

---

## TCP Three-Way Handshake

TCP 建立連線流程：

```text
Client
↓ SYN

Server
↓ SYN-ACK

Client
↓ ACK

Connection Established
```

建立完成後：

```text
ESTABLISHED
```

---

## TCP Four-Way Close

TCP 關閉流程：

```text
Client
↓ FIN

Server
↓ ACK

Server
↓ FIN

Client
↓ ACK

TIME-WAIT
```

因此：

```text
TIME-WAIT
```

是正常現象。

並不代表系統異常。

---

## 常見排障指令

查看監聽 Port：

```bash
ss -tulnp
```

查看已建立連線：

```bash
ss -ntp
```

查看特定 Port：

```bash
ss -tulnp | grep 8000
```

查看 DNS 是否正常：

```bash
nslookup google.com
```

或：

```bash
dig google.com
```

查看網路連通性：

```bash
ping <IP>
```

查看路由路徑：

```bash
traceroute <IP>
```

---

## Kubernetes 關聯

後續進入 Kubernetes 後：

常見排障流程：

```text
Pod Running
↓
Service
↓
Endpoints
↓
Ingress
↓
Application
```

若 Service 無法存取：

仍應先確認：

```text
Process
↓
Listen Port
↓
TCP Connection
```

再往 Kubernetes Layer 排查。

```
```


## 實際觀察

執行：

```bash
curl http://localhost:8000
```

後可看到：

```text
127.0.0.1:8000
TIME-WAIT
```

代表：

* HTTP Request 已完成
* TCP Connection 已正常關閉

---

## SRE 排錯流程

當服務無法存取時：

### Step 1

確認 Process 是否存在

```bash
ps aux
```

---

### Step 2

確認 Port 是否監聽

```bash
ss -tulnp
```

---

### Step 3

確認本機是否可連線

```bash
curl localhost:PORT
```

---

### Step 4

確認 Firewall 或 Cloud Network

例如：

* GCP Firewall
* Security Group
* Kubernetes Network Policy

---

## 與未來專案的關聯

後續會使用：

* FastAPI
* Prometheus
* Grafana
* vLLM
* ArgoCD

排查流程皆相同：

```text
Process
↓
Listen Port
↓
curl localhost
↓
Network
↓
Application
```

---

## 重點整理

常用指令：

```bash
ss -tulnp
ss -tan
curl
```

重要 TCP State：

* LISTEN
* ESTABLISHED
* TIME-WAIT

---

## 結論

Network Analysis 是 SRE 與 AI Infrastructure Engineer 的核心能力。

當服務異常時，應優先確認：

* Process
* Port
* TCP Connection
* Network Connectivity

而非直接判斷為應用程式問題。

