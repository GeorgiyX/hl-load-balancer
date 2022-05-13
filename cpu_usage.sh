#!/bin/bash

if [[ "$#" -ne 1 || $1 == "--help" ]]; then
    echo -e "Использование скрипта:"
    echo -e "./cpu_usage.sh <имя инстанса>"
    exit 0
fi

function send_cpu() {
  cpu="$[100-$(vmstat 1 2|tail -1|awk '{print $15}')]"
  echo "cpu_usage $cpu" | curl --data-binary @-  http://localhost:9091/metrics/job/cpu_usage/instance/$1
}

while sleep 1; do
  send_cpu $1
done
