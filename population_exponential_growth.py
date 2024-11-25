"""
This project implements a system dynamic model using bptk-py.
The model has been developed during the CERC SDM course (main lecturer: Dr. Eicker)
by team #. Cena as the main developer of the project, developed it further
for this new project. I, Alireza, was a TA of the course and helped the development and now
implement it using Python's BPTK-Py
Project code developer: Alireza Adli alireza.adli@mail.concordia.ca
Project theoritical developer: Cena   @mail.concordia.ca
"""

from BPTK_Py import Model
from BPTK_Py import sd_functions as sd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

population_exponential_growth = Model(starttime=0.0, stoptime=25.0, dt=1.0, name='SimpleProjectManagement')

private_cars_num = population_exponential_growth.stock('Number of Private Cars')
new_cars_num = population_exponential_growth.flow('Number of New Cars')
shift_to_sustainable_modes = population_exponential_growth.flow('Shift to Sustainable Modes')
initial_population = population_exponential_growth.constant('Initial Population')
population_growth_rate = population_exponential_growth.constant('Population Growth Rate')
population = population_exponential_growth.converter('Population')
current_infrastructure_capacity = population_exponential_growth.converter('Current Infrastructure Capacity')
education_level = population_exponential_growth.converter('Education Level')
sustainable_mode_preference = population_exponential_growth.converter('Mode Preference Towards Sustainable Modes')
available_transportation_modes = population_exponential_growth.constant('Available Transportation Modes')
ride_sharing_trip_share = population_exponential_growth.converter('Share of Ride-Sharing Trips')
public_transport_trip_share = population_exponential_growth.converter('Share of Public Transport Trips')
active_transportation_trip_share = population_exponential_growth.converter('Share of Active Transportation Trips')
investment_in_rs = population_exponential_growth.converter('Investment in RS')
investment_in_pt = population_exponential_growth.converter('Investment in PT')
investment_in_at = population_exponential_growth.converter('Investment in AT')
public_investment_in_mobility = population_exponential_growth.constant('Public Investment in Mobility')

public_investment_in_mobility.equation = 2e9
available_transportation_modes.equation = 3.0
initial_population.equation = 17100
population_growth_rate.equation = 0.01
population.equation = initial_population * sd.exp(population_growth_rate * sd.time())
initial_private_cars_num = population_exponential_growth.converter('Initial Number of Private Cars')
initial_private_cars_num.equation = (sd.If(sd.time() == 0, population, initial_private_cars_num)) * 0.84 * 0.9
# initial_private_cars_num.equation = population*0.84*0.9

private_cars_num.initial_value = initial_private_cars_num

private_cars_num.equation = new_cars_num - shift_to_sustainable_modes

new_cars_num.equation = (1 - sd.time() / 25) * (population - shift_to_sustainable_modes) * 0.84 * 0.9
education_level.equation = sd.time() / 25
sustainable_mode_preference.equation = (available_transportation_modes / (available_transportation_modes + 1)) * (1 + education_level + 1.1)

ride_sharing_trip_share.equation = sustainable_mode_preference * (1 + investment_in_rs / public_investment_in_mobility)
public_transport_trip_share.equation = sustainable_mode_preference * (1 + investment_in_pt / public_investment_in_mobility)
active_transportation_trip_share.equation = sustainable_mode_preference * (1 + investment_in_at / public_investment_in_mobility)
investment_in_rs.equation = 2e8 + public_investment_in_mobility * 0.3
investment_in_pt.equation = 8e8 + 0.6 * public_investment_in_mobility
investment_in_at.equation = 5e7 + public_investment_in_mobility * 0.1
current_infrastructure_capacity.equation = 100 / (1 + sd.exp(-(0.05 * (sd.time() - 15))))
shift_to_sustainable_modes.equation = \
  ((min(1, current_infrastructure_capacity / 100) *
    (active_transportation_trip_share + public_transport_trip_share + ride_sharing_trip_share) /
    max(1, (active_transportation_trip_share + public_transport_trip_share + ride_sharing_trip_share))) / 100) * private_cars_num

print(private_cars_num(0))
print(private_cars_num(23))
private_cars_num.plot()
plt.show()