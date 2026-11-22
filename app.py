from pathlib import Path
import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(page_title='Laptop Store Analytics', page_icon='💻', layout='wide')
ROOT = Path(__file__).parent
sales = pd.read_csv(ROOT/'sales.csv', parse_dates=['date'])
inventory = pd.read_csv(ROOT/'inventory.csv')
st.title('Laptop Store | Sales & Inventory')
st.caption('Interactive portfolio demo • Synthetic data • Currency: EGP')
brands = st.sidebar.multiselect('Brands', sorted(sales.brand.unique()), default=sorted(sales.brand.unique()))
period = st.sidebar.date_input('Date range', (sales.date.min().date(), sales.date.max().date()))
if len(period) != 2:
    st.info('Select a start and end date.'); st.stop()
d = sales[sales.brand.isin(brands) & sales.date.between(pd.Timestamp(period[0]), pd.Timestamp(period[1]))].copy()
d['revenue'] = d.quantity*d.unit_price
d['gross_profit'] = d.quantity*(d.unit_price-d.unit_cost)
cols = st.columns(4)
cols[0].metric('Revenue', f'EGP {d.revenue.sum():,.0f}')
cols[1].metric('Gross profit', f'EGP {d.gross_profit.sum():,.0f}')
cols[2].metric('Units sold', f'{d.quantity.sum():,}')
cols[3].metric('Transactions', f'{len(d):,}')
if not d.empty:
    d['month'] = d.date.dt.to_period('M').astype(str)
    a,b = st.columns(2)
    a.plotly_chart(px.line(d.groupby('month',as_index=False).revenue.sum(), x='month',y='revenue',markers=True,title='Monthly revenue'),use_container_width=True)
    b.plotly_chart(px.bar(d.groupby('brand',as_index=False).revenue.sum().sort_values('revenue',ascending=False),x='brand',y='revenue',title='Revenue by brand'),use_container_width=True)
    st.plotly_chart(px.bar(d.groupby('model',as_index=False).quantity.sum().nlargest(10,'quantity'),x='quantity',y='model',orientation='h',title='Top models by units sold'),use_container_width=True)
else: st.info('No sales match these filters.')
st.subheader('Current inventory snapshot')
i=inventory[inventory.brand.isin(brands)].copy()
i['status']=i.stock_on_hand.le(i.reorder_level).map({True:'Reorder',False:'In stock'})
st.dataframe(i,hide_index=True,use_container_width=True)
st.subheader('Sales transactions')
st.dataframe(d,hide_index=True,use_container_width=True)
st.download_button('Download filtered sales',d.to_csv(index=False),'filtered_sales.csv','text/csv')
