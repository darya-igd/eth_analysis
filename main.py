from src.data_loader import load_transactions

import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

df= load_transactions("data/transactions.xlsx")

df['from_address'] = df['from_address'].str.lower()
df['to_address'] = df['to_address'].str.lower()

df= df.dropna(subset=['from_address'])

G= nx.DiGraph()

for _, row in df.iterrows():
    u= row['from_address']
    v= row['to_address']
    vol=row['transfer_volume']

    if G.has_edge(u,v):
        G[u][v]['count'] += 1
        G[u][v]['sum_value'] += vol

    else:
        G.add_edge(u,v, count=1, sum_value=vol)


# print("Nodes:", G.number_of_nodes())
# print("Edges:", G.number_of_edges())

out_deg= dict(G.out_degree())
in_deg= dict(G.in_degree())

top_senders= sorted(out_deg.items(), key=lambda x: x[1], reverse=True)[:10]
top_receivers= sorted(in_deg.items(), key=lambda x: x[1], reverse=True)[:10]

edges_count= sorted( G.edges(data=True), key=lambda x: x[2]['count'], reverse=True)[:10]

components= list(nx.weakly_connected_components(G))
sizes= sorted([len(c) for c in components], reverse=True)

# print ("\nconnected components:", len(components))
# print("\nTop 10 component sizes:", sizes[:10])
# print("\nLargest component %:", round(100*sizes[0]/G.number_of_nodes(),2)) 

seen= set()
ping_stats= []
ping_pong_pairs= []
for u,v in G.edges():
    if G.has_edge(v,u):
        pair= tuple(sorted((u,v)))
        if pair not in seen:
            seen.add(pair)
            ping_pong_pairs.append(pair)

            count_uv = G[u][v]['count']
            count_vu = G[v][u]['count']
            total = count_uv + count_vu
            ping_stats.append((u, v, total))

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

sent_counts= df['from_address'].value_counts()

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



# sort values
data = np.sort(sent_counts.values)

# cumulative fraction
cdf = np.arange(1, len(data) + 1) / len(data)

plt.figure(figsize=(10,6))

plt.plot(data, cdf, linewidth=2)

plt.xscale("log")   # important because transaction counts vary a lot

plt.xlabel("Number of transactions (Log)")
plt.ylabel("Fraction of wallets")
plt.title("CDF of Wallet Sending Activity")

plt.grid(True)

plt.show()




#==========================================================================================================================








