import os
import calendar, time 
import datetime
from slack_bolt import App, Ack
from slack import WebClient
from taskview import *
import json
import random
import string
from apscheduler.schedulers.background import BackgroundScheduler


app = App(
    signing_secret = os.environ.get("SLACK_SIGN"),

# Initialize a Web API client
    token=os.environ.get("SLACK_BOT_TOKEN")
)

queue=[]
data=[]

sched = BackgroundScheduler(daemon=True)

@app.shortcut("todo")
def todo(view, shortcut, body, client, ack):
    p1 = viewx("ice")
    ack()
    try:
        client.views_open(
            trigger_id=shortcut["trigger_id"],
            view=p1.viewthing())
    except:
        print("wait")

def write_json(new_data,user, filename='tasks.json'):
    with open(filename,'r+') as file:
          # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        if user not in file_data:
            file_data.update(new_data)
        else:
            file_data[user].append(new_data[user][0])
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)

def printname(list):
    puff = []
    for i in list:
        puff.append(f"<@{i}>")
    man = "-> "+str(puff)[1:-1]
    man = man.replace("'","")
    return(man)

def scheduler(date1, time1):
    if date1 is not None:
        if time1 is None:
            time1 = "09:30:00"
            full = date1 + " "+ time1
            return full
        else:
            full = date1 + " "+ time1+":00"
            return full
    else:
        if time1 is not None:
            date1 = datetime.today().strftime('%Y-%m-%d')
            full = date1 + " "+ time1+":00"
            return full

def todo1(user,id,note, nolie, due,recurr="no"):
    return [
    {
        "assign": user,
        "duedate": due,
        "due": "yes",
        "recurr": recurr
    },    
    {
        "type": "section",
        "block_id": f"{id}",
        "text": {
            "type": "mrkdwn",
            "text": f":red_circle:  {note}"
        },
        "accessory": viewx.ACCESSORY
    },
    {
        "type": "context",
        "elements": [
            {
                "type": "mrkdwn",
                "text": f"<@{user}> {nolie} \nHạn hoàn thành/Due on: {due}\nID: {id}_{user}"
            }
        ]
    },
    {
        "type": "divider"
    }]

def job(user,line):
    app.client.chat_postMessage(channel=user,text=line)

def everydayjob(value,hour,minute,user, line):
    if value == "every":
        sched.add_job(job, 'cron', day_of_week = "*", hour=hour,minute=minute,args=[user,line])
    else:
        sched.add_job(job, 'cron', day_of_week = value, hour=hour,minute=minute,args=[user,line])

@app.command("/removesched")
def getts(body, say, client, ack, command):
    ack()
    if len(command) == 12:
        client.chat_postMessage(channel=command['user_id'],text=f"Bạn phải thêm Job_ID/You have to add Job_ID:\n/removesched *Job_ID*")
    else:
        try:
            sched.remove_job(command["text"])
        except:
            print("error")
            client.chat_postMessage(channel=command['user_id'],text=f"Hãy thử lại sau/Try again later")

@app.view("todo_view_edit")
def waha(view, shortcut, body, client, ack, say):
    user=body['user']['id']
    see = viewx.BLOCK_HOME.copy()
    linewhat = view["state"]["values"]["block_a"]["todo_input"]["value"]
    yeti = f"*Bạn có việc cần phải hoàn thành/You have ongoing tasks:*\n:point_right: {linewhat}"
    ack()
    try:
        with open("tasks.json",'r+') as file:
            blockid = queue[0]
            file_data = json.load(file)
            for i in range(0,len(file_data[user])):
                tasks = file_data[user][i][1]['block_id']
                sussy = blockid+"_"+user
                try:
                    sched.modify_job(sussy,args=[user,yeti])
                except:
                    print("sus")
                if tasks == blockid:
                    file_data[user][i][1]['text']['text'] = f":red_circle:  {linewhat}"
                    lien = open("tasks.json",'w')
                    json.dump(file_data,lien,indent=4)
            file_data[user].reverse()
            for i in range(len(file_data[user])):
                see.extend(file_data[user][i][1:])
            queue.pop()
        client.views_publish(
            # Use the user ID associated with the event
            user_id=user,
            # Home tabs must be enabled in your app configuration
            view={
                "type": "home",
                "blocks": see
            }
        )
    except:
        print("wait")

