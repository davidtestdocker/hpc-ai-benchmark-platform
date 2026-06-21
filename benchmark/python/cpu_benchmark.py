#!/usr/bin/env python3

import time
import os
import json

class CPUBenchmark:

    def run(self, iterations: int = 10_000_000) -> dict:
        start_time = time.time()

        result = 0

        for i in range(iterations):
            result += i * i

        end_time = time.time()

        duration = end_time - start_time
        operations_per_second = round(iterations / duration, 2)

        return {
            "benchmark": "cpu",
            "hostname": os.uname().nodename,
            "iterations": iterations,
            "duration_seconds": round(duration, 4),
            "operations_per_second": operations_per_second,
            "result": result
        }


benchmark = CPUBenchmark()
benchmark_result = benchmark.run()

with open( "/root/hpc-ai-benchmark-platform/reports/cpu_benchmark.json","w") as file:
    json.dump(benchmark_result, file, indent=4)
print(json.dumps(benchmark_result, indent=4))
