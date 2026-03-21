from src.data_loader import load_transactions

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from collections import defaultdict

df= load_transactions("data/transactions.xlsx")


df['from_address'] = df['from_address'].str.lower()
df['to_address'] = df['to_address'].str.lower()

df= df.dropna(subset=['from_address'])

# G= nx.DiGraph()

# for _, row in df.iterrows():
#     u= row['from_address']
#     v= row['to_address']
#     vol=row['transfer_volume']

#     if G.has_edge(u,v):
#         G[u][v]['count'] += 1
#         G[u][v]['sum_value'] += vol

#     else:
#         G.add_edge(u,v, count=1, sum_value=vol)


# out_deg= dict(G.out_degree())
# in_deg= dict(G.in_degree())

# top_senders= sorted(out_deg.items(), key=lambda x: x[1], reverse=True)[:10]
# top_receivers= sorted(in_deg.items(), key=lambda x: x[1], reverse=True)[:10]

# edges_count= sorted( G.edges(data=True), key=lambda x: x[2]['count'], reverse=True)[:10]

# components= list(nx.weakly_connected_components(G))
# sizes= sorted([len(c) for c in components], reverse=True)


# seen= set()
# ping_stats= []
# ping_pong_pairs= []
# for u,v in G.edges():
#     if G.has_edge(v,u):
#         pair= tuple(sorted((u,v)))
#         if pair not in seen:
#             seen.add(pair)
#             ping_pong_pairs.append(pair)

#             count_uv = G[u][v]['count']
#             count_vu = G[v][u]['count']
#             total = count_uv + count_vu
#             ping_stats.append((u, v, total))

#=========================================== GENERAL DATA ANALYSIS ========================================================
# print("Nodes:", G.number_of_nodes())
# print("Edges:", G.number_of_edges())

# print("Nodes:", G.number_of_nodes())
# print("Edges:", G.number_of_edges())

# print ("\nconnected components:", len(components))
# print("\nTop 10 component sizes:", sizes[:10])
# print("\nLargest component %:", round(100*sizes[0]/G.number_of_nodes(),2)) 

#print("\nTop ping-pong pairs by total transactions:")
#ping_stats = sorted(ping_stats, key=lambda x: x[2], reverse=True)
#for u, v, total in ping_stats[:30]:
#    print(u, "<->", v, "total tx:", total)

#print("\nNumber of ping-pong pairs:", len(ping_pong_pairs))

# print("\nTop 10 edges by transaction count:")
# for u,v, data in edges_count:
#     print(u, "->", v, "count=", data['count'], "sum_value=", data['sum_value'])

#print("\nTop 10 Senders:")
#for addr, deg in top_senders:
#    print(addr, deg)

# print("\nTop 10 Receivers:")
# for addr, deg in top_receivers:
#     print(addr, deg)

#============================================VISUALIZATION================================================================
sent_counts= df['from_address'].value_counts()  # number of transactions sent by each wallet

received_counts= df['to_address'].value_counts()  # number of transactions received by each wallet

# ---------------------------- Distribution of sending transactions per wallet -----------------------------

# categories1 = {
#     "1": ((sent_counts >= 1) & (sent_counts < 2)).sum(),
#     "2-5": ((sent_counts >= 2) & (sent_counts <= 5)).sum(),
#     "6-10": ((sent_counts >= 6) & (sent_counts <= 10)).sum(),
#     "11-50": ((sent_counts >= 11) & (sent_counts <= 50)).sum()
# }

# categories2 = {
#     "51-100": ((sent_counts >= 51) & (sent_counts <= 100)).sum(),
#     "100-1000": ((sent_counts >= 100) & (sent_counts <= 1000)).sum(),
#     "1000-10,000": ((sent_counts >= 1000) & (sent_counts <= 10000)).sum(),
#     "10,000+": (sent_counts > 10000).sum()
# }


# fig, axs= plt.subplots(1, 2, figsize=(20,6))
# axs[0].bar(categories1.keys(), categories1.values())
# axs[0].set_xlabel("Number of transactions")
# axs[0].set_ylabel("Number of wallets")
# axs[0].set_title("Distribution of transactions per wallet (1-50)")

# axs[1].bar(categories2.keys(), categories2.values())
# axs[1].set_xlabel("Number of transactions")
# axs[1].set_ylabel("Number of wallets")
# axs[1].set_title("Distribution of transactions per wallet (51+)")
# plt.show()

# ---------------------------- Distribution of receiving transactions per wallet -----------------------------

# categories1 = {
#     "1": ((received_counts >= 1) & (received_counts < 2)).sum(),
#     "2-5": ((received_counts >= 2) & (received_counts <= 5)).sum(),
#     "6-10": ((received_counts >= 6) & (received_counts <= 10)).sum(),
#     "11-20": ((received_counts >= 11) & (received_counts <= 20)).sum()
# }

