
# ==============================================================================
# 🛡️ H3R4 OMNIPOTENT KERNEL V25.0 (SUPREME TITAN EDITION)
# ==============================================================================
# INTEGRATED MODULES:
# - Advanced Protection (Emergency, Lockdown, Global Restore)
# - Smart Moderation (Strike System, Auto-Mute, Kick, Ban, Purge)
# - Dynamic Database (Auto-Response, Blacklist Word, Config Sync)
# - Real-Time GUI (Rich Terminal, Live Logs, Latency Guard)
# ==============================================================================

import os
import json
import asyncio
import datetime
import time
import discord
import sys
import traceback
import logging
from discord.ext import commands, tasks
from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.table import Table
from rich.text import Text
from rich.live import Live
from rich.layout import Layout

# --- [1. GLOBAL CORE CONFIGURATION] ---
VERSION = "25.0"
CONFIG_FILE = "h3r4_guardian_config.json"
START_TIME = time.time()
LOG_HISTORY = []
console = Console()

def init_db():
    """Memastikan integritas database dengan fail-safe defaults."""
    default_structure = {
        "token": "",
        "mod_role_id": "",
        "mute_role_id": "",
        "custom_words": [],
        "responses": {},
        "emergency_mode": False
    }
    if not os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'w') as f:
            json.dump(default_structure, f, indent=4)
        return default_structure
    
    try:
        with open(CONFIG_FILE, 'r') as f:
            data = json.load(f)
            # Validasi setiap key agar tidak ada KeyError saat runtime
            for key, value in default_structure.items():
                if key not in data:
                    data[key] = value
            return data
    except Exception as e:
        print(f"DATABASE CORRUPTION DETECTED: {e}")
        return default_structure

def save_db(data):
    """Menyimpan data dengan sinkronisasi instan ke disk."""
    try:
        with open(CONFIG_FILE, 'w') as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        add_log("DB_SYNC_FAIL", f"Error saving: {str(e)}")

def add_log(event_type, details):
    """Sistem logging visual untuk Rich Terminal GUI."""
    ts = datetime.datetime.now().strftime("%H:%M:%S")
    log_entry = f"[[cyan]{ts}[/cyan]] [[bold yellow]{event_type}[/bold yellow]] {details}"
    LOG_HISTORY.append(log_entry)
    if len(LOG_HISTORY) > 22:
        LOG_HISTORY.pop(0)

# --- [2. VISUAL GUI ENGINE] ---
BANNER_ART = r"""
  ⣠⣶⣶⣶⣤⣤⣄⡀      [H3R4 OMNIPOTENT V25.0]
 ⣼⣿⣿⣿⣿⣿⣿⣿⣿⣦     [STABILITY: SUPREME]
⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣶⣶⡄  [OPERATOR: REN.K_K]
⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟  [MUTE SYS : ACTIVE]
   ⢼⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⢻⣿⣿⠁   [VERSION  : 25.0]
"""

