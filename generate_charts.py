import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    'figure.facecolor': 'white',
    'axes.facecolor': 'white',
    'font.family': 'sans-serif',
    'font.size': 11,
    'axes.titlesize': 13,
    'axes.titleweight': 'bold',
})

channels = ['Email', 'Google Search', 'YouTube', 'Instagram', 'Contextual\nDisplay']
channels_compact = ['Email', 'Google\nSearch', 'YouTube', 'Instagram', 'Contextual\nDisplay']

# --- Chart 1: Attribution Comparison Across Models ---
last_touch = [103145.35, 369960.84, 139685.87, 321662.74, 544429.67]
first_touch = [471100.59, 73610.06, 166965.93, 101525.20, 665682.69]
linear = [247006.00, 184189.76, 169430.22, 202724.22, 675534.27]
itt = [111348.01, 58453.04, 114700.14, 73037.20, 27950.07]

x = np.arange(len(channels))
width = 0.2

fig, ax = plt.subplots(figsize=(10, 5))
bars1 = ax.bar(x - 1.5*width, [v/1000 for v in last_touch], width, label='Last-Touch', color='#4C72B0')
bars2 = ax.bar(x - 0.5*width, [v/1000 for v in first_touch], width, label='First-Touch', color='#55A868')
bars3 = ax.bar(x + 0.5*width, [v/1000 for v in linear], width, label='Linear', color='#C44E52')
bars4 = ax.bar(x + 1.5*width, [v/1000 for v in itt], width, label='Incremental (ITT)', color='#8172B2')

ax.set_ylabel('Attributed Sales ($K)')
ax.set_title('Sales Attribution by Channel Across Models')
ax.set_xticks(x)
ax.set_xticklabels(channels_compact)
ax.legend(loc='upper right')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig("outputs/attribution_comparison_by_model.png", dpi=300)
plt.close()

# --- Chart 2: ROI Comparison ---
itt_roi = [63.12, -93.69, 47.47, 45.51, -33.42]
last_touch_roi = [51.10, -60.04, 79.59, 540.84, 1196.84]
first_touch_roi = [590.13, -92.05, 114.67, 102.27, 1485.66]
linear_roi = [261.85, -80.11, 117.84, 303.88, 1509.13]

fig, ax = plt.subplots(figsize=(10, 5))
bars1 = ax.bar(x - 1.5*width, last_touch_roi, width, label='Last-Touch', color='#4C72B0')
bars2 = ax.bar(x - 0.5*width, first_touch_roi, width, label='First-Touch', color='#55A868')
bars3 = ax.bar(x + 0.5*width, linear_roi, width, label='Linear', color='#C44E52')
bars4 = ax.bar(x + 1.5*width, itt_roi, width, label='Incremental (ITT)', color='#8172B2')

ax.set_ylabel('ROI (%)')
ax.set_title('Channel ROI: Naive Attribution vs. Incremental Analysis')
ax.set_xticks(x)
ax.set_xticklabels(channels_compact)
ax.legend(loc='upper right')
ax.axhline(y=0, color='black', linewidth=0.8, linestyle='-')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig("outputs/roi_comparison_by_model.png", dpi=300)
plt.close()

# --- Chart 3: Incremental Sales vs. Cost by Channel ---
incremental = [111348.01, 58453.04, 114700.14, 73037.20, 27950.07]
costs = [68262.36, 925906.40, 77778.40, 50193.60, 41981.36]

fig, ax = plt.subplots(figsize=(9, 5))
x2 = np.arange(len(channels))
width2 = 0.35
bars1 = ax.bar(x2 - width2/2, [v/1000 for v in incremental], width2, label='Incremental Sales', color='#55A868')
bars2 = ax.bar(x2 + width2/2, [v/1000 for v in costs], width2, label='Channel Cost', color='#C44E52')

ax.set_ylabel('Amount ($K)')
ax.set_title('Incremental Sales vs. Channel Cost')
ax.set_xticks(x2)
ax.set_xticklabels(channels_compact)
ax.legend()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig("outputs/incremental_sales_vs_cost.png", dpi=300)
plt.close()

# --- Chart 4: Total Attributed Sales - Naive vs Incremental ---
naive_total = 1478884
itt_total = 385488
organic_itt = 1355259
organic_naive = 261863

fig, ax = plt.subplots(figsize=(7, 5))
categories = ['Incremental\n(Experimental)', 'Naive Attribution\n(Avg. of 3 Models)']
attributed = [itt_total/1000, naive_total/1000]
organic = [organic_itt/1000, organic_naive/1000]

bars1 = ax.bar(categories, attributed, color='#4C72B0', label='Attributed to Channels')
bars2 = ax.bar(categories, organic, bottom=attributed, color='#CCB974', label='Organic (Unattributed)')

ax.set_ylabel('Sales ($K)')
ax.set_title('Channel-Attributed vs. Organic Sales')
ax.legend()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig("outputs/attributed_vs_organic_sales.png", dpi=300)
plt.close()

print("Charts saved to outputs/")