# categories2 = {
#     "21-50": ((received_counts >= 21) & (received_counts <= 50)).sum(),
#     "51-100": ((received_counts >= 51) & (received_counts <= 100)).sum(),
#     "101-150": ((received_counts >= 101) & (received_counts <= 150)).sum(),
#     "151+": (received_counts > 151).sum()
# }


# fig, axs= plt.subplots(1, 2, figsize=(20,6))
# axs[0].bar(categories1.keys(), categories1.values())
# axs[0].set_xlabel("Number of transactions")
# axs[0].set_ylabel("Number of wallets")
# axs[0].set_title("Distribution of receiving transactions per wallet")

# axs[1].bar(categories2.keys(), categories2.values())
# axs[1].set_xlabel("Number of transactions")
# axs[1].set_ylabel("Number of wallets")
# axs[1].set_title("Distribution of receiving transactions per wallet")
# plt.show()

# ---------------------------- Distribution of both sending and receiving transactions per wallet -----------------------------


#-----LOW RANGES-----

# count_to_wallets = defaultdict(set)

# for wallet, count in sent_counts.items():
#     count_to_wallets[count].add(wallet)

# for wallet, count in received_counts.items():
#     count_to_wallets[count].add(wallet)

# union_dist = {count: len(wallets) for count, wallets in count_to_wallets.items()}

# union_dist = pd.Series(union_dist).sort_index()

# ranges = [
#     (1, 4),
#     (5, 10),
#     (11, 20),
#     (21, 50)
# ]

# fig, axs = plt.subplots(2, 2)
# axs = axs.flatten()

# for ax, (low, high) in zip(axs, ranges):
#     subset = union_dist[(union_dist.index >= low) & (union_dist.index <= high)]

#     ax.bar(subset.index, subset.values)
#     ax.set_title(f"Wallets with {low}-{high} Transactions")
#     ax.set_xlabel("Number of transactions")
#     ax.set_ylabel("Number of wallets")

# plt.tight_layout()
# plt.show()

#-----HIGH RANGES-----

# bin_ranges = [
#     (51, 100, 5),      # bins of width 5
#     (101, 500, 50),    # bins of width 50
#     (501, 1000, 100),  # bins of width 100
#     (1001, int(max(sent_counts.max(), received_counts.max())), 5000)
# ]

# fig, axs = plt.subplots(2, 2)
# axs = axs.flatten()

# for ax, (low, high, step) in zip(axs, bin_ranges):
#     labels = []
#     values = []

#     for start in range(low, high + 1, step):
#         end = min(start + step - 1, high)

#         sent_wallets = set(sent_counts[(sent_counts >= start) & (sent_counts <= end)].index)
#         received_wallets = set(received_counts[(received_counts >= start) & (received_counts <= end)].index)

#         wallets = sent_wallets | received_wallets

#         labels.append(f"{start}-{end}")
#         values.append(len(wallets))

#     ax.bar(labels, values)
#     ax.set_title(f"Wallets with {low}-{high} Transactions")
#     ax.set_xlabel("Transaction bin")
#     ax.set_ylabel("Number of wallets")
#     ax.tick_params(axis='x', rotation=45)

# plt.tight_layout()
# # plt.show()

#----------------------------- CDF of sending transactions per wallet -----------------------------

# # sort values
# data = np.sort(sent_counts.values)

# # cumulative fraction
# cdf = np.arange(1, len(data) + 1) / len(data)

# fig, axs = plt.subplots(1, 2, figsize=(10,6))

# # masks
# mask_1 = data <= 50
# mask_2 = data > 50

# # graph 1: 1-50 transactions
# axs[0].plot(data[mask_1], cdf[mask_1], linewidth=3)
# axs[0].set_xlabel("Number of transactions")
# axs[0].set_ylabel("Fraction of wallets")
# axs[0].set_title("CDF of Wallet Sending Activity (1-50)")
# axs[0].set_xlim(1, 50)

# # graph 2: 51+ transactions
# axs[1].plot(data[mask_2], cdf[mask_2], linewidth=3)
# axs[1].set_xlabel("Number of transactions")
# axs[1].set_ylabel("Fraction of wallets")
# axs[1].set_title("CDF of Wallet Sending Activity (51+)")
# axs[1].set_xlim(51, data.max())

# plt.tight_layout()
# plt.show()

#----------------------------- CDF of receiving transactions per wallet -----------------------------

# # sort values
# data = np.sort(received_counts.values)

# # cumulative fraction
# cdf = np.arange(1, len(data) + 1) / len(data)

# fig, axs = plt.subplots(1, 2, figsize=(10,6))

