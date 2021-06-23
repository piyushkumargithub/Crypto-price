import time
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import numpy as np
from matplotlib.animation import FuncAnimation
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()

# list includes overwhelming amount of coins 

# options=list()
# for coins in cg.get_coins_list():
#     options.append(coins["symbol"])

# well known coins

from second_part import getData
import plotly.graph_objects as go








#part 2 end 









def add_coin(coin):
    
    # def animate(i,coin,x_vals=[],y_vals=[]):
    #     value=format(cg.get_price(ids=coin,vs_currencies='inr')[coin]['inr'],'.2f')
    #     currenttime=pd.to_datetime(time.ctime()[11:19])
    #     if len(x_vals)>=100:
    #         x_vals.pop(0)
    #         y_vals.pop(0)
    #     x_vals.append(currenttime)
    #     y_vals.append(value)
        
    
    #     plt.cla()
    #     plt.plot(x_vals,y_vals)

        
    if coin!="Select a coin from this drop down list":
        st.markdown("## Value of {} : {:.2f} INR".format(coin, cg.get_price(coin , vs_currencies='inr')[coin]["inr"] ))
        last_rows=( cg.get_price(coin , vs_currencies='inr')[coin]["inr"])
        cc="chart"+coin
        cc= st.line_chart([last_rows])
        cc.x

        while True:
            new_rows = cg.get_price(coin , vs_currencies='inr')[coin]["inr"]
            
            cc.add_rows([new_rows])    
            time.sleep(10)


def main():
        st.title("Crypto")
        choice = st.selectbox("How to fetch price?",options=["Historical price","Live price"])
        if (choice=="Live price"):
            options=["bitcoin" , "nem" , "nano" , "ethereum" ,"chiliz"]

            coin = st.selectbox( label = "choose crypto coin" , options = options ,index=0)
            if st.button("Show live pricing"):
                st.markdown("## Zoom in/out or drag to adjust price frame")
                add_coin(coin)


        elif(choice=="Historical price"):
            #Part 2
            options = ["BTC" , "LTC" , "ETH" ]
            CRYPTO = st.selectbox( label = "choose crypto coin" , options = options ,index=0)
            CURRENCY = 'INR'

            if st.button("Show Historical pricing"):
                crypto_data = getData(CRYPTO,CURRENCY)

                # Candlestick
                fig = go.Figure(
                    data = [
                        go.Candlestick(
                            x = crypto_data.index,
                            open = crypto_data.Open,
                            high = crypto_data.High,
                            low = crypto_data.Low,
                            close = crypto_data.Close
                        ),
                        go.Scatter(
                            x = crypto_data.index, 
                            y = crypto_data.Close.rolling(window=20).mean(),
                            mode = 'lines', 
                            name = '20SMA',
                            line = {'color': '#ff006a'}
                        ),
                        go.Scatter(
                            x = crypto_data.index, 
                            y = crypto_data.Close.rolling(window=50).mean(),
                            mode = 'lines', 
                            name = '50SMA',
                            line = {'color': '#1900ff'}
                        )
                    ]
                )
                fig.update_layout(
                title = f'The Candlestick graph for {CRYPTO}',
                xaxis_title = 'Date',
                yaxis_title = f'Price ({CURRENCY})',
                xaxis_rangeslider_visible = False
                )
                fig.update_yaxes(tickprefix='₹')

                st.plotly_chart(fig)


if __name__=='__main__':
    main()



