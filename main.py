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
#     mod = CoronaMeasureModel(t_max, dt, Tau_c=1, Tau_r=K, alpha=0.5)
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
#
#
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
#     mod = CoronaMeasureModel(t_max, dt, Tau_c=1, Tau_r=K, alpha=1.5)
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
#
#
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
#     mod = CoronaMeasureModel(t_max, dt, Tau_c=1, Tau_r=K, alpha=1.5)
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
#
#
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
#     mod = CoronaMeasureModel(t_max, dt, Tau_c=1, Tau_r=0.5, alpha=alpha)
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
#
#
# # Generating figure 2.2
# cs = []
# rs = []
# fig, ax = plt.subplots(2, 1, figsize=(8, 8), sharex=True, sharey=True)
# alphas = [ 1.05, 1.1, 1.25, 1.5, 1.75, 2.5]
# colors = cm.jet(np.linspace(0, 1, len(alphas)))
#
# t_max = 25
# dt = 0.01
# t = np.arange(0, t_max, dt)
# for i, alpha in enumerate(alphas):
#     # defining model with given parameters
#     mod = CoronaMeasureModel(t_max, dt, Tau_c=1, Tau_r=1.5, alpha=alpha)
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
# plt.legend(loc="upper left")
# plt.ylabel("Positive Cases")
# plt.axes(ax[1])
# plt.legend(loc="upper left")
# plt.ylabel("Reported Cases ~ Measures")
# plt.xlabel("t [days]")
# plt.show()


# # Generating figure 3.1
# cs = []
# rs = []
# fig, ax = plt.subplots(2, 1, figsize=(8, 8), sharex=True)
# a_s = [0.1, 0.25, 0.5, 0.75, 1]
# r_inf = 500
# Tau_r = 10
# colors = cm.jet(np.linspace(0, 1, len(a_s)))
#
# t_max = 100
# dt = 0.01
# t = np.arange(0, t_max, dt)
# for i, a in enumerate(a_s):
#     # defining model with given parameters
#     mod = CoronaMeasureModel(t_max, dt, Tau_r=10, A=a, r_inf=r_inf, linear=False)  # non-linear model parameters
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
#     plt.plot(t, c, label=f"$a$={a}", color=col)
#     if i == len(a_s) - 1:
#         plt.axhline(y=r_inf, color='black', linestyle='--', label=f"$r_\\infty$")
#     plt.axes(ax[1])
#     plt.plot(t, r, label=f"$a$={a}", color=col)
#     if i == len(a_s) - 1:
#         plt.axhline(y=r_inf, color='black', linestyle='--', label=f"$r_\\infty$")
#
# plt.axes(ax[0])
# plt.legend(loc="upper right")
# plt.ylabel("Positive Cases")
# plt.axes(ax[1])
# plt.ylabel("Reported Cases ~ Measures")
# plt.xlabel("t [days]")
# plt.show()

# # Generating figure 3.2
# cs = []
# rs = []
# fig, ax = plt.subplots(2, 1, figsize=(8, 8), sharex=True)
# r_infs = [0, 50, 250, 500, 1000]
# a = 0.1
# Tau_r = 10
# colors = cm.jet(np.linspace(0, 1, len(r_infs)))
#
# t_max = 100
# dt = 0.01
# t = np.arange(0, t_max, dt)
# for i, r_inf in enumerate(r_infs):
#     # defining model with given parameters
#     mod = CoronaMeasureModel(t_max, dt, Tau_r=Tau_r, A=a, r_inf=r_inf, linear=False)  # non-linear model parameters
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
#     plt.plot(t, c, label=f"$r_{{\\infty}}$={r_inf}", color=col)
#     plt.axhline(y=r_inf, color=col, linestyle='--')
#     plt.axes(ax[1])
#     plt.plot(t, r, label=f"$r_{{\\infty}}$={r_inf}", color=col)
#     plt.axhline(y=r_inf, color=col, linestyle='--')
#
# plt.axes(ax[0])
# plt.legend(loc="upper right")
# plt.ylabel("Positive Cases")
# plt.ylim((-500, 10000))
# plt.axes(ax[1])
# plt.ylabel("Reported Cases ~ Measures")
# plt.xlabel("t [days]")
# plt.show()
