from openfisca_us.model_api import *


class household_net_income(Variable):
    value_type = float
    entity = Household
    label = u"Household net income"
    definition_period = YEAR
    unit = "currency-USD"

    def formula(household, period, parameters):
        return household.sum(household.members("net_income", period))