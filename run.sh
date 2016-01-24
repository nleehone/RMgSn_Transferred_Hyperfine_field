#!/bin/sh

# NdMgSn
python3 RMgSn_Transferred_Bhf.py config/NdMgSn_4K.py results/NdMgSn_4K.dat
python3 RMgSn_Transferred_Bhf_plot.py results/NdMgSn_4K.dat plots/NdMgSn_4K.png 0.1

# HoMgSn
python3 RMgSn_Transferred_Bhf.py config/HoMgSn_4K.py results/HoMgSn_4K.dat
python3 RMgSn_Transferred_Bhf_plot.py results/HoMgSn_4K.dat plots/HoMgSn_4K.png

# DyMgSn
# WARNING: TAKES LONG TIME TO RUN
python3 RMgSn_Transferred_Bhf.py config/DyMgSn_4K.py results/DyMgSn_4K.dat
python3 RMgSn_Transferred_Bhf_plot.py results/DyMgSn_4K.dat plots/DyMgSn_4K.png
python3 RMgSn_Transferred_Bhf.py config/DyMgSn_14p8K.py results/DyMgSn_14p8K.dat
python3 RMgSn_Transferred_Bhf_plot.py results/DyMgSn_14p8K.dat plots/DyMgSn_14p8K.png

# TbMgSn
python3 RMgSn_Transferred_Bhf.py config/TbMgSn_sine_4K.py results/TbMgSn_sine_4K.dat
python3 RMgSn_Transferred_Bhf_plot.py results/TbMgSn_sine_4K.dat plots/TbMgSn_sine_4K.png
python3 RMgSn_Transferred_Bhf.py config/TbMgSn_cycloidal_4K.py results/TbMgSn_cycloidal_4K.dat
python3 RMgSn_Transferred_Bhf_plot.py results/TbMgSn_cycloidal_4K.dat plots/TbMgSn_cycloidal_4K.png 0.1

# ErMgSn
python3 RMgSn_Transferred_Bhf.py config/ErMgSn_k0p8_4K.py results/ErMgSn_k0p8_4K.dat
python3 RMgSn_Transferred_Bhf_plot.py results/ErMgSn_k0p8_4K.dat plots/ErMgSn_k0p8_4K.png
python3 RMgSn_Transferred_Bhf.py config/ErMgSn_k0p801_4K.py results/ErMgSn_k0p801_4K.dat
python3 RMgSn_Transferred_Bhf_plot.py results/ErMgSn_k0p801_4K.dat plots/ErMgSn_k0p801_4K.png

