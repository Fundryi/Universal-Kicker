import os
import hikari
from hikari.api.interaction_server import Response
import lightbulb
import time
from hikari.guilds import Guild, Role
from lightbulb.checks import has_role_permissions
from lightbulb.decorators import command

with open("./secrets/token") as token_read:
    _token = token_read.read().strip()

with open("./secrets/guild") as guild_read:
    _guild = int(guild_read.read())


bot = lightbulb.BotApp(
    token=_token, 
    default_enabled_guilds=_guild
)

@bot.listen(hikari.StartedEvent)
async def on_start(event):
    print('Bot has started!')


@bot.command
@lightbulb.option('role', 'All users that are in this group will be kicked!', type=Role)
@lightbulb.command('role_kick', 'Kicks all users in a specific role.')
@lightbulb.implements(lightbulb.SlashCommand)
async def MassKick(ctx):
    for member in ctx.get_guild().get_members().values():
        if ctx.options.role in member.get_roles():
            await ctx.guild.kick(member, reason='There is no reason :)')
            await ctx.respond()

bot.run()
