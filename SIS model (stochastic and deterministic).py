import numpy as np
from matplotlib import pyplot as plt

def prob_time_until_infection():
    #Placeholder
    print("HI")
def prob_time_until_recovery():
    #Placeholder
    print("Hi")

start_infected = 100
list_values = [[0.1, 0.2], [1, 2], [10, 5]]
dt = 0.01

time_to_infection_list = []
time_to_recovery_list = []
number_of_repititions = 100000

for i, values in enumerate(list_values):
    bn = values[0]
    dn = values[1]

    prob_another_infection = bn * dt
    prob_another_recovery = dn * dt
    prob_nothing = 1 -(bn + dn) * dt

    infection_times_local = []
    recovery_times_local = []

    for idx in range(number_of_repititions):
        infection_found = False
        recovery_found = False
        j = 0
        while not (infection_found and recovery_found):

            random_value = np.random.rand()

            time_step = j * dt
            if random_value < prob_nothing:
                j += 1
                continue
            elif random_value < (prob_another_infection+prob_nothing):
                
                infection_times_local.append(time_step)
                infection_found = True
            else:
                recovery_times_local.append(time_step)
                recovery_found = True
            j += 1
    
    counts_infection, bin_edges_infection = np.histogram(infection_times_local, bins = 60, density=True)
    counts_infection = np.where(counts_infection == 0, 1e-10, counts_infection)
    counts_recovery, bin_edges_recovery = np.histogram(recovery_times_local, bins = 60, density=True)
    counts_recovery = np.where(counts_recovery == 0, 1e-10, counts_recovery)
    bin_center_infection = 0.5 * (bin_edges_infection[:-1] + bin_edges_infection[1:])
    bin_center_recovery = 0.5 * (bin_edges_recovery[:-1] + bin_edges_recovery[1:])
    log_counts_infection = np.log(counts_infection)
    log_counts_recovery = np.log(counts_recovery)

    gradient_infection = np.polyfit(bin_center_infection, log_counts_infection, 1)[0]
    gradient_recovery = np.polyfit(bin_center_recovery, log_counts_recovery, 1)[0]
    print(f"Gradient for infection times (bn={bn}, dn={dn}): {gradient_infection:.3f}")
    print(f"Gradient for recovery times (bn={bn}, dn={dn}): {gradient_recovery:.3f}")

    fig, axs = plt.subplots(1, 2, figsize=(10, 5))
    axs[0].plot(bin_center_infection, log_counts_infection)
    axs[0].set_title(f"Time until infection (bn={bn}, dn={dn})")
    axs[0].set_xlabel("Time until infection")
    axs[0].set_ylabel("log P(t_b)")
    axs[0].text(0.1, 0.2, f"Gradient: {gradient_infection:.3f}", transform = axs[0].transAxes)
    axs[1].set_title(f"Time until recovery (bn={bn}, dn={dn})")
    axs[1].set_xlabel("Time until recovery")
    axs[1].set_ylabel("log P(t_r)")
    axs[1].text(0.1, 0.2, f"Gradient: {gradient_recovery:.3f}", transform = axs[1].transAxes)
    axs[1].plot(bin_center_recovery, log_counts_recovery)

    plt.show()
    print(f"Infection times for bn={bn}, dn={dn}: Mean = {np.mean(infection_times_local):.3f}, Std = {np.std(infection_times_local):.3f}")
    print(f"Recovery times for bn={bn}, dn={dn}: Mean = {np.mean(recovery_times_local):.3f}, Std = {np.std(recovery_times_local):.3f}")
    time_to_infection_list.append(infection_times_local)
    time_to_recovery_list.append(recovery_times_local)


        


        


    


