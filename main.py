import os
import json
import asyncio
import datetime
import time
import discord
import traceback
import sys
from discord.ext import commands
from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.table import Table
from rich.text import Text
from rich.live import Live
from rich.layout import Layout

# --- [SYSTEM CORE CONFIGURATION] ---
console = Console()
CONFIG_FILE = "h3r4_guardian_config.json"
START_TIME = time.time()
LOG_HISTORY = []
VERSION = "19.0"
CAPITAL = 1000.0

def load_db():
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, 'r') as f:
                data = json.load(f)
                keys = ["token", "mod_role_id", "mute_role_id", "custom_words", "responses"]
                for key in keys:
                    if key not in data: data[key] = [] if "id" not in key else ""
                return data
        except: pass
    return {"token": "", "mod_role_id": "", "mute_role_id": "", "custom_words": [], "responses": {}}

def save_db(data):
    try:
        with open(CONFIG_FILE, 'w') as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        add_log("DB_ERROR", str(e))

def add_log(event_type, details):
    timestamp = datetime.datetime.now().strftime("%H:%M:%S")
    log_entry = f"[[cyan]{timestamp}[/cyan]] [[bold yellow]{event_type}[/bold yellow]] {details}"
    LOG_HISTORY.append(log_entry)
    if len(LOG_HISTORY) > 15: LOG_HISTORY.pop(0)

# --- [GUI ELEMENTS] ---
BANNER_ART = r"""
  ⣠⣶⣶⣶⣤⣤⣄⡀      [H3R4 OMNIPOTENT V19.0]
 ⣼⣿⣿⣿⣿⣿⣿⣿⣿⣦     [STABILITY: SUPREME]
⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣶⣶⡄  [OPERATOR: REN.K_K]
⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟  [DATABASE: PROTECTED]
   ⢼⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⢻⣿⣿⠁   [CAPITAL : $1000]
"""

class H3R4_Guardian(commands.Bot):
    def __init__(self, db_config):
        intents = discord.Intents.all()
        super().__init__(command_prefix="?", intents=intents, help_command=None)
        self.db = db_config
        self.version = VERSION

    async def on_ready(self):
        add_log("SYSTEM", f"Kernel Active. Logged in as {self.user}")
        self.loop.create_task(self.refresh_gui())

    async def refresh_gui(self):
        with Live(self.render_screen(), refresh_per_second=2) as live:
            while not self.is_closed():
                live.update(self.render_screen())
                await asyncio.sleep(1)

    def render_screen(self):
        uptime = str(datetime.timedelta(seconds=int(time.time() - START_TIME)))
        header = Panel(Align.center(f"[bold red]{BANNER_ART}[/bold red]"), border_style="red")
        log_text = Text.from_markup("\n".join(LOG_HISTORY))
        body = Panel(log_text, title="[bold cyan]REAL-TIME KERNEL LOGS[/bold cyan]", border_style="cyan")
        footer = Panel(Align.center(f"[bold white]UPTIME: {uptime} | VERSION: {VERSION} | CAPITAL: ${CAPITAL}[/bold white]"), border_style="white")
        layout = Layout()
        layout.split_column(Layout(header, size=11), Layout(body, size=18), Layout(footer, size=3))
        return layout

    async def on_message(self, message):
        if message.author.bot or not message.guild: return
        
        content = message.content.lower().strip()
        author = message.author
        
        # SENSOR & AUTO-RESP
        responses = self.db.get("responses", {})
        if content in responses:
            await message.channel.send(responses[content])
            add_log("AUTO-RESP", f"{author.name} triggered '{content}'")

        mod_id = str(self.db.get("mod_role_id", ""))
        is_mod = author.guild_permissions.administrator or any(str(r.id) == mod_id for r in author.roles)

        if not is_mod:
            for word in self.db.get("custom_words", []):
                if word.lower() in content:
                    try:
                        await message.delete()
                        add_log("SECURITY", f"Deleted bad word from {author.name}")
                        return
                    except: pass
        
        await self.process_commands(message)

# --- [COMMANDS REGISTRATION] ---

