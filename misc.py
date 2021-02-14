import os
import json
from datetime import datetime

def save_data(message):
    channel_id = message.channel.id
    filename = saves_dir + 'c' + str(channel_id) + '.json'

    if not os.path.exists(saves_dir):
        os.mkdir(saves_dir)
    if not os.path.exists(filename):
        open(filename, 'w').close()
  
    msg_content =  message.content.replace('$bookmark','')
    msg_content = msg_content.strip()

    json_file = open(filename,'r+')
    file = {}
    try:
        file = json.load(json_file)
    except json.decoder.JSONDecodeError:
        pass
    data = {}
    if 'data' in file:
        data = file['data']

    json_file.close()

    json_file = open(filename,'w+')
  
    msg_data = {}
    msg_data['created_at'] = message.created_at.strftime("%d/%m/%y %H:%M")
    msg_data['author'] = message.author.name
    msg_data['content'] = msg_content
  
    msg_id = 'm'+str(message.id)
    data[msg_id]= msg_data
    file['data'] = data
    json_file.write(json.dumps(file))
    json_file.close()
    return True

def list_data(channel_id):
    filename = saves_dir +'c'+str(channel_id)+'.json'
    if not os.path.exists(saves_dir):
        os.mkdir(saves_dir)
    if not os.path.exists(filename):
        open(filename, 'w').close()

    json_file = open(filename)
    file = {}
    try:
        file = json.load(json_file)
    except json.decoder.JSONDecodeError:
        pass

    data = {}
    if 'data' in file:
        data = file['data']

    output = ':printer: Αποθηκευμένα μηνύματα στο κανάλι: ' + message.channel.name
    output += '\n \n'
    for msg in data:
        msg_data =data[msg]
        output += '\t'
        output += ':page_facing_up: ['+msg_data['created_at']+'] '+msg_data['author']+': '+msg_data['content']
        output += '\n'
    
    json_file.close()
    return output

def clear_data(channel_id):
    filename = saves_dir +'c'+str(channel_id)+'.json'
    os.remove(filename)