RESULT_OK = {"response": {"reason": "", "result": True}}
RESULT_NOT_OK = {"response": {"reason": "", "result": False}}

# 408 - Request Timeout
RESULT_VEHICLE_UNAVAILABLE = {
    "response": None,
    "error": 'vehicle unavailable: {:error=>"vehicle unavailable:"}',
    "error_description": "",
}


VIN = "5yjsa11111111111"
CAR_ID = 12345678901234567
# 2015 Model S 85D with some manually added keys (sentry mode, heated steering) for testing
VEHICLE_DATA = {
    "id": 12345678901234567,
    "user_id": 123456,
    "vehicle_id": 1234567890,
    "vin": "5YJSA11111111111",
    "display_name": "My Model S",
    "option_codes": "AD15,MDL3,PBSB,RENA,BT37,ID3W,RF3G,S3PB,DRLH,DV2W,W39B,APF0,COUS,BC3B,CH07,PC30,FC3P,FG31,GLFR,HL31,HM31,IL31,LTPB,MR31,FM3B,RS3H,SA3P,STCP,SC04,SU3C,T3CA,TW00,TM00,UT3P,WR00,AU3P,APH3,AF00,ZCST,MI00,CDM0,P3WS",
    "color": None,
    "access_type": "OWNER",
    "tokens": ["redacted", "redacted"],
    "state": "online",
    "in_service": False,
    "id_s": "12345678901234567",
    "calendar_enabled": True,
    "api_version": 36,
    "backseat_token": None,
    "backseat_token_updated_at": None,
    "charge_state": {
        "battery_heater_on": False,
        "battery_level": 78,
        "battery_range": 169.08,
        "charge_amps": 32,
        "charge_current_request": 32,
        "charge_current_request_max": 32,
        "charge_enable_request": True,
        "charge_energy_added": 13.57,
        "charge_limit_soc": 80,
        "charge_limit_soc_max": 100,
        "charge_limit_soc_min": 50,
        "charge_limit_soc_std": 90,
        "charge_miles_added_ideal": 59.0,
        "charge_miles_added_rated": 47.0,
        "charge_port_cold_weather_mode": None,
        "charge_port_color": "FlashingGreen",
        "charge_port_door_open": True,
        "charge_port_latch": "Engaged",
        "charge_rate": 23.2,
        "charge_to_max_range": False,
        "charger_actual_current": 32,
        "charger_phases": 1,
        "charger_pilot_current": 32,
        "charger_power": 7,
        "charger_voltage": 242,
        "charging_state": "Charging",
        "conn_charge_cable": "SAE",
        "est_battery_range": 150.09,
        "fast_charger_brand": "<invalid>",
        "fast_charger_present": False,
        "fast_charger_type": "MCSingleWireCAN",
        "ideal_battery_range": 213.19,
        "managed_charging_active": False,
        "managed_charging_start_time": None,
        "managed_charging_user_canceled": False,
        "max_range_charge_counter": 0,
        "minutes_to_full_charge": 15,
        "not_enough_power_to_heat": False,
        "off_peak_charging_enabled": True,
        "off_peak_charging_times": "weekdays",
        "off_peak_hours_end_time": 360,
        "preconditioning_enabled": False,
        "preconditioning_times": "all_week",
        "scheduled_charging_mode": "DepartBy",
        "scheduled_charging_pending": False,
        "scheduled_charging_start_time": None,
        "scheduled_charging_start_time_app": 480,
        "scheduled_departure_time": 1661515200,
        "scheduled_departure_time_minutes": 300,
        "supercharger_session_trip_planner": False,
        "time_to_full_charge": 0.25,
        "timestamp": 1661641175268,
        "trip_charging": False,
        "usable_battery_level": 77,
        "user_charge_enable_request": None,
    },
    "climate_state": {
        "allow_cabin_overheat_protection": True,
        "battery_heater": False,
        "battery_heater_no_power": False,
        "cabin_overheat_protection": "Off",
        "climate_keeper_mode": "off",
        "defrost_mode": 0,
        "driver_temp_setting": 23.3,
        "fan_status": 0,
        "hvac_auto_request": "On",
        "inside_temp": 35.5,
        "is_auto_conditioning_on": False,
        "is_climate_on": False,
        "is_front_defroster_on": False,
        "is_preconditioning": False,
        "is_rear_defroster_on": False,
        "left_temp_direction": -309,
        "max_avail_temp": 28.0,
        "min_avail_temp": 15.0,
        "outside_temp": 32.5,
        "passenger_temp_setting": 23.3,
        "remote_heater_control_enabled": False,
        "right_temp_direction": -309,
        "seat_heater_left": 0,
        "seat_heater_right": 0,
        "side_mirror_heaters": False,
        "supports_fan_only_cabin_overheat_protection": False,
        "timestamp": 1661641175268,
        "wiper_blade_heater": False,
        "steering_wheel_heater": True,
    },
    "drive_state": {
        "active_route_destination": "Saved destination name",
        "active_route_energy_at_arrival": 40,
        "active_route_latitude": 34.111111,
        "active_route_longitude": -88.11111,
        "active_route_miles_to_arrival": 19.83,
        "active_route_minutes_to_arrival": 34.13,
        "active_route_traffic_minutes_delay": 0.0,
        "gps_as_of": 1661641173,
        "heading": 182,
        "latitude": 33.111111,
        "longitude": -88.111111,
        "native_latitude": 33.111111,
        "native_location_supported": 1,
        "native_longitude": -88.111111,
        "native_type": "wgs",
        "power": -7,
        "shift_state": None,
        "speed": None,
        "timestamp": 1661641175268,
    },
    "gui_settings": {
        "gui_24_hour_time": False,
        "gui_charge_rate_units": "mi/hr",
        "gui_distance_units": "mi/hr",
        "gui_range_display": "Rated",
        "gui_temperature_units": "F",
        "show_range_units": True,
        "timestamp": 1661641175268,
    },
    "vehicle_config": {
        "can_accept_navigation_requests": True,
        "can_actuate_trunks": True,
        "car_special_type": "base",
        "car_type": "models",
        "charge_port_type": "US",
        "dashcam_clip_save_supported": False,
        "default_charge_to_max": False,
        "driver_assist": "MonoCam",
        "ece_restrictions": False,
        "efficiency_package": "Default",
        "eu_vehicle": False,
        "exterior_color": "White",
        "front_drive_unit": "NoneOrSmall",
        "has_air_suspension": False,
        "has_ludicrous_mode": False,
        "has_seat_cooling": False,
        "headlamp_type": "Hid",
        "interior_trim_type": "AllBlack",
        "motorized_charge_port": True,
        "plg": True,
        "pws": False,
        "rear_drive_unit": "Small",
        "rear_seat_heaters": 0,
        "rear_seat_type": 1,
        "rhd": False,
        "roof_color": "Colored",
        "seat_type": 1,
        "spoiler_type": "None",
        "sun_roof_installed": 0,
        "third_row_seats": "None",
        "timestamp": 1661641175269,
        "trim_badging": "85d",
        "use_range_badging": False,
        "utc_offset": -25200,
        "wheel_type": "Base19",
    },
    "vehicle_state": {
        "api_version": 36,
        "autopark_state_v2": "standby",
        "autopark_style": "standard",
        "calendar_supported": True,
        "car_version": "2022.8.10.1 171f0fe61c20",
        "center_display_state": 0,
        "dashcam_clip_save_available": False,
        "dashcam_state": "<invalid>",
        "df": 1,
        "dr": 0,
        "fd_window": 0,
        "feature_bitmask": "5,0",
        "fp_window": 0,
        "ft": 0,
        "homelink_device_count": 2,
        "homelink_nearby": True,
        "is_user_present": False,
        "last_autopark_error": "no_error",
        "locked": False,
        "media_state": {"remote_control_enabled": True},
        "notifications_supported": True,
        "odometer": 70915.596752,
        "parsed_calendar_supported": True,
        "pf": 0,
        "pr": 0,
        "rd_window": 0,
        "remote_start": False,
        "remote_start_enabled": True,
        "remote_start_supported": True,
        "rp_window": 0,
        "rt": 0,
        "santa_mode": 0,
        "smart_summon_available": False,
        "software_update": {
            "download_perc": 0,
            "expected_duration_sec": 2700,
            "install_perc": 1,
            "status": "available",
            "version": "2022.36.20",
        },
        "speed_limit_mode": {
            "active": False,
            "current_limit_mph": 85.0,
            "max_limit_mph": 90,
            "min_limit_mph": 50.0,
            "pin_code_set": False,
        },
        "summon_standby_mode_enabled": False,
        "timestamp": 1661641175268,
        "tpms_pressure_fl": 2.40,
        "tpms_pressure_fr": 2.58,
        "tpms_pressure_rl": 2.62,
        "tpms_pressure_rr": 2.71,
        "tpms_hard_warning_fl": False,
        "tpms_hard_warning_fr": False,
        "tpms_hard_warning_rl": False,
        "tpms_hard_warning_rr": False,
        "tpms_last_seen_pressure_time_fl": 1669639797,
        "tpms_last_seen_pressure_time_fr": 1669639800,
        "tpms_last_seen_pressure_time_rl": 1669639803,
        "tpms_last_seen_pressure_time_rr": 1669639806,
        "tpms_rcp_front_value": 2.9,
        "tpms_rcp_rear_value": 2.9,
        "tpms_soft_warning_fl": False,
        "tpms_soft_warning_fr": False,
        "tpms_soft_warning_rl": False,
        "tpms_soft_warning_rr": False,
        "valet_mode": False,
        "valet_pin_needed": False,
        "vehicle_name": "My Model S",
        "sentry_mode": True,
        "sentry_mode_available": True,
    },
}

