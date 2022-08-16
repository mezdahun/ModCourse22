"""Main class to create and run model simulations"""
import numpy as np
import matplotlib.pyplot as plt


class Model:
    """Main Model class to include simulation and model parameters"""

    def __init__(self, t_max, dt=1, model_name="General Model"):
        """Init method to create model instance

        :param t_max: maximum or end time of the model simulation
        :param dt: simulation time resolution
        :param model_name: name or identifier of the model to be simulated
        """
        # Simulation parameters
        self.t = 0
        self.t_i = 0
        self.t_max = t_max
        self.dt = dt
        self.t_len = int(self.t_max / self.dt)

        # General Model parameters
        self.model_name = model_name

        print(f"Initialized Model: {self.model_name}")

    def run(self):
        """Running model simulation"""
        for self.t_i in range(1, self.t_len):
            self.evolve()
            self.t += self.dt

    def evolve(self):
        """Single step evolution method to be overwritten in children"""
        pass

    def show_evolution(self, state_vars, var_names=None):
        """Showing the evolution (over time) of a given state variable

        :param state_vars: list of numpy arrays of recorded state variables (data)
        :param var_names: names of state variables for plot titles
        """
        num_vars = len(state_vars)
        if var_names is not None:
            if len(var_names) != num_vars:
                raise Exception("Passed different amount od state variables and variable names to plotting method")

        time = np.arange(0, self.t_max, self.dt)

        fig, ax = plt.subplots(1, num_vars, sharex=True)
        plt.suptitle(self.model_name)

        for i, var in enumerate(state_vars):
            plt.axes(ax[i])
            plt.plot(time, state_vars[i])
            plt.xlabel("time")
            if var_names is not None:
                plt.title(var_names[i])
        plt.show()


class NeuronModel(Model):
    def __init__(self, t_max, dt=1, Tau_e=1, Tau_r=1, Beta=1):
        """Model Parameters:
        """
        super().__init__(t_max, dt, model_name="Corona Measure Model")
        # Model Specific Parameters
        # generating Input injection function


        # corona cases
        self.e = np.zeros(self.t_len)
        self.e[0] = 1
        self.Tau_e = Tau_e

        # Restrictions
        self.r = np.zeros(self.t_len)
        self.r[0] = 0
        self.Tau_r = Tau_r
        self.Beta = Beta

    def alpha(self, r):
        """Introducing nonlinearity into the model"""
        return (1 - r)

    def evolve(self):
        """Overriding evolve method of superclass"""

        print(f"Evolving system with timestep {self.t_i}")

        # Nonlinear Model
        de = (1 / self.Tau_e) * self.alpha(self.r[self.t_i - 1]) * (self.e[self.t_i - 1])
        dr = (1 / self.Tau_r) * (self.Beta * self.e[self.t_i - 1] - self.r[self.t_i - 1])

        # Evolving state variables in time
        self.e[self.t_i] = self.e[self.t_i - 1] + de * self.dt
        self.r[self.t_i] = self.r[self.t_i - 1] + dr * self.dt


class CoronaMeasureModel(Model):
    def __init__(self, t_max, dt=1, Tau_c=20, Tau_r=25, alpha=1.5, A=0.1, r_inf=5, linear=True):
        """Model Parameters:
        """
        super().__init__(t_max, dt, model_name="Corona Measure Model")
        # Model Specific Parameters
        # generating Input injection function
        self.linear = linear

        # corona cases
        self.c = np.zeros(self.t_len)
        self.c[0] = 100
        self.Tau_c = Tau_c

        # Restrictions
        self.r = np.zeros(self.t_len)
        self.r[0] = 0
        self.r_inf = r_inf
        self.A = A
        self.Tau_r = Tau_r
        self.alpha = alpha  # ratio of reported

    def coeff(self, r):
        """Introducing nonlinearity into the model"""
        return self.A * (self.r_inf - r)

    def evolve(self):
        """Overriding evolve method of superclass"""

        print(f"Evolving system with timestep {self.t_i}")

        # Calculating temporal evolution
        # Linear Model
        if self.linear:
            dc = (1 / self.Tau_c) * (self.c[self.t_i - 1] - self.alpha * self.r[self.t_i - 1])
        else:
            # Nonlinear Model
            dc = (1 / self.Tau_c) * self.coeff(self.r[self.t_i - 1]) * (self.c[self.t_i - 1])
        dr = (1 / self.Tau_r) * (self.c[self.t_i - 1] - self.r[self.t_i - 1])

        # Evolving state variables in time
        self.c[self.t_i] = self.c[self.t_i - 1] + dc * self.dt
        self.r[self.t_i] = self.r[self.t_i - 1] + dr * self.dt

        # Restricting cases to positive in linear model
        # if self.c[self.t_i] < 0:
        #     self.c[self.t_i] = 0
        # if self.r[self.t_i] < 0:
        #     self.r[self.t_i] = 0

    def get_data(self):
        """returning evolved data structure"""
        return self.c, self.r

class CoronaInjectionModel(Model):
    def __init__(self, t_inj, t_max, dt=1, I_amp=100, Tau_1=5, Tau_2=200):
        """Model Parameters:

        t_inj = time point of injection
        I_amp = aux. unit amplitude of injection function
        Tau_1 = mRNA to protein timescale
        Tau_2 = Immunity to protein timescale
        """
        super().__init__(t_max, dt, model_name="Corona Injection Immunity Model")

        # Model Specific Parameters
        # generating Input injection function
        self.t_inj = t_inj
        self.t_inj_i = int(self.t_inj / self.dt)
        self.I = np.zeros(self.t_len)
        self.I[self.t_inj_i:self.t_inj_i + 10] = I_amp

        # mRNA to Protein process
        self.x1 = np.zeros(self.t_len)
        self.Tau_1 = Tau_1

        # Immune reaction to protein process
        self.x2 = np.zeros(self.t_len)
        self.Tau_2 = Tau_2

    def evolve(self):
        """Overriding evolve method of superclass"""

        print(f"Evolving system with timestep {self.t_i}")

        # Calculating temporal evolution
        dx1 = - (1 / self.Tau_1) * self.x1[self.t_i - 1] + self.I[self.t_i - 1]
        dx2 = - (1 / self.Tau_2) * self.x2[self.t_i - 1] + self.x1[self.t_i - 1]

        # Evolving state variables in time
        self.x1[self.t_i] = self.x1[self.t_i - 1] + dx1 * self.dt
        self.x2[self.t_i] = self.x2[self.t_i - 1] + dx2 * self.dt