# # masks
# mask_1 = data <= 20
# mask_2 = data > 20

# # graph 1: 1-20 transactions
# axs[0].plot(data[mask_1], cdf[mask_1], linewidth=3)
# axs[0].set_xlabel("Number of transactions")
# axs[0].set_ylabel("Fraction of wallets")
# axs[0].set_title("CDF of Wallet receiving Activity")
# axs[0].set_xlim(1, 20)

# # graph 2: 21+ transactions
# axs[1].plot(data[mask_2], cdf[mask_2], linewidth=3)
# axs[1].set_xlabel("Number of transactions")
# axs[1].set_ylabel("Fraction of wallets")
# axs[1].set_title("CDF of Wallet receiving Activity")
# axs[1].set_xlim(21, data.max())

# plt.tight_layout()
# plt.show()

# ---------------------------- CDF of both sending and receiving transactions per wallet -----------------------------

# count_to_wallets = defaultdict(set)

# for wallet, count in sent_counts.items():
#     count_to_wallets[count].add(wallet)

# for wallet, count in received_counts.items():
#     count_to_wallets[count].add(wallet)

# union_dist = pd.Series({k: len(v) for k, v in count_to_wallets.items()})
# union_dist = union_dist.sort_index()

# cdf = union_dist.cumsum() / union_dist.sum()

# cdf_1 = cdf[cdf.index <= 10]
# cdf_2 = cdf[(cdf.index > 10) & (cdf.index <= 50)]
# cdf_3 = cdf[(cdf.index > 50) & (cdf.index <= 100)]
# cdf_4 = cdf[cdf.index > 100]

# fig, axs = plt.subplots(2, 2)
# axs = axs.flatten()

# axs[0].plot(cdf_1.index, cdf_1.values, marker='o')
# axs[0].set_title("CDF (1-10 Transactions)")
# axs[0].set_xlabel("Number of transactions")
# axs[0].set_ylabel("Fraction of wallets")
# axs[0].set_xticks(range(1, 11))

# axs[1].plot(cdf_2.index, cdf_2.values)
# axs[1].set_title("CDF (11-50 Transactions)")
# axs[1].set_xlabel("Number of transactions")
# axs[1].set_ylabel("Fraction of wallets")

# axs[2].plot(cdf_3.index, cdf_3.values)
# axs[2].set_title("CDF (51-100 Transactions)")
# axs[2].set_xlabel("Number of transactions")
# axs[2].set_ylabel("Fraction of wallets")

# axs[3].plot(cdf_4.index, cdf_4.values)
# axs[3].set_title("CDF (100+ Transactions)")
# axs[3].set_xlabel("Number of transactions")
# axs[3].set_ylabel("Fraction of wallets")

# plt.tight_layout()
# plt.show()

#----------------------------------------fraction contributed by top 10 senders------------------------------------------

# total= len(df)
# top10 = sent_counts.sort_values(ascending=False).head(10)
# top10_fraction = top10 / total
# cum_fraction = top10_fraction.cumsum()

# plt.figure()
# plt.plot(range(1, 11), cum_fraction.values, marker='o')
# plt.xlabel("Top X senders")
# plt.ylabel("Cumulative fraction of transactions")
# plt.title("Cumulative Contribution of Top Senders")

# plt.grid(True)
# plt.show()

#----------------------------------------fraction contributed by top 10 receivers------------------------------------------ 

# total= len(df)
# top10 = received_counts.sort_values(ascending=False).head(10)
# top10_fraction = top10 / total
# cum_fraction = top10_fraction.cumsum()

# plt.figure()
# plt.plot(range(1, 11), cum_fraction.values, marker='o')
# plt.xlabel("Top X receivers")
# plt.ylabel("Cumulative fraction of transactions")
# plt.title("Cumulative Contribution of Top Receivers")

# plt.grid(True)
# plt.show()

#----------------------------------------fraction contributed by top 10 wallets------------------------------------------ 
top10_senders = sent_counts.sort_values(ascending=False).head(10)
top10_receivers = received_counts.sort_values(ascending=False).head(10)
top_wallets = set(top10_senders.index) | set(top10_receivers.index)
total_counts = sent_counts.add(received_counts, fill_value=0)
top_activity = total_counts.loc[list(top_wallets)].sort_values(ascending=False)
top_activity = top_activity.head(10)
total_tx = len(df)
top_fraction = top_activity / total_tx
cum_fraction = top_fraction.cumsum()

plt.figure()
plt.plot(range(1, len(cum_fraction)+1), cum_fraction.values, marker='o')

plt.xlabel("Top X wallets")
plt.ylabel("Cumulative fraction")
plt.title("Cumulative Activity of Top Wallets (Send OR Receive)")

plt.grid(True)
plt.show()

#==========================================================================================================================








