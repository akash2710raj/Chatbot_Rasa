from typing import Any, Text, Dict, List, Union
import pytz
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import json
from rasa_sdk.events import UserUttered, SlotSet
import time
from rasa_sdk.forms import FormAction
from rasa_sdk.events import AllSlotsReset
import datetime

import sqlite3

def storedatabase(name, email, phonenumber, service):
    print("in the database")
        
    date = str(datetime.datetime.now(pytz.timezone('Asia/Kolkata')).strftime('%d-%m-%Y %H:%M:%S'))
    print(service)
    ## SQL Operations
    conn = sqlite3.connect('data.db')

    cursor = conn.cursor()
    cursor.execute(f'''INSERT INTO User (NAME,EMAIL,PHONENUMBER,DATE,SERVICES) VALUES (?,?,?,?,?)''',(name,email,phonenumber,date,service))
    conn.commit()
    print("after commit in database")

class ActionWelcome(Action):

    def name(self):
        return "action_welcome"

    def run(self, dispatcher, tracker, domain):
        print('init')
        dispatcher.utter_message(template="utter_welcome")
        return


class ActionFallback(Action):

    def name(self):
        return "action_fallback"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Sorry, I Couldn't Understand. Can You Rephrase It?")

class ActionTellname(Action):

    def name(self):
        return "action_tellname"

    def run(self, dispatcher, tracker, domain):
        name = tracker.latest_message['entities']
        print(name)


        try:
            name = tracker.latest_message['entities'][0].get('value')
            print(name)
        except:
            name = None
        if name is not None:
            dispatcher.utter_message(text = f'Hi, Your Email Please?')
            return [SlotSet("name",name)]
        else:
            dispatcher.utter_message(text = f'No Worries, Your Email Please??')
            
        return

class ActionTellemail(Action):
    
    def name(self):
        return "action_tellemail"

    def run(self, dispatcher, tracker, domain):
        email = tracker.latest_message['entities']
        print(email)
        
        try:
            email = tracker.latest_message['entities'][0].get('value')
            print(email)
        except:
            email = None
        if email is not None:
            
            dispatcher.utter_message(text = "Please Provide Your Contact Number With Country Code.")
            return [SlotSet("email",email)]
        else:
            dispatcher.utter_message(text = 'No Worries, Please Provide Your Phone Number With Country Code.')
            
        return


class ActionTellphonenumber(Action):
    
    def name(self):
        return "action_tellphonenumber"

    def run(self, dispatcher, tracker, domain):
        phonenumber = tracker.latest_message['entities']
        print(phonenumber)
        name = tracker.get_slot("name")
        button_msg = [
                  {
                      "title": "Coding",
                      "payload": "/coding"
                  },
                  {
                      "title": "Writing",
                      "payload": "/writing"
                  },
                {
                    "title": "Topic Based Learning",
                    "payload": "/tbl"
                },
                {
                    "title":"Project Based Learning",
                    "payload": "/pbl"
                }
              ]
        try:
            phonenumber = tracker.latest_message['entities'][0].get('value')
            print(phonenumber)
        except:
            phonenumber = None
        if phonenumber is not None:
            dispatcher.utter_message(text = f'Hi {name} , How May I Help You Today?',buttons=button_msg)
            return [SlotSet("phonenumber",phonenumber)]
        else:
            dispatcher.utter_message(text = f'No Worries, How May I Help You Today?',buttons = button_msg)
            
        return

        
class ActionCoding(Action):

    def name(self):
        return "action_coding"

    def run(self, dispatcher, tracker, domain):
        
        dispatcher.utter_message(template='utter_coding')
        name = tracker.get_slot("name")
        email = tracker.get_slot("email")
        phonenumber = tracker.get_slot("phonenumber")
        storedatabase(name, email, phonenumber,"coding")
        return [SlotSet("service","coding")]


class ActionWriting(Action):

    def name(self):
        return "action_writing"

    def run(self, dispatcher, tracker, domain):
        
        # dispatcher.utter_message(template='utter_writing')
        with open('batch.json') as fp:
            data = json.load(fp)
            w_link = data.get('service').get('writing').get('link')
            
            dispatcher.utter_message(text=f'Awesome,Please Visit Link For More Information On Writing Service.<br><br>You Can see here: <a href="{w_link}" target="_blank">here</a>')
            btn_msg = [
                      {
                          "title": "Yes",
                          "payload": "/affirm"
                      },
                      {
                          "title": "No",
                          "payload": "/deny"
                      }

                  ]
            dispatcher.utter_message(text = 'Did That Help?', buttons = btn_msg)
        name = tracker.get_slot("name")
        email = tracker.get_slot("email")
        phonenumber = tracker.get_slot("phonenumber")
        storedatabase(name, email, phonenumber,"writng")
        return [SlotSet("service","writing")]



