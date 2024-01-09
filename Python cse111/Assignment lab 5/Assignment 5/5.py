class Pokemon:
    def __init__(self,a,b,c,d,e):
        self.pokemon1_name = a
        self.pokemon2_name = b
        self.pokemon1_power = c
        self.pokemon2_power = d
        self.damage_rate = e
team_pika = Pokemon("pikachu", "charmander", 90, 60, 10)
print("=======Team 1=======")
print("Pokemon 1:",team_pika.pokemon1_name, team_pika.pokemon1_power)
print("Pokemon 2:",team_pika.pokemon2_name, team_pika.pokemon2_power)
pika_combined_power = (team_pika.pokemon1_power + team_pika.pokemon2_power) * team_pika.damage_rate
print("Combined Power:", pika_combined_power)
team_bulb = Pokemon("bulbasaur","squirtle",80,70,9)
print("=======Team 2=======")
print("Pokemon 1:",team_bulb.pokemon1_name, team_bulb.pokemon1_power)
print("Pokemon 2:",team_bulb.pokemon2_name, team_bulb.pokemon2_power)
pika_combined_power2 = (team_bulb.pokemon1_power + team_bulb.pokemon2_power) * team_bulb.damage_rate
print("Combined Power:", pika_combined_power2)
