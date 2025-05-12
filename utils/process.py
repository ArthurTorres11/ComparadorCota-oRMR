import streamlit as st
import pandas as pd
import io

def process_files():
    st.markdown("### 🔢 Selecione o número de cotações recebidas")
    qtd = st.selectbox("Quantas cotações você recebeu?", [1, 2, 3, 4, 5])

    if "avancar" not in st.session_state:
        st.session_state.avancar = False

    if not st.session_state.avancar:
        if st.button("Avançar para envio das cotações"):
            st.session_state.avancar = True
        return

    uploads = []
    st.markdown("### 📤 Upload dos Arquivos de Cotação")

    for i in range(qtd):
        col1, col2 = st.columns([1.5, 3])
        with col1:
            empresa = st.text_input(f"Nome da empresa {i+1}", key=f"empresa_{i}")
        with col2:
            file = st.file_uploader(f"Planilha da {empresa or f'Empresa {i+1}'}", type=["xlsx"], key=f"file_{i}")
        if file and empresa:
            uploads.append((empresa, file))

    if len(uploads) < qtd:
        st.info("Preencha todos os nomes e envie todos os arquivos para continuar.")
        return

    try:
        comparador = pd.DataFrame()

        for empresa, arquivo in uploads:
            df = pd.read_excel(arquivo, header=7, usecols=[1, 2, 3, 4])
            df.columns = ["Quantidade", "Peça", "Preço", "Marca"]

            df["Preço"] = (
                df["Preço"]
                .astype(str)
                .str.replace("R\\$", "", regex=True)
                .str.replace(",", ".", regex=False)
                .str.strip()
            )
            df["Preço"] = pd.to_numeric(df["Preço"], errors="coerce")
            df["Peça"] = df["Peça"].astype(str).str.strip()
            df["Marca"] = df["Marca"].astype(str).str.strip()

            df = df[df["Peça"].notna() & (df["Preço"] > 0)]
            df["Empresa"] = empresa
            comparador = pd.concat([comparador, df], ignore_index=True)

        melhores = comparador.sort_values("Preço").groupby("Peça").first().reset_index()

        st.markdown("### ✅ Resultado com os Melhores Preços")
        st.dataframe(melhores[["Peça", "Empresa", "Preço", "Marca"]], use_container_width=True)

        towrite = io.BytesIO()
        melhores.to_excel(towrite, index=False, sheet_name="Melhores Preços")
        towrite.seek(0)
        st.download_button(
            "📥 Exportar Resultado para Excel",
            data=towrite,
            file_name="melhores_precos.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
    except Exception as e:
        st.error(f"Erro no processamento: {e}")