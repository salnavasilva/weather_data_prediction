

class solar_panel:
    
    def __init__(self, id_panel, date_fab_panel, name_model, price_panel, solar_sys_output_kWh, height_m, length_m, useful_life_years, annual_degradation_rate):
        self.id_panel = id_panel
        self.date_fab_panel = date_fab_panel
        self.name_model = name_model
        self.price_panel = price_panel
        self.solar_sys_output_kWh = solar_sys_output_kWh
        self.height_m = height_m
        self.length_m = length_m
        self.useful_life_years = useful_life_years
        self.annual_degradation_rate = annual_degradation_rate

    def panel_size(self):
        return self.height_m * self.length_m
    
    def __str__(self):
        return f"--> Solar panel ID : {self.id_panel} \n--> model : {self.name_model}"

class panel_installation(solar_panel):
    def __init__(self, id_installation, panels_group = None):
        super().__init__(price_panel, solar_sys_output_kWh, height_m, length_m)
        self.id_installation = id_installation

        if panels_group is None:
            self.panels_group = []
        else:
            self.panels_group = panels_group

    def add_panel_to_group(self, individual_panel):
        if individual_panel not in self.panels_group:
            self.panels_group.append(individual_panel)
        else:
            print("Already in panels_group")

    def remove_panel_from_group(self, individual_panel):
        if individual_panel in self.panels_group:
            self.panels_group.remove(individual_panel)
        else:
            print("Not in panels_group")
    
    def show_panels_group(self):
        print(self.panels_group)




if __name__ == "__main__":
    
    solar_1 = solar_panel("0001", "2024-06-01", "SP-600", 2000, 9, 2, 3, 5, 0.05)
    print(solar_1)
    print(solar_1.__dict__)
    print(solar_1.panel_size())

    panel_installation_1 = panel_installation(id_installation= "PI_001")
    print(panel_installation_1)


    