class H3R4_Titan_Core(commands.Bot):
    def __init__(self, db_config):
        intents = discord.Intents.all()
        super().__init__(command_prefix="?", intents=intents, help_command=None)
        self.db = db_config
        self.strike_map = {}
        self.start_timestamp = time.time()

    async def setup_hook(self):
        """Inisialisasi task background."""
        add_log("BOOT", "Initializing Titanium Kernel Hooks...")
        self.loop.create_task(self.terminal_gui_task())

    async def terminal_gui_task(self):
        """Looping update terminal secara asinkron."""
        with Live(self.generate_layout(), refresh_per_second=2) as live:
            while not self.is_closed():
                try:
                    live.update(self.generate_layout())
                except:
                    pass
                await asyncio.sleep(1)

    def generate_layout(self):
        """Membangun visual dashboard terminal."""
        try:
            uptime = str(datetime.timedelta(seconds=int(time.time() - self.start_timestamp)))
            
            # LATENCY GUARD (Anti-NaN Crash)
            if self.latency is None or str(self.latency) == "nan":
                ping_display = "[bold yellow]SYNCING...[/bold yellow]"
            else:
                ping_display = f"[bold green]{round(self.latency * 1000)}ms[/bold green]"

            header = Panel(Align.center(f"[bold red]{BANNER_ART}[/bold red]"), border_style="red")
            
            log_content = "\n".join(LOG_HISTORY)
            body = Panel(Text.from_markup(log_content), title="[bold cyan]REAL-TIME ACTIVITY LOG[/bold cyan]", border_style="cyan")
            
            status_line = f"UPTIME: {uptime} | PING: {ping_display} | V: {VERSION} | STATUS: [bold green]ONLINE[/bold green]"
            footer = Panel(Align.center(status_line), border_style="white")
            
            layout = Layout()
            layout.split_column(
                Layout(header, size=11),
                Layout(body, size=24),
                Layout(footer, size=3)
            )
            return layout
        except Exception as e:
            return Panel(f"GUI Rendering Error: {e}", border_style="red")

    # --- [3. CORE MESSAGE INTERCEPTOR] ---
    async def on_message(self, message):
        # Abaikan Bot dan DM
        if message.author.bot or not message.guild:
            return

        author = message.author
        content_raw = message.content.strip()
        content_lower = content_raw.lower()
        
        # 3.1 AUTO-RESPONSE MODULE (Exact Match)
        responses = self.db.get("responses", {})
        if content_lower in responses:
            try:
                await message.channel.send(responses[content_lower])
                add_log("RESPONSE", f"Triggered: '{content_lower}' by {author.name}")
            except Exception as e:
                add_log("ERR_SEND", str(e))

        # 3.2 MODERATOR BYPASS CHECK
        mod_role_id = str(self.db.get("mod_role_id", ""))
        is_mod = (author.guild_permissions.administrator or 
                  any(str(r.id) == mod_role_id for r in author.roles))

        # 3.3 PROTECTION MODULE: WORD FILTER & STRIKES
        if not is_mod:
            blacklist = self.db.get("custom_words", [])
            for bad_word in blacklist:
                if bad_word.lower() in content_lower:
                    await self.handle_security_violation(message, author)
                    return # Stop processing commands if message is deleted

        # 3.4 PROCESS COMMANDS
        await self.process_commands(message)

    async def handle_security_violation(self, message, author):
        """Menangani strike dan mute otomatis."""
        try:
            await message.delete()
            uid = str(author.id)
            self.strike_map[uid] = self.strike_map.get(uid, 0) + 1
            strikes = self.strike_map[uid]
            
            add_log("SECURITY", f"Strike {strikes}/3 for {author.name}")

            if strikes >= 3:
                await self.apply_auto_mute(message, author)
            else:
                emb = discord.Embed(
                    title="⚠️ ATURAN SERVER",
                    description=f"{author.mention}, pesan kamu dihapus karena kata terlarang.\n**Strike: `{strikes}/3`**\n(3 Strike = Mute Otomatis)",
                    color=0xffcc00
                )
                warn = await message.channel.send(embed=emb)
                await asyncio.sleep(4)
                await warn.delete()
        except discord.Forbidden:
            add_log("PERM_ERR", "Bot lacks permission to delete/mute.")
        except Exception as e:
            add_log("SEC_ERR", str(e))

    async def apply_auto_mute(self, message, author):
        """Eksekusi pemberian role mute."""
        mute_id = self.db.get("mute_role_id", "")
        if not mute_id:
            await message.channel.send("⚠️ **CRITICAL:** ID Role Mute belum di-set di panel!")
            return
        
        try:
            role = message.guild.get_role(int(mute_id))
            if role:
                await author.add_roles(role, reason="H3R4 Strike System: Max Violations")
                self.strike_map[str(author.id)] = 0 # Reset strike
                emb = discord.Embed(
                    title="🚫 USER MUTED",
                    description=f"{author.mention} telah di-mute otomatis karena mencapai batas strike.",
                    color=0xff0000
                )
                await message.channel.send(embed=emb)
                add_log("MOD", f"Muted: {author.name} (Max Strikes)")
            else:
                add_log("ERROR", "Role Mute tidak ditemukan di server.")
        except Exception as e:
            add_log("MOD_ERR", f"Mute failed: {str(e)}")

# --- [4. TITANIUM COMMANDS REPOSITORY] ---

bot_kernel = H3R4_Titan_Core(init_db())

# -- [4.1 SYSTEM INFO COMMANDS] --
@bot_kernel.command()
async def help(ctx):
    add_log("COMMAND", f"{ctx.author.name} opened Help")
    embed = discord.Embed(
        title="🛡️ H3R4 OMNIPOTENT COMMAND CENTER",
        description="Pusat kendali kernel perlindungan server.",
        color=0xff0000,
        timestamp=datetime.datetime.now()
    )
    embed.add_field(name="🚨 [PROTECTION]", value="`?lock`, `?unlock`, `?emergency`, `?unemergency`", inline=False)
    embed.add_field(name="⚖️ [MODERATION]", value="`?kick`, `?ban`, `?purge`, `?strikes`", inline=False)
    embed.add_field(name="⚙️ [DATABASE]", value="`?addword`, `?listword`, `?addresp`, `?delresp`", inline=False)
    embed.add_field(name="🔍 [INTEL]", value="`?userinfo`, `?ping`, `?uptime`", inline=False)
    embed.set_thumbnail(url=bot_kernel.user.display_avatar.url)
    embed.set_footer(text=f"Kernel V{VERSION} | Operator: ren.k_k")
    await ctx.send(embed=embed)

