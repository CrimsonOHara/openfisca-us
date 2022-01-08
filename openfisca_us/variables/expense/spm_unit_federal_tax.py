from openfisca_us.model_api import *


class spm_unit_federal_tax(Variable):
    value_type = float
    entity = SPMUnit
    label = u"SPM unit federal tax"
    definition_period = YEAR
    unit = "currency-USD"