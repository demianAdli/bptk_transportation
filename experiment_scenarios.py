import matplotlib.pyplot as plt

from genesis_transportation import *
import BPTK_Py


bptk = BPTK_Py.bptk()
scenario_manager = {
    'population_senarios': {
        'model': model_01,
        'base_constants': {
            'initial_population': 17100,
            'public_investment_in_mobility': 2e9,
            'available_transportation_modes': 3.0
        }
    }
}

bptk.register_scenario_manager(scenario_manager)

bptk.register_scenarios(
    scenarios={
            'scenario_default': {
                'constants': {
                    'initial_population': 17100
                }
            },
            'scenario_20': {
                'constants': {
                    'initial_population': 20000
                }
            }
        }
    ,
    scenario_manager='population_senarios')

population_results = bptk.plot_scenarios(
    scenarios='scenario_default,scenario_20',
    scenario_managers='population_senarios',
    equations='Number of Private Cars',
    series_names={
        'population_senarios_scenario_default_Number of Private Cars': 'scenario_default',
        'population_senarios_scenario_20_Number of Private Cars': 'scenario_20'
    }, return_df=True

)
print(population_results)
plt.show()
