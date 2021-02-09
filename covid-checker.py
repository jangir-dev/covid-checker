import covid

covid = covid.Covid()
country = input("Country name (en): ")

country_list = covid.get_data()

try:
	data = covid.get_status_by_country_name(country)
	print(f"Confirmed cases: {data['confirmed']}")
	print(f"Active cases: {data['active']}")
	print(f"Total deaths: {data['deaths']}")
	print(f"Recovered: {data['recovered']}")

except ValueError:
	print("Oops, seems something went wrong.. Please retype country name.\n")

	for i in country_list:
		print(i['country'], end=" ")