import sqlite3
from sqlite3 import dbapi2

connection = sqlite3.connect("switrs.sqlite")

cursor = connection.cursor()



for row in cursor.execute("SELECT * FROM collisions"):
    case_id = row[0]
    jurisdiction = row[1]
    new_collision = Collision(case_id=case_id, jurisdiction = jurisdiction)
    commit(new_collision)    

connection.close()

class Collision(db.Model):
    case_id = case_id
    jurisdiction
    officer_id
    reporting_district
    chp_shift
    population
    county_city_location
    special_condition
    beat_type
    chp_beat_type
    city_division_lapd
    chp_beat_class
    beat_number
    primary_road
    secondary_road
    distance
    direction
    intersection
    weather_1
    weather_2
    state_highway_indicator
    caltrans_county
    caltrans_district
    state_route
    route_suffix
    postmile_prefix
    postmile
       'location_type', 'ramp_intersection', 'side_of_highway', 'tow_away',
       'collision_severity', 'killed_victims', 'injured_victims',
       'party_count', 'primary_collision_factor', 'pcf_violation_code',
       'pcf_violation_category', 'pcf_violation', 'pcf_violation_subsection',
       'hit_and_run', 'type_of_collision', 'motor_vehicle_involved_with',
       'pedestrian_action', 'road_surface', 'road_condition_1',
       'road_condition_2', 'lighting', 'control_device', 'chp_road_type',
       'pedestrian_collision', 'bicycle_collision', 'motorcycle_collision',
       'truck_collision', 'not_private_property', 'alcohol_involved',
       'statewide_vehicle_type_at_fault', 'chp_vehicle_type_at_fault',
       'severe_injury_count', 'other_visible_injury_count',
       'complaint_of_pain_injury_count', 'pedestrian_killed_count',
       'pedestrian_injured_count', 'bicyclist_killed_count',
       'bicyclist_injured_count', 'motorcyclist_killed_count',
       'motorcyclist_injured_count', 'primary_ramp', 'secondary_ramp',
       'latitude', 'longitude', 'collision_date', 'collision_time',
       'process_date'

"""

Parties:

Victims:
'id', 'case_id', 'party_number', 'victim_role', 'victim_sex',
       'victim_age', 'victim_degree_of_injury', 'victim_seating_position',
       'victim_safety_equipment_1', 'victim_safety_equipment_2',
       'victim_ejected'

"""