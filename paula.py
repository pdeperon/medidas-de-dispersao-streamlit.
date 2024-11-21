import streamlit as st
import statistics 
import math

st.title("Medidas de Dispersão")

if "valores" not in st.session_state:
    st.session_state.valores = []

with st.form("form_medidas"):
    st.subheader("Calcular Medidas de Dispersão")
    valor = st.number_input("Digite um valor: ",min_value=0.0, step=0.01, format="%.2f")
    enviado = st.form_submit_button("Adicionar Valor")

if enviado:
    if not isinstance(valor, (int, float)):
        st.error("Entrada inválida! Insira apenas números.")
    else:
        st.session_state.valores.append(valor)  
        st.success("Valor Adicionado com Sucesso!!")

    st.write("Valores adicionados:", st.session_state.valores)

if len(st.session_state.valores) < 2:
    st.error("Adicione pelo menos dois valores para calcular as medidas de dispersão!")
else:
    if st.button("Calcular Média"):
         media = float(sum(st.session_state.valores) / len(st.session_state.valores))
         st.write("A média é a soma de todos os valores de um conjunto de dados dividida pelo número total de valores.")
         st.write(f"A média dos valores é {media}")

    elif st.button("Calcular amplitude"):
        amplitude = max(st.session_state.valores) - min(st.session_state.valores)
        st.write("A amplitude é a diferença entre o maior e o menor valor de um conjunto de dados. Mede a dispersão simples dos dados.")
        st.write(f"A amplitude dos valores foi de {amplitude}")

    elif st.button("Calcular a Variancia"):
        variancia_amostral = statistics.variance(st.session_state.valores)
        st.write("A variância mede o quão dispersos os valores estão em relação à média. É a média dos quadrados das diferenças entre cada valor e a média.")
        st.write(f"A variancia amostral foi de {variancia_amostral}")

    elif st.button("Calcular Desvio Padrão"):
         variancia_amostral = statistics.variance(st.session_state.valores)
         desvio_padrao = math.sqrt(variancia_amostral)
         st.write("O desvio padrão é a raiz quadrada da variância. Ele representa a dispersão dos valores em relação à média em unidades originais dos dados.")
         st.write(f"O desvio padrao foi de {desvio_padrao:.2f}")

    elif st.button("Calcular o Coeficiente de Variação"):
        media = float(sum(st.session_state.valores) / len(st.session_state.valores))
        variancia_amostral = statistics.variance(st.session_state.valores)
        desvio_padrao = math.sqrt(variancia_amostral)
        coeficiente_variacao = (desvio_padrao / media) * 100
        st.write("O coeficiente de variação mede a dispersão relativa de um conjunto de dados em relação à média. É expresso como uma porcentagem e permite comparar a variabilidade de diferentes conjuntos de dados, mesmo que tenham médias diferentes.")
        st.write(f"O coeficiente de variação é de {coeficiente_variacao:.2f} %")
   
    if st.button("Exibir Resultados"):
        media = float(sum(st.session_state.valores) / len(st.session_state.valores))
        amplitude = max(st.session_state.valores) - min(st.session_state.valores)
        variancia_amostral = statistics.variance(st.session_state.valores)
        desvio_padrao = math.sqrt(variancia_amostral)
        coeficiente_variacao = (desvio_padrao / media) * 100

        st.subheader("Resultados Finais")
        st.write(f"A média dos valores é {media}")
        st.write(f"A amplitude dos valores foi de {amplitude}")
        st.write(f"A variância foi de {variancia_amostral}")
        st.write(f"O desvio padrão foi de {desvio_padrao:.2f}")
        st.write(f"O coeficiente de variação é de {coeficiente_variacao:.2f} %")

    elif st.button("Voltar e escolher outra opção"):
        st.session_state.opcao_calculo = None


