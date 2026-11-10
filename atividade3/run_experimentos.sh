#!/bin/bash
ITERACOES=${ITERACOES:-20000000}
IMAGEM="python:3.12-slim"
OUTPUT="resultados.csv"

echo "condicao,repeticao,iteracoes,checksum,wall_time,cpu_time,cpu_max,mem_max,mem_peak,pids_max" > $OUTPUT

for rep in 1 2 3; do
    for cond in "C1" "C2"; do
        if [ "$cond" == "C1" ]; then CPUS="0.5"; else CPUS="1.0"; fi
        
        echo "Executando $cond (Repetição $rep) com quota de $CPUS CPU..."
        RESULTADO=$(docker run --rm -e ITERACOES=$ITERACOES --cpus="$CPUS" --memory="256m" --memory-swap="256m" --pids-limit="64" -v "$PWD:/app" -w /app $IMAGEM python carga_cpu.py | grep "^RES,")
        
        VALORES=$(echo $RESULTADO | sed 's/^RES,//')
        echo "$cond,$rep,$VALORES" >> $OUTPUT
    done
done
echo "Experimentos concluídos! Dados guardados em $OUTPUT."