@app.view("todo_view")
def todoview(view, shortcut, body, client, ack, say):
    line1 = view["state"]["values"]["block_a"]["todo_input"]["value"]
    line2 = view["state"]["values"]["block_b"]["user_input"]["selected_users"]
    user=body['user']['id']
    id = ''.join(random.choice(string.ascii_letters) for i in range(10))
    #ice = calendar.timegm(time.strptime(line2, 'date %d-%m-%Y at %H:%M'))
    see = viewx.BLOCK_HOME.copy()
    nolie = printname(line2)
    if len(line2) == 0:
        nolie = "có việc cần phải làm/Has tasks to complete"
    todo = [
    {
        "assign": user,
        "duedate": "None",
        "due": "no",
        "recurr": "no"
    },    
    {
        "type": "section",
        "block_id": f"{id}",
        "text": {
            "type": "mrkdwn",
            "text": f":red_circle:  {line1}"
        },
        "accessory": viewx.ACCESSORY
    },
    {
        "type": "context",
        "elements": [
            {
                "type": "mrkdwn",
                "text": f"<@{user}> {nolie}\nID: {id}_{user}"
            }
        ]
    },
    {
        "type": "divider"
    }]
    ack()
    #client.chat_postMessage(channel=body['user']['id'], text=f"{ice}")
    try:
        if line1 is None:
            client.chat_postMessage(channel=body['user']['id'], text=f"give yourself a task")
        #this is for extended view
        if len(body['view']['blocks']) > 3:
            if view["title"]["text"] == "TODO EVERYDAY":
                line5 = view["state"]["values"]["block_g"]["pickday"]["selected_option"]
                line4 = view["state"]["values"]["block_e"]["timepicker"]["selected_time"]
                yeet = f"*Bạn có việc cần phải hoàn thành/You have ongoing tasks:*\n:point_right: {line1}"
                lowkey = f"{line5['text']['text']} at {line4}"
                timeski = datetime.strptime(line4, '%H:%M')
                hour = timeski.hour
                minute = timeski.minute
                if line5 is not None:
                    if len(line2) > 0:
                        for i in line2:
                            client.chat_postMessage(channel=i,text=f"Bạn có công việc cần hoàn thành từ/You have a new task from <@{user}>:\n:point_right: {line1}\nID: {id}_{user}")
                            sussy = id+"_"+i
                            everydayjob(line5["value"],hour,minute,i, yeet)
                            dictionary = {
                                i: [
                                    todo1(user,id,line1,nolie,lowkey)
                                ]
                            }

                            write_json(dictionary,i)
                            with open("tasks.json",'r+') as file:
                                file_data = json.load(file)
                                file_data[i].reverse()
                                for j in range(len(file_data[i])):
                                    see.extend(file_data[i][j][1:])
                            client.views_publish(
                                user_id=i,
                                # Home tabs must be enabled in your app configuration
                                view={
                                    "type": "home",
                                    "blocks": see
                                }
                            )
                    else:
                        sussy = id+"_"+user
                        everydayjob(line5["value"],hour,minute,user, yeet)
                    dictionary = {
                        user: [
                            todo1(user,id,line1,nolie,lowkey)
                        ]
                    }

                    write_json(dictionary,user)
                    with open("tasks.json",'r+') as file:
                        file_data = json.load(file)
                        file_data[user].reverse()
                        for j in range(len(file_data[user])):
                            see.extend(file_data[user][j][1:])
                    client.views_publish(
                        user_id=user,
                        # Home tabs must be enabled in your app configuration
                        view={
                            "type": "home",
                            "blocks": see
                        }
                    )

                else:
                    client.chat_postMessage(channel=body['user']['id'], text=f"{view}")
            else:
                line3 = view["state"]["values"]["block_d"]["pick_date"]["selected_date"]
                line4 = view["state"]["values"]["block_e"]["timepicker"]["selected_time"]
                
                duedate = scheduler(line3,line4)
                yeet = f"*Bạn có việc cần phải hoàn thành/You have ongoing tasks:*\n:point_right: {line1}\nID: {id}_{user}"

                if len(line2) > 0:
                    for i in line2:
                        client.chat_postMessage(channel=i,text=f"Bạn có công việc cần hoàn thành từ/You have a new task from <@{user}>:\n:point_right: {line1}\nID: {id}_{user}")
                        sussy = id+"_"+i
                        sched.add_job(job, 'date' ,args=[i,yeet],run_date=duedate,id=sussy)
                        dictionary = {
                            i: [
                                todo1(user,id,line1,nolie,duedate)
                            ]
                        }

                        write_json(dictionary,i)
                        with open("tasks.json",'r+') as file:
                            file_data = json.load(file)
                            file_data[i].reverse()
                            for j in range(len(file_data[i])):
                                see.extend(file_data[i][j][1:])
                        client.views_publish(
                            user_id=i,
                            # Home tabs must be enabled in your app configuration
                            view={
                                "type": "home",
                                "blocks": see
                            }
                        )
                else:
                    sussy = id+"_"+user
                    sched.add_job(job, 'date' ,args=[user,yeet],run_date=duedate,id=sussy)

                dictionary = {
                    user: [
                        todo1(user,id,line1,nolie,duedate)
                    ]
                }
                write_json(dictionary,user)
                with open("tasks.json",'r+') as file:
                    file_data = json.load(file)
                    file_data[user].reverse()
                    for i in range(len(file_data[user])):
                        see.extend(file_data[user][i][1:])
                client.views_publish(
                    user_id=user,
                    # Home tabs must be enabled in your app configuration
                    view={
                        "type": "home",
                        "blocks": see
                    }
                )
            #client.chat_postMessage(channel=body['user']['id'], text=f"{list_scheduled_messages(client,'1626256800','1626256800')['id']}")
        else:
            if len(line2) > 0:
                for i in line2:
                    client.chat_postMessage(channel=i,text=f"Bạn có công việc cần hoàn thành từ/You have a new task from <@{user}>:\n:point_right: {line1}\nID: {id}_{user}")
                    dictionary = {
                        i: [
                            todo
                        ]
                    }
                    write_json(dictionary,i)
                    with open("tasks.json",'r+') as file:
                        file_data = json.load(file)
                        file_data[i].reverse()
                        for j in range(len(file_data[i])):
                            see.extend(file_data[i][j][1:])
                    client.views_publish(
                        user_id=i,
                        # Home tabs must be enabled in your app configuration
                        view={
                            "type": "home",
                            "blocks": see
                        }
                    )
            else:
                dictionary = {
                    user: [
                        todo
                    ]
                }
                write_json(dictionary,user)
                with open("tasks.json",'r+') as file:
                    file_data = json.load(file)
                    file_data[user].reverse()
                    for i in range(len(file_data[user])):
                        see.extend(file_data[user][i][1:])
                client.views_publish(
                    user_id=user,
                    # Home tabs must be enabled in your app configuration
                    view={
                        "type": "home",
                        "blocks": see
                    }
                )
    except:
        print("wait")