class ActionPbl(Action):

    def name(self):
        return "action_pbl"

    def run(self, dispatcher, tracker, domain):
        
        dispatcher.utter_message(template='utter_pbl')
        name = tracker.get_slot("name")
        email = tracker.get_slot("email")
        phonenumber = tracker.get_slot("phonenumber")
        storedatabase(name, email, phonenumber,"pbl")
        return [SlotSet("service","pbl")]


class ActionTbl(Action):

    def name(self):
        return "action_tbl"

    def run(self, dispatcher, tracker, domain):
        
        dispatcher.utter_message(template='utter_tbl')
        name = tracker.get_slot("name")
        email = tracker.get_slot("email")
        phonenumber = tracker.get_slot("phonenumber")
        storedatabase(name, email, phonenumber,"tbl")
        
        return [SlotSet("service","tbl")]

    
class ActionLevel(Action):

    def name(self):
        return "action_level"

    def run(self, dispatcher, tracker, domain):
        # msg = tracker.latest_message.get('text')
        # intent = tracker.latest_message['intent'].get('name')
        # ent = tracker.latest_message['entities'][0].get('value')
        # print(ent)


        button_msg = [
                  {
                      "title": "Basic",
                      "payload": "/basic"
                  },
                  {
                      "title": "Advance",
                      "payload": "/advance"
                  },
                {
                    "title": "Expert",
                    "payload": "/expert"
                },
              ]
            
        dispatcher.utter_message(text = f'Please Select The Level',buttons=button_msg)
        try:
            language = tracker.latest_message['entities'][0].get('value')
            print(language)
        except:
            language = None
        if language is not None:
            return [SlotSet("language",language)]
        else:
            dispatcher.utter_message(text = f'No Worries, How May I Help You Today?',buttons = button_msg)


        return [SlotSet("language",language)]


class ActionBasicLogic(Action):

    def name(self):
        return "action_basiclogic"

    def run(self, dispatcher, tracker, domain):
        return [SlotSet("level","basic")]


class ActionBasicTopic(Action):

    def name(self):
        return "action_basictopic"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
           domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # msg = tracker.latest_message.get('text')
        # intent = tracker.latest_message['intent'].get('name')
        # ent = tracker.latest_message['entities'][0].get('value')
        language = tracker.get_slot('language')
        # print(ent)
        level = tracker.get_slot('level')
        # print(level)
        
        if level == 'basic':
            if language in ['python','java','css','html','c','js']:
                with open('batch.json') as fp:
                    data = json.load(fp)
                msg = ""
                for topic in data.get('service').get('basic').get(language):
                    msg += topic+"<br>"
                dispatcher.utter_message(text = "Please Enter the basic topic")
                dispatcher.utter_message(msg)
                # faculty_name1 = data.get('service').get('coding').get(ent).get('faculty_name1')
                # link = data.get('service').get('coding').get(ent).get('link')
        try:
            topic = tracker.latest_message['entities'][0].get('value')
            print(topic)
        except:
            topic = None
            if topic is not None:
                return [SlotSet("topic",topic)]



class ActionAdvanceLogic(Action):

    def name(self):
        return "action_advancelogic"

    def run(self, dispatcher, tracker, domain):
        return [SlotSet("level","advance")]


class ActionAdvanceTopic(Action):

    def name(self):
        return "action_advancetopic"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
           domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # msg = tracker.latest_message.get('text')
        # intent = tracker.latest_message['intent'].get('name')
        # ent = tracker.latest_message['entities'][0].get('value')
        language = tracker.get_slot('language')
        # print(ent)
        level = tracker.get_slot('level')
        print(level)
        
        if level == 'advance':
            if language in ['python','java','css','html','c','js']:
                with open('batch.json') as fp:
                    data = json.load(fp)
                msg = ""
                for topic in data.get('service').get('advance').get(language):
                    msg += topic+"<br>"
                dispatcher.utter_message(msg)
                # faculty_name1 = data.get('service').get('coding').get(ent).get('faculty_name1')
                # link = data.get('service').get('coding').get(ent).get('link')


class ActionExpertLogic(Action):

    def name(self):
        return "action_expertlogic"

    def run(self, dispatcher, tracker, domain):
        return [SlotSet("level","expert")]


