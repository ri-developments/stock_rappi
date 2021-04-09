import streamlit as st
import sqlalchemy
import pandas as pd
import plotly.express as px

#@st.cache
def existencias_02():

    direccion_servidor = '169.55.96.120'
    nombre_bd = 'UnoEE_Scotchland_Real'
    nombre_usuario = 'sco'
    password = 'Sco$12$%'

    conn = sqlalchemy.create_engine(f"mssql+pyodbc://{nombre_usuario}:{password}@{direccion_servidor}:20446/{nombre_bd}")

    sql_acumulados='''
    select t132.f132_id_instalacion Instalacion
         ,t150mb.f150_descripcion Dec_Instalacion
         ,t120mi.f120_id Item
         ,t120mi.f120_referencia Ref
         ,t120mi.f120_descripcion Descripcion
         ,f400_cant_existencia_1 - f400_cant_salida_sin_conf_1 - f400_cant_comprometida_1 as Cant_Disponible
         ,t132.f132_mf_stock_segur_estatico stock_seguridad_esta,
           CASE WHEN (f400_cant_existencia_1 - f400_cant_salida_sin_conf_1 - f400_cant_comprometida_1)>t132.f132_mf_stock_segur_estatico then 'Disponible' else 'Agotado' END as Disponible  
    from t132_mc_items_instalacion as t132
    inner join t121_mc_items_extensiones t121mie on t132.f132_rowid_item_ext = t121mie.f121_rowid
    inner join t120_mc_items t120mi on t121mie.f121_rowid_item = t120mi.f120_rowid
    inner join t150_mc_bodegas t150mb on t150mb.f150_id_instalacion= t132.f132_id_instalacion  and t150mb.f150_id_cia=t132.f132_id_cia
    inner join t400_cm_existencia t400ce  on t121mie.f121_rowid = t400ce.f400_rowid_item_ext and t150mb.f150_rowid = t400ce.f400_rowid_bodega
    '''
    df_existencias = pd.read_sql(sql_acumulados, conn)
    print(df_existencias.head(2))
    return df_existencias


df_existencias = existencias_02()