def register_all_commands(bot):

    # --- [SUPREME HELP INTERFACE] ---
    @bot.command()
    async def help(ctx):
        add_log("COMMAND", f"{ctx.author.name} requested Help Menu")
        embed = discord.Embed(
            title="🛡️ H3R4 OMNIPOTENT COMMAND CENTER",
            description="Welcome, Operator. All systems are calibrated and secure.",
            color=0xff0000,
            timestamp=datetime.datetime.now()
        )
        
        # Security & Lockdown
        embed.add_field(
            name="🚨 [PROTECTION PROTOCOLS]",
            value=(
                "`?emergency` - Lockdown seluruh server\n"
                "`?unemergency` - Pulihkan akses seluruh server\n"
                "`?lock` - Kunci channel ini saja\n"
                "`?unlock` - Buka channel ini saja"
            ),
            inline=False
        )
        
        # Moderation
        embed.add_field(
            name="⚖️ [MODERATION SYSTEM]",
            value=(
                "`?kick @user [reason]` - Keluarkan user\n"
                "`?ban @user [reason]` - Ban permanen user\n"
                "`?purge [n]` - Bersihkan pesan massal\n"
                "`?mute @user` - Mute user (Mod Role Only)"
            ),
            inline=False
        )
        
        # Configuration
        embed.add_field(
            name="⚙️ [DATABASE CONFIG]",
            value=(
                "`?addword [kata]` - Tambah blacklist kata\n"
                "`?listword` - Lihat blacklist kata saat ini\n"
                "`?addresp [trig] | [resp]` - Set auto-response\n"
                "`?delresp [trig]` - Hapus auto-response"
            ),
            inline=False
        )
        
        # Information
        embed.add_field(
            name="🔍 [INTEL & SYSTEM]",
            value=(
                "`?userinfo @user` - Detail data user\n"
                "`?ping` - Cek latensi koneksi\n"
                "`?uptime` - Waktu aktif sistem"
            ),
            inline=False
        )
        
        embed.set_thumbnail(url=ctx.bot.user.display_avatar.url)
        embed.set_footer(text=f"H3R4 OMNIPOTENT V{VERSION} | Capital: ${CAPITAL}", icon_url=ctx.author.display_avatar.url)
        await ctx.send(embed=embed)

    # --- [MODERATION COMMANDS] ---
    @bot.command()
    @commands.has_permissions(kick_members=True)
    async def kick(ctx, member: discord.Member, *, reason="Violating rules"):
        await member.kick(reason=reason)
        add_log("MOD", f"KICK: {member.name}")
        await ctx.send(f"👢 **{member.name}** has been kicked. Reason: `{reason}`")

    @bot.command()
    @commands.has_permissions(ban_members=True)
    async def ban(ctx, member: discord.Member, *, reason="Violating rules"):
        await member.ban(reason=reason)
        add_log("MOD", f"BAN: {member.name}")
        await ctx.send(f"🔨 **{member.name}** has been banned. Reason: `{reason}`")

    @bot.command()
    @commands.has_permissions(manage_messages=True)
    async def purge(ctx, amount: int):
        deleted = await ctx.channel.purge(limit=amount + 1)
        add_log("MOD", f"PURGE: {len(deleted)-1} messages")
        await ctx.send(f"🧹 Purged `{len(deleted)-1}` messages.", delete_after=3)

    # --- [CHANNEL SECURITY] ---
    @bot.command()
    @commands.has_permissions(manage_channels=True)
    async def lock(ctx):
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
        add_log("SECURITY", f"LOCKED: #{ctx.channel.name}")
        await ctx.send("🔒 **Channel Locked.**")

    @bot.command()
    @commands.has_permissions(manage_channels=True)
    async def unlock(ctx):
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
        add_log("SECURITY", f"UNLOCKED: #{ctx.channel.name}")
        await ctx.send("🔓 **Channel Unlocked.**")

    @bot.command()
    @commands.has_permissions(administrator=True)
    async def emergency(ctx):
        for c in ctx.guild.text_channels:
            try: await c.set_permissions(ctx.guild.default_role, send_messages=False)
            except: continue
        add_log("EMERGENCY", "GLOBAL LOCKDOWN")
        await ctx.send("🚨 **GLOBAL LOCKDOWN ACTIVATED.**")

    @bot.command()
    @commands.has_permissions(administrator=True)
    async def unemergency(ctx):
        for c in ctx.guild.text_channels:
            try: await c.set_permissions(ctx.guild.default_role, send_messages=None)
            except: continue
        add_log("EMERGENCY", "GLOBAL RESTORE")
        await ctx.send("🔓 **SERVER RESTORED.**")

    # --- [DATABASE COMMANDS] ---
    @bot.command()
    @commands.has_permissions(administrator=True)
    async def addword(ctx, *, word: str):
        w = word.lower().strip()
        if w not in bot.db["custom_words"]:
            bot.db["custom_words"].append(w); save_db(bot.db)
            add_log("DB", f"Added word: {w}")
            await ctx.send(f"✅ `{w}` added to filter.")

    @bot.command()
    async def listword(ctx):
        words = ", ".join(bot.db["custom_words"]) or "Empty"
        await ctx.send(f"📋 **Filter:** `{words}`")

    @bot.command()
    @commands.has_permissions(administrator=True)
    async def addresp(ctx, *, pair: str):
        try:
            t, r = pair.split("|")
            bot.db["responses"][t.strip().lower()] = r.strip()
            save_db(bot.db); add_log("DB", f"Added Response: {t.strip()}")
            await ctx.send(f"✅ Response for `{t.strip()}` active.")
        except: await ctx.send("Format: `?addresp keyword | answer`")

    @bot.command()
    @commands.has_permissions(administrator=True)
    async def delresp(ctx, *, trigger: str):
        t = trigger.lower().strip()
        if t in bot.db["responses"]:
            del bot.db["responses"][t]; save_db(bot.db)
            add_log("DB", f"Deleted Response: {t}")
            await ctx.send(f"🗑️ `{t}` deleted.")

    # --- [SYSTEM INFO] ---
    @bot.command()
    async def userinfo(ctx, member: discord.Member = None):
        m = member or ctx.author
        embed = discord.Embed(title=f"User Intelligence: {m.name}", color=m.color)
        embed.add_field(name="ID", value=m.id)
        embed.add_field(name="Account Created", value=m.created_at.strftime("%d %b %Y"))
        embed.set_thumbnail(url=m.display_avatar.url)
        await ctx.send(embed=embed)

    @bot.command()
    async def ping(ctx): await ctx.send(f"🏓 Latency: `{round(bot.latency * 1000)}ms`")

    @bot.command()
    async def uptime(ctx):
        delta = datetime.timedelta(seconds=int(time.time() - START_TIME))
        await ctx.send(f"⏱️ **System Uptime:** `{str(delta)}`")