VEHICLE = {
    "id": 12345678901234567,
    "user_id": 123,
    "vehicle_id": 1234567890,
    "vin": "5YJSA11111111111",
    "display_name": "My Model S",
    "option_codes": "MDLS,RENA,AF02,APF1,APH2,APPB,AU01,BC0R,BP00,BR00,BS00,CDM0,CH05,PBCW,CW00,DCF0,DRLH,DSH7,DV4W,FG02,FR04,HP00,IDBA,IX01,LP01,ME02,MI01,PF01,PI01,PK00,PS01,PX00,PX4D,QTVB,RFP2,SC01,SP00,SR01,SU01,TM00,TP03,TR00,UTAB,WTAS,X001,X003,X007,X011,X013,X021,X024,X027,X028,X031,X037,X040,X044,YFFC,COUS,P3WS",
    "color": None,
    "tokens": ["abcdef1234567890", "1234567890abcdef"],
    "state": "online",
    "in_service": False,
    "id_s": "12345678901234567",
    "calendar_enabled": True,
    "api_version": 7,
    "backseat_token": None,
    "backseat_token_updated_at": None,
    "drive_state": None,
    "climate_state": None,
    "charge_state": None,
    "gui_settings": None,
    "vehicle_state": None,
    "vehicle_config": {
        "can_accept_navigation_requests": True,
        "can_actuate_trunks": True,
        "car_special_type": "base",
        "car_type": "models",
        "charge_port_type": "US",
        "dashcam_clip_save_supported": False,
        "default_charge_to_max": False,
        "driver_assist": "MonoCam",
        "ece_restrictions": False,
        "efficiency_package": "Default",
        "eu_vehicle": False,
        "exterior_color": "White",
        "front_drive_unit": "NoneOrSmall",
        "has_air_suspension": False,
        "has_ludicrous_mode": False,
        "has_seat_cooling": False,
        "headlamp_type": "Hid",
        "interior_trim_type": "AllBlack",
        "motorized_charge_port": True,
        "plg": True,
        "pws": False,
        "rear_drive_unit": "Small",
        "rear_seat_heaters": 0,
        "rear_seat_type": 1,
        "rhd": False,
        "roof_color": "Colored",
        "seat_type": 1,
        "spoiler_type": "None",
        "sun_roof_installed": 0,
        "third_row_seats": "None",
        "timestamp": 1661641175269,
        "trim_badging": "85d",
        "use_range_badging": False,
        "utc_offset": -25200,
        "wheel_type": "Base19",
    },
}
