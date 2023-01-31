import discord
from discord import app_commands

import json
#import webserver
import chess
import random
import os
from googletrans import Translator
#おじさんには原因がわからなかったのでここはほのかのちゃんに丸投げするで候
#デフェフェフェフェ♪
r = open('config.json', 'r')
load = json.load(r)


class FixReplyDict:
  msg = ""
  reply = ""


intents = discord.Intents.default()
intents.members = True
intents.message_content = True

client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


def simple_embed(title, description):
  embed = discord.Embed()
  embed.colour = int("f0f8ff", 16)
  embed.title = title
  embed.description = description
  return embed


@client.event
async def on_ready():
  print(f"正常に起動しました\nログイン:{client.user}")
  print('We have logged in as {0.user}'.format(client))

  await tree.sync()


@client.event
async def on_message(message):
    if message.content == 'op.cleanup':
        if message.author.guild_permissions.administrator:
            await message.channel.purge()
            await message.channel.send('log is fired')
        else:
            await message.channel.send('消えた')
    
    if message in "もやし":
      await message.channel.send("もやぁ？")
    if message in "ひまたく": 
      await message.channel.send("ひまたく！！")
    if message in "エクミル": 
       await message.channel.send("それ誰？")   
    if message in "なんで？": 
       await message.channel.send("わかんない")   
    if message == "は？": 
        await message.channel.send("なに？")   
    if message in "おはよう": 
        await message.channel.send("おはよ～")
    if message in "ゆかりボット":
        await message.channel.send("一部の機能はゆかりボットから流用しています。ゆかりボットを作成したもやしさんとひまたくさんに深く感謝いたします")
    if 'yu!' in message or 'yukari!' in message or 'y!' in message:
        await message.channel.send('コマンド発動！')
    meirei = message.split(' ')
    rei = meirei[0]
    print(rei)
    if 'help' in rei:
      await message.channel.send('```help ヘルプコマンド\nsay <message> 喋れる\nranodm <count> <to count> ～から～までの範囲をランダムに出せる\ndon <coin> <count> さいころカジノです。１から６までの数字を指定して当てます。\nhonyaku　<message> 翻訳です。間違ってる可能性あるので仕方ないです。```')
    if 'say' in rei:
      c1 = meirei[1:]
      say = ' '.join(c1)
      await message.channel.send(say)
    if 'random' in rei:
      to1 = int(meirei[1])
      to2 = int(meirei[2])
      par = random.randint(to1,to2)
      await message.channel.send(par)
    if 'don' in rei:
      coin = int(meirei[1])
      ta = int(meirei[2])
      if 0 < ta < 7:
        par = random.randint(1,6)
        point =- coin
        if ta == par:
          point =+ coin * 2
        await message.channel.send('目標は' + str(ta) + 'で答えは' + str(par) + 'です！\n金額は' + str(point) + 'になったよ。')
      else:
        await message.channel.send('エラーです。\nさいころは１から６までです。')
    if 'honyaku' in rei:
      message = meirei[1:]
      coment = ' '.join(message)
      #coment = coment.split('.')
      print(coment)
      translator = Translator()
      translated = translator.translate(coment, dest='ja')
      print(translated.text)
      await message.channel.send(say)

@client.event
async def start(ctx):
    global board
    board = chess.Board()
    await ctx.send("ボードを作成しました")
    await ctx.send("```" + str(board) + "```")

@client.event
async def move(ctx,movePos):
    global board
    if board == None:
        await ctx.send("ボードが作成されていません")
        return
    try:
        board.push_san(movePos)
        await ctx.send("```" + str(board) + "```")
    except:
        await ctx.send(movePos + "は有効な値ではありません")
        a = ""
        for i in board.legal_moves:
            a += str(i) + ","
        await ctx.send("> " + a)
    if board.is_game_over():
        await ctx.send("game over")
        board = None

#コマンドのやつ
@tree.command(name="test", description="テストコマンド")
async def test(interaction: discord.Interaction):
  msg = "テスト"
  await interaction.response.send_message(msg)

#webserver.run()

my_secret = os.environ['DISCORD_TOKEN']
client.run(my_secret)
#トークンがトークン
#知っていましたか？明日って今日の一日後なんですよ