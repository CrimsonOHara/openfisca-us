from openfisca_us.model_api import *


class spm_unit_assets(Variable):
    value_type = float
    entity = SPMUnit
    label = u"SPM unit assets"
    definition_period = YEAR
    unit = "currency-USD"