# --- [PANEL INTERFACE] ---
def show_panel():
    while True:
        os.system('clear' if os.name == 'posix' else 'cls')
        db = load_db()
        table = Table(title="H3R4 OMNIPOTENT MANAGEMENT PANEL", expand=True)
        table.add_column("No", style="cyan", justify="center")
        table.add_column("Setting", style="white")
        table.add_column("Value", style="green")
        table.add_row("1", "Bot Token", "SET" if db["token"] else "[red]EMPTY[/red]")
        table.add_row("2", "Mod Role ID", db["mod_role_id"] or "[red]NOT SET[/red]")
        table.add_row("3", "Mute Role ID", db["mute_role_id"] or "[red]NOT SET[/red]")
        table.add_row("4", "DATABASE STATUS", "[bold yellow]STABLE[/bold yellow]")
        table.add_row("5", "[bold green]START SYSTEM[/bold green]", "READY")
        table.add_row("6", "Exit", "SHUTDOWN")
        console.print(Panel(Align.center(f"[bold red]{BANNER_ART}[/bold red]"), border_style="red"))
        console.print(table)
        c = input("\n$> ")
        if c == '1': db["token"] = input("Token: "); save_db(db)
        elif c == '2': db["mod_role_id"] = input("Mod ID: "); save_db(db)
        elif c == '3': db["mute_role_id"] = input("Mute ID: "); save_db(db)
        elif c == '4': 
            if input("Confirm Reset DB? (y/n): ") == 'y': os.remove(CONFIG_FILE)
        elif c == '5':
            if db["token"]: return db
        elif c == '6': sys.exit()

if __name__ == "__main__":
    db = show_panel()
    bot = H3R4_Guardian(db)
    register_all_commands(bot)
    try:
        bot.run(db["token"])
    except Exception as e:
        print(f"FATAL ERROR: {e}")
        time.sleep(10)