@app.action("overflow")
def function(view, shortcut, body, client, ack, say,action):
    blockid = action['block_id']
    value = action['selected_option']['value']
    see = viewx.BLOCK_HOME.copy()
    user = body['user']['id']
    ack()
    try:
        with open("tasks.json",'r+') as file:
            file_data = json.load(file)
            leng=len(file_data[user])
            for i in range(leng):
                tasks = file_data[user][i][1]['block_id']
                if tasks == blockid:
                    if value == "value-0":
                        string = file_data[user][i][1]['text']['text']
                        finished1 = f":white_check_mark:{string[12:]}"
                        file_data[user][i][1]['text']['text'] = finished1
                        file_data[user][i][1]['accessory'] = viewx.ACCESSORY_NEW
                        client.chat_postMessage(channel=file_data[user][i][0]["assign"], text=f"<@{user}> đã hoàn thành công việc/has completed the task:\n{string} \nvào lúc/on: {datetime.fromtimestamp(int(float(body['actions'][0]['action_ts'])))}\nID: {blockid}_{user}")
                        dictionary = {
                                user: [
                                    file_data[user][i]
                                ]
                            }
                        write_json(dictionary,user,filename="donetasks.json")
                        welwel=blockid+"_"+user
                        try:
                            sched.remove_job(welwel)
                        except:
                            print("it's already began")
                        liny = open("tasks.json",'w')
                        file_data[user].pop(i)
                        json.dump(file_data,liny,indent=4)
                        with open("donetasks.json",'r+') as nobody:
                            south = json.load(nobody)
                            while len(south[user]) > 3:
                                lina = open("donetasks.json",'w')
                                south[user].pop(0)
                                json.dump(south,lina,indent=4)
                                break
                        break
                    if value == "value-1":
                        line1 = file_data[user][i][1]['text']['text']
                        p1 = viewx(line1[14:])
                        client.views_open(        
                            trigger_id=body["trigger_id"],
                            view=p1.viewthingedit())
                        queue.append(tasks)
                    if value == "value-2":
                        string = file_data[user][i][1]['text']['text']
                        client.chat_postMessage(channel=user, text=f"Bạn đã xoá công việc/You have deleted a task:\n{string} \nvào lúc/on: {datetime.fromtimestamp(int(float(body['actions'][0]['action_ts'])))}\nID: {blockid}_{user}")
                        welwel=blockid+"_"+user
                        try:
                            sched.remove_job(welwel)
                        except:
                            print("it's already began")
                        file_data[user].pop(i)
                        liny = open("tasks.json",'w')
                        json.dump(file_data,liny,indent=4)
                        break
            file_data[user].reverse()
            for i in range(len(file_data[user])):
                see.extend(file_data[user][i][1:])
        client.views_publish(
            # Use the user ID associated with the event
            user_id=user,
            # Home tabs must be enabled in your app configuration
            view={
                "type": "home",
                "blocks": see
            }
        )
    except:
        print("wait")