class ActionExpertTopic(Action):

    def name(self):
        return "action_experttopic"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
           domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # msg = tracker.latest_message.get('text')
        # intent = tracker.latest_message['intent'].get('name')
        # ent = tracker.latest_message['entities'][0].get('value')
        language = tracker.get_slot('language')
        # print(ent)
        level = tracker.get_slot('level')
        print(level)
        
        if level == 'expert':
            if language in ['python','java','css','html','c','js']:
                with open('batch.json') as fp:
                    data = json.load(fp)
                msg = ""
                for topic in data.get('service').get('expert').get(language):
                    msg += topic+"<br>"
                dispatcher.utter_message(msg)
                # faculty_name1 = data.get('service').get('coding').get(ent).get('faculty_name1')
                # link = data.get('service').get('coding').get(ent).get('link')


class ActionTopic(Action):
    
    def name(self) -> Text:
        return "action_topic"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
           domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        language = tracker.get_slot('language')
        # level = tracker.get_slot('level')
        # topic = tracker.get_slot('topic')
        topic = tracker.latest_message['text']
        print(topic)
        lang, tpc = topic.split(' ')

        with open('batch.json') as fp:
            data = json.load(fp)
        next_batch1 = data.get('service').get("tbl").get(lang).get(tpc).get("next_batch1")
        faculty_name1 = data.get('service').get("tbl").get(lang).get(tpc).get('faculty_name1')
        topic1 = data.get('service').get("tbl").get(lang).get(tpc).get('topic1')
        link1 = data.get('service').get("tbl").get(lang).get(tpc).get('link1')

        dispatcher.utter_message(text=f'Next Batch of {topic1} <br> Faculty Name Is: {faculty_name1} <br> Next Batch Is On: {next_batch1} <br>For More Updates <a href="{link1}" >Click Here</a>')

        # next_batch2 = data.get('service').get("tbl").get(language).get('topic').get("next_batch2")
        # faculty_name2 = data.get('service').get("tbl").get(language).get('topic').get('faculty_name2')
        # topic2 = data.get('service').get("tbl").get(language).get('topic').get('topic2')
        # link2 = data.get('service').get("tbl").get(language).get('topic').get('link1')

        # dispatcher.utter_message(text=f'Next Batch of {topic2} <br>Faculty Name Is: {faculty_name2} <br> Next Batch Is On: {next_batch2} <br>For More Updates <a href="{link2}" >Click Here</a>')

        # next_batch3 = data.get('service').get("tbl").get(language).get('topic').get("next_batch3")
        # faculty_name3 = data.get('service').get("tbl").get(language).get('topic').get('faculty_name3')
        # topic3 = data.get('service').get("tbl").get(language).get('topic').get('topic3')
        # link3 = data.get('service').get("tbl").get(language).get('topic').get('link1')

        # dispatcher.utter_message(text=f'Next Batch of {topic3} <br>Faculty Name Is: {faculty_name3} <br> Next Batch Is On: {next_batch3} <br>For More Updates <a href="{link3}" >Click Here</a>')
        time.sleep(1)
        btn_msg = [
            {
                "title": "Yes",
                "payload": "/affirm"
                },
                {
                    "title": "No",
                    "payload": "/deny"
                    }

                  ]
        dispatcher.utter_message(text = 'Did That Help?', buttons = btn_msg)

        return[]




