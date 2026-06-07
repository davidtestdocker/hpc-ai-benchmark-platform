# VMSTAT and IOSTAT Analysis

## Objective

Learn how to identify CPU bottlenecks and Disk IO bottlenecks using Linux performance tools.

---

## VMSTAT

### Command

```bash
vmstat 1 5
```

### Key Metrics

| Metric | Description       |
| ------ | ----------------- |
| r      | Run Queue         |
| b      | Blocked Processes |
| id     | CPU Idle          |
| wa     | IO Wait           |

---

### Normal System

Result:

```text
r=0
b=0
id=100
wa=0
```

Observation:

* CPU idle
* No process waiting for CPU
* No IO bottleneck

---

### CPU Stress Test

Command:

```bash
yes > /dev/null &
yes > /dev/null &
yes > /dev/null &
yes > /dev/null &
```

Result:

```text
r=4
id=0
wa=0
```

Observation:

* All CPU cores utilized
* No IO wait
* CPU became bottleneck

---

## IOSTAT

### Command

```bash
iostat -x 1 5
```

### Key Metrics

| Metric | Description                 |
| ------ | --------------------------- |
| r/s    | Read Operations Per Second  |
| w/s    | Write Operations Per Second |
| await  | Average IO Latency          |
| %util  | Disk Utilization            |

---

### Disk Write Test

Command:

```bash
dd if=/dev/zero of=testfile2 bs=1M count=8192 oflag=direct status=progress
```

Result:

```text
iowait = 23.31%
util = 92.60%
```

Observation:

* Disk heavily utilized
* CPU spent significant time waiting for IO
* Storage became bottleneck

---

## Key Learning

High CPU Usage does not always mean CPU bottleneck.

Potential bottlenecks include:

* CPU
* Memory
* Disk IO
* Network

Performance analysis requires multiple tools:

* top
* vmstat
* iostat
* sar

---

## Conclusion

CPU metrics alone are insufficient for performance troubleshooting.

Disk utilization and IO wait must be analyzed together to identify system bottlenecks.

