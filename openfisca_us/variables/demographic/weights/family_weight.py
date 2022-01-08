from openfisca_us.model_api import *


class family_weight(Variable):
    value_type = float
    entity = Family
    label = u"Family weight"
    definition_period = YEAR