class ActionValidate(Action):
    
    def name(self) -> Text:
        return "action_validate"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
           domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        msg = tracker.latest_message.get('text')
        intent = tracker.latest_message['intent'].get('name')
        ent = tracker.latest_message['entities'][0].get('value')
        print(ent)
        service = tracker.get_slot('service')
        print(service)
        
        if service == 'coding':
            if ent in ['python','java','css','html','c','js']:
                with open('batch.json') as fp:
                    data = json.load(fp)
                next_batch1 = data.get('service').get('coding').get(ent).get('next_batch1')
                faculty_name1 = data.get('service').get('coding').get(ent).get('faculty_name1')
                link = data.get('service').get('coding').get(ent).get('link')

                dispatcher.utter_message(text=f'Faculty Name Is: {faculty_name1} <br> Next Batch Is On: {next_batch1} <br>For More Updates <a href="{link}" >Click Here</a>')

                next_batch2 = data.get('service').get('coding').get(ent).get('next_batch2')
                faculty_name2 = data.get('service').get('coding').get(ent).get('faculty_name2')
                link = data.get('service').get('coding').get(ent).get('link')

                dispatcher.utter_message(text=f'Faculty Name Is: {faculty_name2} <br> Next Batch Is On: {next_batch2} <br>For More Updates <a href="{link}" >Click Here</a>')

                next_batch3 = data.get('service').get('coding').get(ent).get('next_batch3')
                faculty_name3 = data.get('service').get('coding').get(ent).get('faculty_name3')
                link = data.get('service').get('coding').get(ent).get('link')

                dispatcher.utter_message(text=f'Faculty Name Is: {faculty_name3} <br> Next Batch Is On: {next_batch3} <br>For More Updates <a href="{link}" >Click Here</a>')
                time.sleep(1)
                btn_msg = [
                      {
                          "title": "Yes",
                          "payload": "/affirm"
                      },
                      {
                          "title": "No",
                          "payload": "/deny"
                      }

                  ]
                dispatcher.utter_message(text = 'Did That Help?', buttons = btn_msg)

            else:
                btn_msg = [
                      {
                          "title": "Yes",
                          "payload": "/affirm"
                      },
                      {
                          "title": "No",
                          "payload": "/deny"
                      }

                  ]
                dispatcher.utter_message(text=f"Sorry, We Currently This Service Is Not Available.",buttons=btn_msg)
                return[UserUttered(text="/coding")]

        elif service == 'pbl':
            if ent in ['python','java','css','html','c','js']:
                with open('batch.json') as fp:
                    data = json.load(fp)
                duration1 = data.get('service').get('pbl').get(ent).get('duration1')
                p_name1 = data.get('service').get('pbl').get(ent).get('p_name1')
                link = data.get('service').get('pbl').get(ent).get('link')

                dispatcher.utter_message(text=f'Project Is: {p_name1} <br> Duration Is Of: {duration1} <br>For More Updates <a href="{link}" >Click Here</a>')

                duration2 = data.get('service').get('pbl').get(ent).get('duration2')
                p_name2 = data.get('service').get('pbl').get(ent).get('p_name2')
                link = data.get('service').get('pbl').get(ent).get('link')

                dispatcher.utter_message(text=f'Project Is: {p_name2} <br> Duration Is Of: {duration2} <br>For More Updates <a href="{link}" >Click Here</a>')

                duration3 = data.get('service').get('pbl').get(ent).get('duration3')
                p_name3 = data.get('service').get('pbl').get(ent).get('p_name3')
                link = data.get('service').get('pbl').get(ent).get('link')

                dispatcher.utter_message(text=f'Project Is: {p_name3} <br> Duration Is Of: {duration3} <br>For More Updates <a href="{link}" >Click Here</a>')
                time.sleep(1)
                btn_msg = [
                      {
                          "title": "Yes",
                          "payload": "/affirm"
                      },
                      {
                          "title": "No",
                          "payload": "/deny"
                      }

                  ]
                dispatcher.utter_message(text = 'Did That Help?', buttons = btn_msg)

            else:
                btn_msg = [
                      {
                          "title": "Yes",
                          "payload": "/affirm"
                      },
                      {
                          "title": "No",
                          "payload": "/deny"
                      }

                  ]
                dispatcher.utter_message(text=f"Sorry, We Currently This Service Is Not Available.",buttons=btn_msg)
                return[UserUttered(text="/pbl")]


        else:


             dispatcher.utter_message(text='Sorry. We Provide Services In: ')
            
        return []

    
    
    
class FurtherHelpForm(FormAction):
    
    def name(self):
        """Name of the Form"""
        return "feedback_form"


    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        
        if tracker.get_slot('name') is not None:
            return ["email"]
        elif tracker.get_slot('email') is not None:
            return ["phonenumber"]
        else:
            tracker.get_slot('phonenumber') is not None
            return None

    
    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:

        return {
            "name": self.from_entity(entity="name"),
            "email": self.from_entity(entity="email"),
            "phonenumber": self.from_entity(entity="phonenumber")  
        }


    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""
        
        dispatcher.utter_message('Thank you for providing the info.')
        print(tracker.get_slot("name"))
        print(tracker.get_slot("email")[0])
        print(tracker.get_slot("phonenumber"))
        name = tracker.get_slot("name")
        email = tracker.get_slot("email")[0]
        phonenumber = tracker.get_slot("phonenumber")
        
        date = str(datetime.datetime.now(pytz.timezone('Asia/Kolkata')).strftime('%d-%m-%Y %H:%M:%S'))
        service = tracker.get_slot("service")
        print(service)
        ## SQL Operations
        conn = sqlite3.connect('data.db')

        cursor = conn.cursor()
        cursor.execute(f'''INSERT INTO User (NAME,EMAIL,PHONENUMBEF,DATE,SERVICES) VALUES (?,?,?,?,?)''',(name,email,phonenumber,date,service))
        conn.commit()
        return [AllSlotsReset()]
