import aiohttp  
import random
import asyncio
from datetime import datetime, timedelta
import time

class Pokemon:
    pokemons = {}
    def __init__(self, pokemon_trainer):
        self.pokemon_trainer = pokemon_trainer
        self.pokemon_number = random.randint(1, 1000)
        self.name = None
        self.hp = None
        self.attack = None
        if pokemon_trainer not in Pokemon.pokemons:
            Pokemon.pokemons[pokemon_trainer] = self
        else:
            self = Pokemon.pokemons[pokemon_trainer]

    async def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'  
        async with aiohttp.ClientSession() as session:  
            async with session.get(url) as response:  
                if response.status == 200:
                    data = await response.json()  
                    return data['forms'][0]['name']  
                else:
                    return "Pikachu"  
    
    async def get_hp(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'  
        async with aiohttp.ClientSession() as session:  
            async with session.get(url) as response:  
                if response.status == 200:
                    data = await response.json()  
                    return data['stats'][0]['base_stat']  * 3
                else:
                    return 0  
                
    async def get_attack(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'  
        async with aiohttp.ClientSession() as session:  
            async with session.get(url) as response:  
                if response.status == 200:
                    data = await response.json()  
                    return data['stats'][1]['base_stat']  
                else:
                    return 0  

    async def info(self):
        if not self.name:
            self.name = await self.get_name()
            self.hp = await self.get_hp()
            self.attack = await self.get_attack()
            self.last_feed_time= datetime.now() 
        return f"Pokémonunuzun ismi: {self.name}\nPokémonunuzun Canı: {self.hp}\nPokémonunuzun Atağı: {self.attack}"  

    async def show_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'  
        async with aiohttp.ClientSession() as session:  
            async with session.get(url) as response:  
                if response.status == 200:
                    data = await response.json()  
                    return data['sprites']["other"]["home"]["front_default"]  
                else:
                    return None
                
    async def saldir(self, enemy):
        if isinstance(enemy, Mage):
            kalkan = random.randint(1,5)
            if kalkan == 1:
                return f"{self.name}, {enemy.name}'in kalkanını kıramadı.{enemy.name} hasar almadı"
        if enemy.hp > self.attack:
            enemy.hp -= self.attack
            return f"{self.name}, {enemy.name}'a saldırdı. {self.attack} hasar verdi.\n{enemy.name}'in kalan canı: {enemy.hp}"
        else:
            return f"{self.name}, {enemy.name}'a saldırdı.\n{enemy.name} yenildi"
        
    async def feed(self, beslemearalıgı = 20, canartısı = 10):
        simdikizaman = datetime.now()
        zamanaralıgı = timedelta(seconds=beslemearalıgı)
        if (simdikizaman-self.last_feed_time)> zamanaralıgı:
            self.hp += canartısı
            self.last_feed_time = simdikizaman
            return f"{self.name} Canı {canartısı} arttı"
        else:
            return f"{self.name} şu zaman besleye bilirsiniz: {simdikizaman + zamanaralıgı}"

class Warrior(Pokemon):
    async def saldir(self, enemy):
        bonus_attack = random.randint(1,20)
        self.attack += bonus_attack
        sonuc = await super().saldir(enemy)
        self.attack -= bonus_attack
        return f"{sonuc}\nBonus atak puanı: {bonus_attack}"
    async def feed(self, beslemearalıgı = 20, canartısı = 15):
        bonus= random.randint(1,20)
        canartısı += bonus 
        return await super().feed(beslemearalıgı,canartısı)

class Mage(Pokemon):
    async def feed (self, beslenmearalıgı= random.randint(5,15), canartısı = 10):
        return await super().feed(beslenmearalıgı,canartısı=canartısı)




if __name__ == "__main__":
    async def deneme():
        pokemon1 = Warrior("Ash")
        pokemon2 = Mage("Misty")


        print(await pokemon1.info())
        print("--------------------------------------")
        print(await pokemon2.info())
        print("--------------------------------------")
        print(await pokemon1.saldir(pokemon2))
        print("--------------------------------------")
        print(await pokemon2.saldir(pokemon1))
        print("--------------------------------------")
        time.sleep(21)
        print(await pokemon1.feed())
        print("--------------------------------------")
        print(await pokemon2.feed())

    asyncio.run(deneme())
