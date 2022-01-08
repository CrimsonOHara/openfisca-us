from openfisca_us.model_api import *

# Counties in NY state only for now.


class County(Enum):
    ALBANY_NY = "Albany, NY"
    ALLEGANY_NY = "Allegany, NY"
    BRONX_NY = "Bronx, NY"
    BROOME_NY = "Broome, NY"
    CATTARAUGUS_NY = "Cattaraugus, NY"
    CAYUGA_NY = "Cayuga, NY"
    CHAUTAUQUA_NY = "Chautauqua, NY"
    CHEMUNG_NY = "Chemung, NY"
    CHENANGO_NY = "Chenango, NY"
    CLINTON_NY = "Clinton, NY"
    COLUMBIA_NY = "Columbia, NY"
    CORTLAND_NY = "Cortland, NY"
    DELAWARE_NY = "Delaware, NY"
    DUTCHESS_NY = "Dutchess, NY"
    ERIE_NY = "Erie, NY"
    ESSEX_NY = "Essex, NY"
    FRANKLIN_NY = "Franklin, NY"
    FULTON_NY = "Fulton, NY"
    GENESEE_NY = "Genesee, NY"
    GREENE_NY = "Greene, NY"
    HAMILTON_NY = "Hamilton, NY"
    HERKIMER_NY = "Herkimer, NY"
    JEFFERSON_NY = "Jefferson, NY"
    KINGS_NY = "Kings, NY"
    LEWIS_NY = "Lewis, NY"
    LIVINGSTON_NY = "Livingston, NY"
    MADISON_NY = "Madison, NY"
    MONROE_NY = "Monroe, NY"
    MONTGOMERY_NY = "Montgomery, NY"
    NASSAU_NY = "Nassau, NY"
    NEW_YORK_NY = "New York, NY"
    NIAGARA_NY = "Niagara, NY"
    ONEIDA_NY = "Oneida, NY"
    ONONDAGA_NY = "Onondaga, NY"
    ONTARIO_NY = "Ontario, NY"
    ORANGE_NY = "Orange, NY"
    ORLEANS_NY = "Orleans, NY"
    OSWEGO_NY = "Oswego, NY"
    OTSEGO_NY = "Otsego, NY"
    PUTNAM_NY = "Putnam, NY"
    QUEENS_NY = "Queens, NY"
    RENSSELAER_NY = "Rensselaer, NY"
    RICHMOND_NY = "Richmond, NY"
    ROCKLAND_NY = "Rockland, NY"
    ST_LAWRENCE_NY = "St. Lawrence, NY"
    SARATOGA_NY = "Saratoga, NY"
    SCHENECTADY_NY = "Schenectady, NY"
    SCHOHARIE_NY = "Schoharie, NY"
    SCHUYLER_NY = "Schuyler, NY"
    SENECA_NY = "Seneca, NY"
    STEUBEN_NY = "Steuben, NY"
    SUFFOLK_NY = "Suffolk, NY"
    SULLIVAN_NY = "Sullivan, NY"
    TIOGA_NY = "Tioga, NY"
    TOMPKINS_NY = "Tompkins, NY"
    ULSTER_NY = "Ulster, NY"
    WARREN_NY = "Warren, NY"
    WASHINGTON_NY = "Washington, NY"
    WAYNE_NY = "Wayne, NY"
    WESTCHESTER_NY = "Westchester, NY"
    WYOMING_NY = "Wyoming, NY"
    YATES_NY = "Yates, NY"


class county(Variable):
    value_type = Enum
    possible_values = County
    default_value = County.NEW_YORK_NY
    entity = Household
    label = u"County"
    definition_period = ETERNITY