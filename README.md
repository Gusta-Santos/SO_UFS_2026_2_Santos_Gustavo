# SO_UFS_2026_2_Santos_Gustavo

## Link para o vídeo

## Link do modelo hugging face  
https://huggingface.co/microsoft/Phi-4-mini-instruct  
https://huggingface.co/bartowski/Phi-4-mini-instruct-GGUF

## Link do repositório original  
Foi utilizada a branch main do repositório original da trilha C  
https://github.com/tonykipkemboi/ollama_pdf_rag

## Como rodar a aplicação  
Para reproduzir os testes feitos nesse repositório em um ambiente Linux, o primeiro passo é garantir que o motor de inferência esteja instalado e operando corretamente. A instalação do Ollama deve ser feita utilizando o script oficial no terminal por meio do comando  
```
curl -fsSL [https://ollama.com/install.sh](https://ollama.com/install.sh) | sh
```
Com o serviço ativo, a obtenção dos modelos de IA ocorreu de duas formas. O modelo de linguagem principal, phi4-mini, foi adquirido de forma manual através do download do arquivo no formato GGUF diretamente do link do repositório no Hugging Face. E o modelo de vetorização nomic-embed-text foi exigido e acionado sob demanda pelo sistema durante a execução do projeto, no momento em que a aplicação precisou criar os embeddings. 

Para a camada de aplicação, deve-se navegar até o diretório principal do projeto e ativar o ambiente virtual isolado utilizando o comando  
```
source venv/bin/activate
```
Nesse momento, é importante realizar o download das dependências do projeto, executando o comando
```
pip install -r requirements.txt
```
Após isso, todas as bibliotecas Python necessárias, inclusive o pacote LangChain, serão baixadas e alocadas isoladamente, prevenindo conflitos no sistema operacional.  
Vale ressaltar que, devido a atualizações nas dependências, foi necessária uma intervenção manual no código fonte: utilizando o editor nano, o método obsoleto get_relevant_documents foi substituído por invoke no arquivo principal para restabelecer a busca no banco vetorial.  
Por fim, com as bibliotecas instaladas, o código ajustado e o motor de inferência em background, basta iniciar a interface gráfica executando o comando  
```
python3 run.py
```
O servidor Streamlit será inicializado, exibindo no terminal o endereço local (geralmente na porta 8501) que deve ser acessado via navegador para a submissão dos arquivos PDF e posterior monitoramento do consumo de CPU e memória.