@app.action("overflow_new")
def function(view, shortcut, body, client, ack, say,action):
    blockid = action['block_id']
    value = action['selected_option']['value']
    see = viewx.BLOCK_HOME_DONE.copy()
    user = body['user']['id']
    ack()
    try:
        with open("donetasks.json",'r+') as file:
            file_data = json.load(file)
            leng=len(file_data[user])
            for i in range(leng):
                tasks = file_data[user][i][1]['block_id']
                if tasks == blockid:
                    if value == "value-4":
                        file_data[user].pop(i)
                        liny = open("donetasks.json",'w')
                        json.dump(file_data,liny,indent=4)
                        break
                    if value == "value-3":
                        string = file_data[user][i][1]['text']['text']
                        finished1 = f":red_circle:{string[18:]}"
                        file_data[user][i][1]['text']['text'] = finished1
                        file_data[user][i][1]['accessory'] = viewx.ACCESSORY
                        dictionary = {
                                user: [
                                    file_data[user][i]
                                ]
                            }
                        write_json(dictionary,user)
                        lien = open("donetasks.json",'w')
                        file_data[user].pop(i)
                        json.dump(file_data,lien,indent=4)
                        break
            file_data[user].reverse()
            for i in range(len(file_data[user])):
                see.extend(file_data[user][i][1:])
        client.views_publish(
            # Use the user ID associated with the event
            user_id=user,
            # Home tabs must be enabled in your app configuration
            view={
                "type": "home",
                "blocks": see
            }
        )
    except:
        print("wait")
                    
