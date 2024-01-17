# Name:   <Nicholas Tillo>
# Student Number: <20291255>
# Email:  <20njt4@queensu.ca>

# I confirm that this assignment solution is my own work and conforms to 
# Queen's standards of Academic Integrity

from matplotlib import pyplot as plt

starting_sheep = 100
starting_hyena = 25

#Case 1
sheep_growth = 0.005
eating_rate = 0.0009
hyena_growth = 0.0005
hyena_death = 0.02

#Case 2
sheep_growth_2 = 0.01
eating_rate_2 = 0.0001
hyena_growth_2 = 0.0002
hyena_death_2 = 0.03

def create_points(k_1, k_2, k_3, k_4, years, sheep, hyena):
    '''
    Creates a list of values for the amount of sheep to the amount of hyenas 
    for an amount of years, depending on conditions k_1, k_2, k_3, k_4.

    Parameters
    k_1 - Float
    k_2 - Float
    k_3 - Float 
    k_4 - Float
    years - Int > 0
    sheep - Int > 0
    hyena - Int > 0
    '''
    list_sheep = [sheep]
    list_hyena = [hyena]
    for val in range(years):
        change_sheep = (k_1 * sheep) - (k_2 * sheep * hyena)
        change_hyena = (k_3 * sheep * hyena) - (k_4 * hyena)
        sheep += change_sheep
        hyena += change_hyena
        list_sheep.append(sheep)
        list_hyena.append(hyena)
    return list_sheep, list_hyena
        
        
set_sheep , set_hyena = create_points(sheep_growth, eating_rate, hyena_growth, hyena_death, 10000, starting_sheep, starting_hyena)
set_sheep_2 , set_hyena_2  = create_points(sheep_growth_2, eating_rate_2, hyena_growth_2, hyena_death_2, 10000, starting_sheep, starting_hyena)
plt.subplot(211)
plt.plot(set_sheep, label = "Sheep")
plt.plot(set_hyena, label = "Hyena")
plt.legend()
plt.subplot(212)
plt.plot(set_sheep_2, label = "Sheep")
plt.plot(set_hyena_2, label = "Hyena")
plt.legend()
plt.show()

