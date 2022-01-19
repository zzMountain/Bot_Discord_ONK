import discord

client = discord.Client()
content = ""


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    ""
    if message.content.startswith('$'):
        new_nick = ""
        fio = 0
        group = ""
        content = message.content[1:]
        for i in content:
            if fio == 3:
                group += i
            new_nick += str(i)
            if i == " ":
                new_nick += " "
                fio += 1
        if new_nick == "" or group == "":
            await message.channel.send('Пиши правильно! Пример:\n$Иван Иванович Иванов 4КС1-18')
        else:
            role_name = group  # specify role name here
            role = discord.utils.get(message.guild.roles, name=role_name)
            if role is not None:
                await message.author.add_roles(role)
            await message.author.edit(nick=str(new_nick))

client.run('Токен')