@app.action("task_choose")        
def menu(view, shortcut, body, client, ack, say,action):
    option=action['selected_option']['value']
    see1 = viewx.BLOCK_HOME_DONE.copy()
    see2 = viewx.BLOCK_HOME.copy()
    user=body['user']['id']
    ack()
    try:
        if option == "value-0":
            with open("tasks.json",'r+') as file:
                file_data = json.load(file)
                if user not in file_data:
                    see2 = see2
                else:
                    file_data[user].reverse()
                    for i in range(len(file_data[user])):
                        see2.extend(file_data[user][i][1:])
                client.views_publish(
                    # Use the user ID associated with the event
                    user_id=user,
                    # Home tabs must be enabled in your app configuration
                    view={
                        "type": "home",
                        "blocks": see2
                    }
                )
        if option == "value-1":
            with open("donetasks.json",'r+') as file:
                file_data = json.load(file)
                if user not in file_data:
                    see1 = see1
                else:
                    file_data[user].reverse()
                    for i in range(len(file_data[user])):
                        see1.extend(file_data[user][i][1:])
                client.views_publish(
                    # Use the user ID associated with the event
                    user_id=user,
                    # Home tabs must be enabled in your app configuration
                    view={
                        "type": "home",
                        "blocks": see1
                    }
                )
    except:
        print("wait")

@app.action("more")
def morebutton(view, shortcut, body, client, ack, say):
    p1 = viewx("ice")
    ack()
    try:
        client.views_update(
            # Pass the view_id
            view_id=body["view"]["id"],
            # String that represents view state to protect against race conditions
            hash=body["view"]["hash"],
            # View payload with updated blocks
            view=p1.extendviewthing())
    except:
        print("wait")

@app.action("ticked")
def tickedbox(view, shortcut, body, client, ack, say, action):
    p1 = viewx("ice")
    ack()
    try:
        client.views_update(
            # Pass the view_id
            view_id=body["view"]["id"],
            # String that represents view state to protect against race conditions
            hash=body["view"]["hash"],
            # View payload with updated blocks
            view=p1.extendviewthing_every())
    except:
        print("wait")

@app.action("ticked_back")
def tickback(view, shortcut, body, client, ack, say, action):
    p1 = viewx("ice")
    ack()
    try:
        client.views_update(
            # Pass the view_id
            view_id=body["view"]["id"],
            # String that represents view state to protect against race conditions
            hash=body["view"]["hash"],
            # View payload with updated blocks
            view=p1.extendviewthing())
    except:
        print("wait")

@app.event("app_home_opened")
def home(client, event, logger, ack, view):
    see = viewx.BLOCK_HOME.copy()
    user = event["user"]
    ack()
    try:
        with open("tasks.json",'r+') as file:
            file_data = json.load(file)
            if user not in file_data:
                see = see
            else:
                file_data[user].reverse()
                for i in range(len(file_data[user])):
                    see.extend(file_data[user][i][1:])
            client.views_publish(
                # Use the user ID associated with the event
                user_id=user,
                # Home tabs must be enabled in your app configuration
                view={
                    "type": "home",
                    "blocks": see
                }
            )
    except:
        print("wait")

@app.action("add")
def add(view, shortcut, body, client, ack, say, event, action):
    p1 = viewx("ice")
    ack()
    try:
        client.views_open(
            trigger_id=body["trigger_id"],
            view=p1.viewthing())
    except:
        print("wait")

if __name__ == "__main__":
    sched.start()
    app.start(port=int(os.environ.get("PORT", 5000)))
