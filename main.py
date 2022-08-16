from modc22.model import CoronaInjectionModel, CoronaMeasureModel, NeuronModel
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np


# # Linear vs Non-linear model of Introducing Corona measurements in the population
# # Generating figure 1.1
# cs = []
# rs = []
# fig, ax = plt.subplots(2, 1, figsize=(8, 8), sharex=True, sharey=True)
# Ks = [0.1, 0.25, 0.5, 1, 1.5, 3]
# colors = cm.jet(np.linspace(0, 1, len(Ks)))
#
# t_max = 10
# dt = 0.01
# t = np.arange(0, t_max, dt)
# for i, K in enumerate(Ks):
#     # defining model with given parameters
#     mod = CoronaMeasureModel(t_max, dt, Tau_c=1, Tau_r=K, alpha=0.5,  # linear model parameters
#                              A=0.9, r_inf=20)  # non-linear model parameters
#     # evolving system
#     mod.run()
#
#     # collecting data
#     c, r = mod.get_data()
#     cs.append(c)
#     rs.append(r)
#
#     # showing data
#     col = colors[i]
#     plt.axes(ax[0])
#     plt.plot(t, c * 1e5, label=f"K={K}", color=col)
#     plt.axes(ax[1])
#     plt.plot(t, r * 1e5, label=f"K={K}", color=col)
#
# plt.axes(ax[0])
# plt.legend(loc="upper left")
# plt.ylabel("Positive Cases")
# plt.axes(ax[1])
# plt.legend(loc="upper left")
# plt.ylabel("Reported Cases ~ Measures")
# plt.xlabel("t [days]")
# plt.show()


# # Generating figure 1.2
# cs = []
# rs = []
# fig, ax = plt.subplots(2, 1, figsize=(8, 8), sharex=True, sharey=True)
# Ks = [0.1, 0.25, 0.5, 0.75, 1]
# colors = cm.jet(np.linspace(0, 1, len(Ks)))
#
# t_max = 30
# dt = 0.01
# t = np.arange(0, t_max, dt)
# for i, K in enumerate(Ks):
#     # defining model with given parameters
#     mod = CoronaMeasureModel(t_max, dt, Tau_c=1, Tau_r=K, alpha=1.5,  # linear model parameters
#                              A=0.9, r_inf=20)  # non-linear model parameters
#     # evolving system
#     mod.run()
#
#     # collecting data
#     c, r = mod.get_data()
#     cs.append(c)
#     rs.append(r)
#
#     # showing data
#     col = colors[i]
#     plt.axes(ax[0])
#     plt.plot(t, c * 1e5, label=f"K={K}", color=col)
#     plt.axes(ax[1])
#     plt.plot(t, r * 1e5, label=f"K={K}", color=col)
#
# plt.axes(ax[0])
# plt.legend(loc="upper right")
# plt.ylabel("Positive Cases")
# plt.axes(ax[1])
# plt.legend(loc="upper right")
# plt.ylabel("Reported Cases ~ Measures")
# plt.xlabel("t [days]")
# plt.show()


# # Generating figure 1.3
# cs = []
# rs = []
# fig, ax = plt.subplots(2, 1, figsize=(8, 8), sharex=True, sharey=True)
# Ks = [1, 1.1, 1.25, 1.5, 1.75]
# colors = cm.jet(np.linspace(0, 1, len(Ks)))
#
# t_max = 30
# dt = 0.01
# t = np.arange(0, t_max, dt)
# for i, K in enumerate(Ks):
#     # defining model with given parameters
#     mod = CoronaMeasureModel(t_max, dt, Tau_c=1, Tau_r=K, alpha=1.5,  # linear model parameters
#                              A=0.9, r_inf=20)  # non-linear model parameters
#     # evolving system
#     mod.run()
#
#     # collecting data
#     c, r = mod.get_data()
#     cs.append(c)
#     rs.append(r)
#
#     # showing data
#     col = colors[i]
#     plt.axes(ax[0])
#     plt.plot(t, c * 1e5, label=f"K={K}", color=col)
#     plt.axes(ax[1])
#     plt.plot(t, r * 1e5, label=f"K={K}", color=col)
#
# plt.axes(ax[0])
# plt.legend(loc="upper left")
# plt.ylabel("Positive Cases")
# plt.axes(ax[1])
# plt.legend(loc="upper left")
# plt.ylabel("Reported Cases ~ Measures")
# plt.xlabel("t [days]")
# plt.show()


# # Generating figure 2.1
# cs = []
# rs = []
# fig, ax = plt.subplots(2, 1, figsize=(8, 8), sharex=True, sharey=True)
# alphas = [1, 1.01, 1.05, 1.1, 1.25, 1.5, 1.75, 2.5]
# colors = cm.jet(np.linspace(0, 1, len(alphas)))
#
# t_max = 30
# dt = 0.01
# t = np.arange(0, t_max, dt)
# for i, alpha in enumerate(alphas):
#     # defining model with given parameters
#     mod = CoronaMeasureModel(t_max, dt, Tau_c=1, Tau_r=0.5, alpha=alpha,  # linear model parameters
#                              A=0.9, r_inf=20)  # non-linear model parameters
#     # evolving system
#     mod.run()
#
#     # collecting data
#     c, r = mod.get_data()
#     cs.append(c)
#     rs.append(r)
#
#     # showing data
#     col = colors[i]
#     plt.axes(ax[0])
#     plt.plot(t, c * 1e5, label=f"$\\alpha$={alpha}", color=col)
#     plt.axes(ax[1])
#     plt.plot(t, r * 1e5, label=f"$\\alpha$={alpha}", color=col)
#
# plt.axes(ax[0])
# plt.legend(loc="upper right")
# plt.ylabel("Positive Cases")
# plt.axes(ax[1])
# plt.legend(loc="upper right")
# plt.ylabel("Reported Cases ~ Measures")
# plt.xlabel("t [days]")
# plt.show()


# Generating figure 2.2
cs = []
rs = []
fig, ax = plt.subplots(2, 1, figsize=(8, 8), sharex=True, sharey=True)
alphas = [ 1.05, 1.1, 1.25, 1.5, 1.75, 2.5]
colors = cm.jet(np.linspace(0, 1, len(alphas)))

t_max = 25
dt = 0.01
t = np.arange(0, t_max, dt)
for i, alpha in enumerate(alphas):
    # defining model with given parameters
    mod = CoronaMeasureModel(t_max, dt, Tau_c=1, Tau_r=1.5, alpha=alpha,  # linear model parameters
                             A=0.9, r_inf=20)  # non-linear model parameters
    # evolving system
    mod.run()

    # collecting data
    c, r = mod.get_data()
    cs.append(c)
    rs.append(r)

    # showing data
    col = colors[i]
    plt.axes(ax[0])
    plt.plot(t, c * 1e5, label=f"$\\alpha$={alpha}", color=col)
    plt.axes(ax[1])
    plt.plot(t, r * 1e5, label=f"$\\alpha$={alpha}", color=col)

plt.axes(ax[0])
plt.legend(loc="upper left")
plt.ylabel("Positive Cases")
plt.axes(ax[1])
plt.legend(loc="upper left")
plt.ylabel("Reported Cases ~ Measures")
plt.xlabel("t [days]")
plt.show()