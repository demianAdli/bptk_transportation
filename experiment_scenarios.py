import matplotlib.pyplot as plt

from genesis_transportation import *
import BPTK_Py


bptk = BPTK_Py.bptk()
# bptk.register_model(model_01)

scenario_manager = {
    'population_senarios': {
        'model': model_01,
        'base_constants': {
            'Initial Population': 17100,
            'Public Investment in Mobility': 2e9,
            'Available Transportation Modes': 3.0
        }
    }
}

bptk.register_scenario_manager(scenario_manager)

bptk.register_scenarios(
    scenarios={
            'base': {
            },
            'scenario20': {
                'constants': {
                    'Initial Population': 20000
                }
            }
        }
    ,
    scenario_manager='population_senarios')

population_results = bptk.plot_scenarios(
    scenarios='base,scenario20',
    scenario_managers='population_senarios',
    equations='Number of Private Cars',
    series_names={
        'population_senarios_base_Number of Private Cars': 'base',
        'population_senarios_scenario20_Number of Private Cars': 'scenario20'
    }, return_df=True
)
print(population_results)
plt.show()

# print(bptk.get_scenario_names([], format="dict"))
