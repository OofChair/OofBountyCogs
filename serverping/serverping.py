from typing import Literal
from simple_ping import Ping

import discord
from redbot.core import commands
from redbot.core.bot import Red
from redbot.core.config import Config

RequestType = Literal["discord_deleted_user", "owner", "user", "user_strict"]

__version__ = "0.0.1"


class ServerPing(commands.Cog):
    """
    Ping a server.
    """

    def __init__(self, bot: Red) -> None:
        self.bot = bot
        self.config = Config.get_conf(
            self,
            identifier=572944636209922059,
            force_registration=True,
        )

    async def red_delete_data_for_user(
        self, *, requester: RequestType, user_id: int
    ) -> None:
        # TODO: Replace this with the proper end user data removal handling.
        super().red_delete_data_for_user(requester=requester, user_id=user_id)

    @commands.command()
    async def serverping(self, ctx, server):
        """Ping a server or an IP. \n\n**Pinging a specific port will not work. This is due to restrictions with the lib.**"""
        ping = Ping(server)
        embed = discord.Embed(title=f"Pinged {server}!")
        embed = discord.Embed(color=(await ctx.embed_colour()))
        embed.add_field(
            name=f"Server returned {ping.avg} ms!",
            value=f"It returned {ping.returncode} error(s)!",
            inline=False,
        )
        embed.set_footer(text=f"I pinged {server}")
        await ctx.send(embed=embed)

    @commands.command()
    async def pingversion(self, ctx):
        """Check what version the cog is on."""
        await ctx.send(f"This cog is on version {__version__}.")


# Ping avg return: {ping.avg}
# Ping errors return: {ping.returncode}
