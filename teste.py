import streamlit as st

# Título do Site
st.title('📊 Validador de Zoneamento')
st.markdown('Verifique se o seu projeto atende às normas do Plano Diretor.')

# Criando colunas para o site ficar bonito
col1, col2 = st.columns(2)

with col1:
    st.header('Terreno')
    larg_t = st.number_input('Largura do terreno (m):', min_value=0.0, step=1.0)
    prof_t = st.number_input('Profundidade do terreno (m):', min_value=0.0, step=1.0)

with col2:
    st.header('Garagem')
    larg_g = st.number_input('Largura da garagem (m):', min_value=0.0, step=1.0)
    prof_g = st.number_input('Profundidade da garagem (m):', min_value=0.0, step=1.0)

# Cálculos
area_terreno = larg_t * prof_t
area_garagem = larg_g * prof_g

# Evita erro de divisão por zero se os campos estiverem vazios
if area_terreno > 0:
    percentual = (area_garagem / area_terreno) * 100
else:
    percentual = 0.0

st.divider() # Aqueles tracinhos que você gostou!

# Seleção da Zona
zona = st.selectbox('Selecione a Zona de Localização:', 
                    ['N - Norte', 'S - Sul', 'L - Leste', 'O - Oeste'])
# Pega apenas a primeira letra para manter sua lógica
zona_letra = zona[0] 

# Exibição dos Resultados
st.subheader('Resumo do Projeto')
st.write(f'**Área do Terreno:** {area_terreno:.2f} m²')
st.write(f'**Área da Garagem:** {area_garagem:.2f} m²')
st.metric('Percentual de Ocupação', f'{percentual:.2f} %')

# Lógica de Validação (Igual à sua!)
if area_terreno > 0:
    atende = False
    
    if zona_letra == 'N' and percentual <= 25:
        atende = True
    elif zona_letra == 'S' and percentual <= 40:
        atende = True
    elif (zona_letra == 'L' or zona_letra == 'O') and percentual <= 30:
        atende = True

    if atende:
        st.success('✅ Projeto atende norma de zoneamento do plano diretor!')
    else:
        st.error('❌ Infelizmente o seu Projeto NÃO atendeu as normas.')