@bot_kernel.command()
async def ping(ctx):
    await ctx.send(f"📡 Kernel Latency: `{round(bot_kernel.latency * 1000)}ms`")

@bot_kernel.command()
async def uptime(ctx):
    delta = datetime.timedelta(seconds=int(time.time() - START_TIME))
    await ctx.send(f"⏱️ **System Uptime:** `{str(delta)}`")

# -- [4.2 PROTECTION & SECURITY COMMANDS] --
@bot_kernel.command()
@commands.has_permissions(administrator=True)
async def emergency(ctx):
    """Mengunci seluruh channel teks di server."""
    await ctx.send("🚨 **GLOBAL LOCKDOWN INITIATED...**")
    count = 0
    for channel in ctx.guild.text_channels:
        try:
            await channel.set_permissions(ctx.guild.default_role, send_messages=False)
            count += 1
        except: continue
    add_log("EMERGENCY", f"Global Lockdown: {count} channels")
    await ctx.send(f"🚨 **SERVER LOCKED.** `{count}` channel berhasil diamankan.")

@bot_kernel.command()
@commands.has_permissions(administrator=True)
async def unemergency(ctx):
    """Membuka kembali seluruh channel."""
    await ctx.send("🔓 **GLOBAL RESTORE IN PROGRESS...**")
    count = 0
    for channel in ctx.guild.text_channels:
        try:
            await channel.set_permissions(ctx.guild.default_role, send_messages=None)
            count += 1
        except: continue
    add_log("EMERGENCY", f"Global Restore: {count} channels")
    await ctx.send(f"🔓 **SERVER RESTORED.** `{count}` channel dibuka kembali.")

@bot_kernel.command()
@commands.has_permissions(manage_channels=True)
async def lock(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
    add_log("SECURITY", f"Channel {ctx.channel.name} Locked")
    await ctx.send("🔒 **Channel ini telah dikunci.**")

@bot_kernel.command()
@commands.has_permissions(manage_channels=True)
async def unlock(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=None)
    add_log("SECURITY", f"Channel {ctx.channel.name} Unlocked")
    await ctx.send("🔓 **Channel ini telah dibuka.**")

# -- [4.3 MODERATION COMMANDS] --
@bot_kernel.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason="Violating Rules"):
    await member.kick(reason=reason)
    add_log("MOD", f"Kicked: {member.name}")
    await ctx.send(f"👢 **{member.name}** telah dikeluarkan. Alasan: `{reason}`")

@bot_kernel.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason="Violating Rules"):
    await member.ban(reason=reason)
    add_log("MOD", f"Banned: {member.name}")
    await ctx.send(f"🔨 **{member.name}** telah di-ban permanen. Alasan: `{reason}`")

@bot_kernel.command()
@commands.has_permissions(manage_messages=True)
async def purge(ctx, amount: int):
    if amount > 100: amount = 100
    deleted = await ctx.channel.purge(limit=amount + 1)
    add_log("MOD", f"Purged {len(deleted)-1} messages")
    await ctx.send(f"🧹 `{len(deleted)-1}` pesan dibersihkan.", delete_after=3)

@bot_kernel.command()
async def strikes(ctx, member: discord.Member = None):
    target = member or ctx.author
    s = bot_kernel.strike_map.get(str(target.id), 0)
    await ctx.send(f"📊 Strike untuk **{target.name}**: `{s}/3` pelanggaran.")

# -- [4.4 DATABASE & CONFIG COMMANDS] --
@bot_kernel.command()
@commands.has_permissions(administrator=True)
async def addword(ctx, *, word: str):
    w = word.lower().strip()
    if w not in bot_kernel.db["custom_words"]:
        bot_kernel.db["custom_words"].append(w)
        save_db(bot_kernel.db)
        add_log("DB", f"New Filter: {w}")
        await ctx.send(f"✅ Kata `{w}` berhasil masuk daftar hitam.")
    else:
        await ctx.send("❌ Kata tersebut sudah ada di daftar.")

@bot_kernel.command()
async def listword(ctx):
    words = ", ".join(bot_kernel.db["custom_words"]) or "Kosong"
    await ctx.send(f"📋 **Filter Saat Ini:** `{words}`")

