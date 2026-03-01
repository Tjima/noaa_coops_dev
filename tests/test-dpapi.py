from noaa_coops import Station
s= Station(1611400)
df = s.get_derived_product("toptenwaterlevels", station_id="1611400", datum="MHHW", units="metric")
print(df)