def main():
    st.title('Reporte de agotados y disponibles')
    menu = df_existencias.Dec_Instalacion.unique()
    st.sidebar.title('STOCK RI')
    st.sidebar.latex('Desing\hspace{0.1 cm}by:')
    st.sidebar.latex('Diego\hspace{0.1 cm}Ramirez')
    st.sidebar.latex('Diego\hspace{0.1 cm}Betancourt')
    choice = st.sidebar.selectbox('Menu',menu)


    if choice == 'CALLE 122':
        st.subheader('SEDE CALLE 122')
        df = df_existencias.loc[(df_existencias.Dec_Instalacion=='CALLE 122') & (df_existencias.Cant_Disponible!=0)].sort_values(by='Cant_Disponible',ascending=True)
        st.dataframe(df)
        fig_01 = px.bar(x=df.Descripcion,y=df.Cant_Disponible,title=f"Disponible {choice}")
        st.plotly_chart(fig_01)
        fig_02 = px.histogram(df,x='Disponible')
        st.plotly_chart(fig_02)

    elif choice == 'TOBERIN':
        st.subheader('SEDE TOBERIN')
        df = df_existencias.loc[
            (df_existencias.Dec_Instalacion == 'TOBERIN') & (df_existencias.Cant_Disponible != 0)].sort_values(
            by='Cant_Disponible', ascending=True)
        st.dataframe(df)
        fig_01 = px.bar(x=df.Descripcion, y=df.Cant_Disponible, title=f"Disponible {choice}")
        st.plotly_chart(fig_01)
        fig_02 = px.histogram(df, x='Disponible')
        st.plotly_chart(fig_02)

    elif choice == 'CHICO':
        st.subheader('SEDE CHICO')
        df = df_existencias.loc[
            (df_existencias.Dec_Instalacion == 'CHICO') & (df_existencias.Cant_Disponible != 0)].sort_values(
            by='Cant_Disponible', ascending=True)
        st.dataframe(df)
        fig_01 = px.bar(x=df.Descripcion, y=df.Cant_Disponible, title=f"Disponible {choice}")
        st.plotly_chart(fig_01)
        fig_02 = px.histogram(df, x='Disponible')
        st.plotly_chart(fig_02)

    elif choice == 'TEUSAQUILLO':
        st.subheader('SEDE TEUSAQUILLO')
        df = df_existencias.loc[
            (df_existencias.Dec_Instalacion == 'TEUSAQUILLO') & (df_existencias.Cant_Disponible != 0)].sort_values(
            by='Cant_Disponible', ascending=True)
        st.dataframe(df)
        fig_01 = px.bar(x=df.Descripcion, y=df.Cant_Disponible, title=f"Disponible {choice}")
        st.plotly_chart(fig_01)
        fig_02 = px.histogram(df, x='Disponible')
        st.plotly_chart(fig_02)

    elif choice == 'MODELIA':
        st.subheader('SEDE MODELIA')
        df = df_existencias.loc[
            (df_existencias.Dec_Instalacion == 'MODELIA') & (df_existencias.Cant_Disponible != 0)].sort_values(
            by='Cant_Disponible', ascending=True)
        st.dataframe(df)
        fig_01 = px.bar(x=df.Descripcion, y=df.Cant_Disponible, title=f"Disponible {choice}")
        st.plotly_chart(fig_01)
        fig_02 = px.histogram(df, x='Disponible')
        st.plotly_chart(fig_02)

    elif choice ==  'SUBA':
        st.subheader('SEDE  SUBA')
        df = df_existencias.loc[
            (df_existencias.Dec_Instalacion == 'SUBA') & (df_existencias.Cant_Disponible != 0)].sort_values(
            by='Cant_Disponible', ascending=True)
        st.dataframe(df)
        fig_01 = px.bar(x=df.Descripcion, y=df.Cant_Disponible, title=f"Disponible {choice}")
        st.plotly_chart(fig_01)
        fig_02 = px.histogram(df, x='Disponible')
        st.plotly_chart(fig_02)

    elif choice == 'CIUDAD JARDIN CALI':
        st.subheader('SEDE CIUDAD JARDIN CALI')
        df = df_existencias.loc[
            (df_existencias.Dec_Instalacion == 'CIUDAD JARDIN CALI') & (df_existencias.Cant_Disponible != 0)].sort_values(
            by='Cant_Disponible', ascending=True)
        st.dataframe(df)
        fig_01 = px.bar(x=df.Descripcion, y=df.Cant_Disponible, title=f"Disponible {choice}")
        st.plotly_chart(fig_01)
        fig_02 = px.histogram(df, x='Disponible')
        st.plotly_chart(fig_02)

    elif choice == 'SAN FERNANDO CALI':
        st.subheader('SEDE SAN FERNANDO CALI')
        df = df_existencias.loc[
            (df_existencias.Dec_Instalacion == 'SAN FERNANDO CALI') & (df_existencias.Cant_Disponible != 0)].sort_values(
            by='Cant_Disponible', ascending=True)
        st.dataframe(df)
        fig_01 = px.bar(x=df.Descripcion, y=df.Cant_Disponible, title=f"Disponible {choice}")
        st.plotly_chart(fig_01)
        fig_02 = px.histogram(df, x='Disponible')
        st.plotly_chart(fig_02)

    elif choice == 'POBLADO':
        st.subheader('SEDE POBLADO')
        df = df_existencias.loc[
            (df_existencias.Dec_Instalacion == 'POBLADO') & (df_existencias.Cant_Disponible != 0)].sort_values(
            by='Cant_Disponible', ascending=True)
        st.dataframe(df)
        fig_01 = px.bar(x=df.Descripcion, y=df.Cant_Disponible, title=f"Disponible {choice}")
        st.plotly_chart(fig_01)
        fig_02 = px.histogram(df, x='Disponible')
        st.plotly_chart(fig_02)

    elif choice == 'LAURELES':
        st.subheader('SEDE LAURELES')
        df = df_existencias.loc[
            (df_existencias.Dec_Instalacion == 'LAURELES') & (df_existencias.Cant_Disponible != 0)].sort_values(
            by='Cant_Disponible', ascending=True)
        st.dataframe(df)
        fig_01 = px.bar(x=df.Descripcion, y=df.Cant_Disponible, title=f"Disponible {choice}")
        st.plotly_chart(fig_01)
        fig_02 = px.histogram(df, x='Disponible')
        st.plotly_chart(fig_02)

    elif choice == 'PEREIRA':
        st.subheader('SEDE PEREIRA')
        df = df_existencias.loc[
            (df_existencias.Dec_Instalacion == 'PEREIRA') & (df_existencias.Cant_Disponible != 0)].sort_values(
            by='Cant_Disponible', ascending=True)
        st.dataframe(df)
        fig_01 = px.bar(x=df.Descripcion, y=df.Cant_Disponible, title=f"Disponible {choice}")
        st.plotly_chart(fig_01)
        fig_02 = px.histogram(df, x='Disponible')
        st.plotly_chart(fig_02)

    elif choice == 'BODEGA PRODUCTO NO CONFORME':
        st.subheader('BODEGA PRODUCTO NO CONFORME')
        df = df_existencias.loc[
            (df_existencias.Dec_Instalacion == 'BODEGA PRODUCTO NO CONFORME') & (df_existencias.Cant_Disponible != 0)].sort_values(
            by='Cant_Disponible', ascending=True)
        st.dataframe(df)
        fig_01 = px.bar(x=df.Descripcion, y=df.Cant_Disponible, title=f"Disponible {choice}")
        st.plotly_chart(fig_01)
        fig_02 = px.histogram(df, x='Disponible')
        st.plotly_chart(fig_02)

    elif choice == 'OFICINA PRINCIPAL':
        st.subheader('OFICINA PRINCIPAL')
        df = df_existencias.loc[
            (df_existencias.Dec_Instalacion == 'OFICINA PRINCIPAL') & (df_existencias.Cant_Disponible != 0)].sort_values(
            by='Cant_Disponible', ascending=True)
        st.dataframe(df)
        fig_01 = px.bar(x=df.Descripcion, y=df.Cant_Disponible, title=f"Disponible {choice}")
        st.plotly_chart(fig_01)
        fig_02 = px.histogram(df, x='Disponible')
        st.plotly_chart(fig_02)

    elif choice == 'BODEGA CALLCENTER':
        st.subheader('BODEGA CALLCENTER')
        df = df_existencias.loc[
            (df_existencias.Dec_Instalacion == 'BODEGA CALLCENTER') & (df_existencias.Cant_Disponible != 0)].sort_values(
            by='Cant_Disponible', ascending=True)
        st.dataframe(df)
        fig_01 = px.bar(x=df.Descripcion, y=df.Cant_Disponible, title=f"Disponible {choice}")
        st.plotly_chart(fig_01)
        fig_02 = px.histogram(df, x='Disponible')
        st.plotly_chart(fig_02)

    elif choice == 'BODEGA INSTITUCIONAL':
        st.subheader('BODEGA INSTITUCIONAL')
        df = df_existencias.loc[
            (df_existencias.Dec_Instalacion == 'BODEGA INSTITUCIONAL') & (df_existencias.Cant_Disponible != 0)].sort_values(
            by='Cant_Disponible', ascending=True)
        st.dataframe(df)
        fig_01 = px.bar(x=df.Descripcion, y=df.Cant_Disponible, title=f"Disponible {choice}")
        st.plotly_chart(fig_01)
        fig_02 = px.histogram(df, x='Disponible')
        st.plotly_chart(fig_02)

    elif choice == 'LA CAMPIÑA':
        st.subheader('SEDE LA CAMPIÑA')
        df = df_existencias.loc[
            (df_existencias.Dec_Instalacion == 'LA CAMPIÑA') & (df_existencias.Cant_Disponible != 0)].sort_values(
            by='Cant_Disponible', ascending=True)
        st.dataframe(df)
        fig_01 = px.bar(x=df.Descripcion, y=df.Cant_Disponible, title=f"Disponible {choice}")
        st.plotly_chart(fig_01)
        fig_02 = px.histogram(df, x='Disponible')
        st.plotly_chart(fig_02)

    elif choice == 'FULFILLMENT BY REPUBLICA':
        st.subheader('SEDE FULFILLMENT BY REPUBLICA')
        df = df_existencias.loc[
            (df_existencias.Dec_Instalacion == 'FULFILLMENT BY REPUBLICA') & (df_existencias.Cant_Disponible != 0)].sort_values(
            by='Cant_Disponible', ascending=True)
        st.dataframe(df)
        fig_01 = px.bar(x=df.Descripcion, y=df.Cant_Disponible, title=f"Disponible {choice}")
        st.plotly_chart(fig_01)
        fig_02 = px.histogram(df, x='Disponible')
        st.plotly_chart(fig_02)


if __name__ == '__main__':
    main()

