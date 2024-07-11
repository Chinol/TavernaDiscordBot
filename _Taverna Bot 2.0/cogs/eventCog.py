import discord
from discord.ext import commands
from discord import app_commands
from utils.config import TEST_SERVER
import utils.calendar as calendar
import asyncio

class EventCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="add_event", description="dodaj event do kalendarza")
    @app_commands.describe(nazwa = "Nazwa Event", data = "Data w formacie DD/MM")
    async def add(self, interaction: discord.Interaction, nazwa: str, data: str):
        
        if calendar.date_check(data) == False:
            await interaction.response.send_message("Podałeś złą datę, Proszę spróbuj jeszcze raz.Ta wiadomość zniknie za 5 sekund", ephemeral=True)
            for time in range(4, 0, -1):
                await asyncio.sleep(1)
                await interaction.edit_original_response(content = f"Podałeś złą datę, Proszę spróbuj jeszcze raz.Ta wiadomość zniknie za {time} sekund")
            await interaction.delete_original_response()
            return
        
        calendar.add_event(nazwa, data)
        
        await interaction.response.send_message(content="Dodano event, ta informacja zniknie za 5 sekund", ephemeral=True)
        
        for time in range(4, 0, -1):
                await asyncio.sleep(1)
                await interaction.edit_original_response(content = f"Dodano event, ta informacja zniknie za {time} sekund")
       
        await interaction.delete_original_response()
    
    @app_commands.command(name="clear_calendar", description="czyści kalendarz do 0")
    async def clear(self, interaction: discord.Interaction):
        
        calendar.clear_calendar()
        
        await interaction.response.send_message(content="Wyczyszczono kalendarz, ta informacja zniknie za 5 sekund", ephemeral=True)
        
        for time in range(4, 0, -1):
                await asyncio.sleep(1)
                await interaction.edit_original_response(content = f"Wyczyszczono kalendarz, ta informacja zniknie za {time} sekund")
        
        await interaction.delete_original_response()

async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(EventCog(bot), guild=TEST_SERVER)