@bot_kernel.command()
@commands.has_permissions(administrator=True)
async def addresp(ctx, *, data: str):
    """Format: ?addresp pemicu | jawaban"""
    try:
        if "|" not in data:
            return await ctx.send("❌ Gunakan format: `?addresp pemicu | jawaban`")
        trigger, response = data.split("|", 1)
        trigger = trigger.strip().lower()
        bot_kernel.db["responses"][trigger] = response.strip()
        save_db(bot_kernel.db)
        add_log("DB", f"Set Resp: {trigger}")
        await ctx.send(f"✅ Bot akan menjawab `{trigger}` dengan `{response.strip()}`.")
    except Exception as e:
        await ctx.send(f"❌ Terjadi kesalahan: {e}")

@bot_kernel.command()
@commands.has_permissions(administrator=True)
async def delresp(ctx, *, trigger: str):
    t = trigger.lower().strip()
    if t in bot_kernel.db["responses"]:
        del bot_kernel.db["responses"][t]
        save_db(bot_kernel.db)
        add_log("DB", f"Deleted Resp: {t}")
        await ctx.send(f"🗑️ Respon untuk `{t}` telah dihapus.")
    else:
        await ctx.send("❌ Respon tidak ditemukan.")

@bot_kernel.command()
async def userinfo(ctx, member: discord.Member = None):
    m = member or ctx.author
    embed = discord.Embed(title=f"User Intelligence: {m.name}", color=m.color)
    embed.add_field(name="ID", value=m.id)
    embed.add_field(name="Account Created", value=m.created_at.strftime("%d %b %Y"))
    embed.add_field(name="Server Joined", value=m.joined_at.strftime("%d %b %Y"))
    embed.set_thumbnail(url=m.display_avatar.url)
    await ctx.send(embed=embed)

# --- [5. DYNAMIC MANAGEMENT PANEL] ---

def launch_bootstrap_panel():
    """Panel interaktif sebelum masuk ke kernel Discord."""
    while True:
        try:
            os.system('clear' if os.name == 'posix' else 'cls')
            db = init_db()
            
            table = Table(title="H3R4 TITANIUM MANAGEMENT PANEL", expand=True, border_style="red")
            table.add_column("ID", justify="center", style="cyan")
            table.add_column("CONFIGURATION", style="white")
            table.add_column("VALUE/STATUS", style="bold green")
            
            table.add_row("1", "Discord Bot Token", "READY" if db["token"] else "[red]EMPTY[/red]")
            table.add_row("2", "Moderator Role ID", db["mod_role_id"] if db["mod_role_id"] else "[yellow]NOT SET[/yellow]")
            table.add_row("3", "Mute Role ID", db["mute_role_id"] if db["mute_role_id"] else "[yellow]NOT SET[/yellow]")
            table.add_row("4", "Blacklist Filter", f"{len(db['custom_words'])} Kata Aktif")
            table.add_row("5", "Auto-Responses", f"{len(db['responses'])} Respon Aktif")
            table.add_row("L", "[bold green]LAUNCH TITAN KERNEL[/bold green]", "READY")
            table.add_row("X", "EXIT SYSTEM", "SHUTDOWN")
            
            console.print(Panel(Align.center(f"[bold red]{BANNER_ART}[/bold red]"), border_style="red"))
            console.print(table)
            
            choice = input("\n[H3R4]$> ").upper()
            
            if choice == '1':
                db["token"] = input("Masukkan Token Bot: ")
                save_db(db)
            elif choice == '2':
                db["mod_role_id"] = input("Masukkan ID Role Moderator: ")
                save_db(db)
            elif choice == '3':
                db["mute_role_id"] = input("Masukkan ID Role Mute: ")
                save_db(db)
            elif choice == 'L':
                if not db["token"]:
                    print("ERROR: Token tidak boleh kosong!"); time.sleep(2)
                    continue
                return db
            elif choice == 'X':
                sys.exit()
        except KeyboardInterrupt:
            sys.exit()

# --- [6. KERNEL EXECUTION START] ---
if __name__ == "__main__":
    current_db = launch_bootstrap_panel()
    
    # Inject data ke instance bot
    bot_kernel.db = current_db
    
    try:
        # Jalankan bot dengan token dari database
        bot_kernel.run(current_db["token"])
    except discord.LoginFailure:
        print("\n[FATAL]: Token Bot Salah atau Invalid!")
        time.sleep(5)
    except Exception as fatal:
        print(f"\n[FATAL KERNEL CRASH]: {fatal}")
        traceback.print_exc()
        time.sleep(10)
