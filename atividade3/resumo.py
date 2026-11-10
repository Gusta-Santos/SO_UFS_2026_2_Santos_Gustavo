import pandas as pd
import matplotlib.pyplot as plt

try:
    df = pd.read_csv('resultados.csv')
    df['trabalho_por_segundo'] = df['iteracoes'] / df['wall_time']

    resumo = df.groupby('condicao')['trabalho_por_segundo'].agg(['median', 'var']).reset_index()
    print("\n=== Resumo: Trabalho Concluído por Segundo ===")
    print(resumo.to_string(index=False))

    plt.figure(figsize=(8, 6))
    plt.bar(resumo['condicao'], resumo['median'], yerr=resumo['var']**0.5, capsize=5, color=['skyblue', 'salmon'])
    plt.title('Mediana de Trabalho por Segundo (C1 vs C2)')
    plt.ylabel('Trabalho / Segundo')
    plt.xlabel('Condição (C1=0.5 CPU, C2=1.0 CPU)')
    plt.savefig('grafico_comparativo.png')
    print("\nGráfico guardado como 'grafico_comparativo.png'")
except Exception as e:
    print(f"Erro ao gerar resumo: {e}")
