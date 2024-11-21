import streamlit as st
import statistics 
import math

st.title("Medidas de Dispersão")

if "valores" not in st.session_state:
    st.session_state.valores = []

with st.form("form_medidas"):
    st.subheader("Calcular Medidas de Dispersão")
    valor = st.number_input("Digite um valor: ",min_value=0.0, step=0.01)
    enviado = st.form_submit_button("Adicionar Valor")

if enviado:
    st.session_state.valores.append(valor)  
    st.success("Valor Adicionado com Sucesso!!")

    st.write("Valores adicionados:", st.session_state.valores)

if len(st.session_state.valores) < 2:
    st.error("Adicione pelo menos dois valores para calcular as medidas de dispersão!")
else:
    if st.button("Calcular Média"):
         media = float(sum(st.session_state.valores) / len(st.session_state.valores))
         st.write(f"A média dos valores é {media}")
    elif st.button("Calcular amplitude"):
        amplitude = max(st.session_state.valores) - min(st.session_state.valores)
        st.write(f"A amplitude dos valores foi de {amplitude}")
    elif st.button("Calcular a Variancia"):
        variancia_amostral = statistics.variance(st.session_state.valores)
        st.write(f"A variancia amostral foi de {variancia_amostral}")
    elif st.button("Calcular Desvio Padrao"):
         variancia_amostral = statistics.variance(st.session_state.valores)
         desvio_padrao = math.sqrt(variancia_amostral)
         st.write(f"O desvio padrao foi de {desvio_padrao}")
    elif st.button("Calcular o Coeficiente de Variacao"):
        media = float(sum(st.session_state.valores) / len(st.session_state.valores))
        variancia_amostral = statistics.variance(st.session_state.valores)
        desvio_padrao = math.sqrt(variancia_amostral)
        coeficiente_variacao = (desvio_padrao / media) * 100
        st.write(f"O coeficiente de variacao é de {coeficiente_variacao:.2f}")
   
    if st.button("Exibir Resultados"):
        media = float(sum(st.session_state.valores) / len(st.session_state.valores))
        amplitude = max(st.session_state.valores) - min(st.session_state.valores)
        variancia_pop = statistics.pvariance(st.session_state.valores)
        variancia_amostral = statistics.variance(st.session_state.valores)
        desvio_padrao = math.sqrt(variancia_pop)
        coeficiente_variacao = (desvio_padrao / media) * 100

        st.subheader("Resultados Finais")
        st.write(f"A média dos valores é {media}")
        st.write(f"A amplitude dos valores foi de {amplitude}")
        st.write(f"A variancia populacional foi de {variancia_pop}")
        st.write(f"A variancia amostral foi de {variancia_amostral}")
        st.write(f"O desvio padrao foi de {desvio_padrao}")
        st.write(f"O coeficiente de variacao é de {coeficiente_variacao:.2f}")

    elif st.button("Voltar e escolher outra opção"):
        st.session_state.opcao_calculo = None


