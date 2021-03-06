import hikari
import time
from hikari.api.interaction_server import Response
from hikari.undefined import count
import lightbulb
from hikari.guilds import Guild, Role
from lightbulb.checks import has_role_permissions
from lightbulb.decorators import command

with open("./secrets/token") as token_read:
    _token = token_read.read().strip()

with open("./secrets/guild") as guild_read:
    _guild = int(guild_read.read())


bot = lightbulb.BotApp(
    token=_token, 
    default_enabled_guilds=_guild,
    intents=hikari.Intents.ALL
)

@bot.listen(hikari.StartedEvent)
async def on_start(event):
    print('Universal Kicker has started!')


@bot.command
@lightbulb.option('role', 'All users that are in this group will be kicked!', type=Role)
@lightbulb.command('kickrole', 'Kicks all users in a specific role.')
@lightbulb.implements(lightbulb.SlashCommand)
async def MassKick(ctx):

    kickedRole = ctx.options.role.mention

    for member in ctx.get_guild().get_members().values():
        if ctx.options.role in member.get_roles():
            await ctx.get_guild().kick(member, reason='The role you are in got cleaned from our server.')

            memberID = member.mention
            userRoleAmount = count(ctx.options.role in member.get_roles())

            await ctx.respond(f'The User {memberID} is being kicked because he is in the role {kickedRole}! | {userRoleAmount} left to kick')
            time.sleep(2)
        #else:
        #   await ctx.respond(f'No one left to kick in the {kickedRole} role!')  
        #break

bot.run()
