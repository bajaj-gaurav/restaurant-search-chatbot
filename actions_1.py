from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet, FollowupAction
import json
import smtplib
import os
from email.message import EmailMessage
import re

output_10 = []


class ActionSearchRestaurants(Action):
    def name(self):
        return 'action_search_restaurants'


    def find_top_rated_restaurants(self, lat, lon, cuisine, budget, xxx, find_restaurant_number):
        global output_10
        output_10 = []
        output_5 = []
        count = 0
        start = 0
        limit = 20
        while count < find_restaurant_number and start < 100:
            results = xxx.restaurant_search_desc_rating("", lat, lon, cuisine, start, limit)
            results = json.loads(results)
            if budget == "Lesser than Rs. 300":
                for restaurant in results['restaurants']:
                    if restaurant['restaurant']['average_cost_for_two'] < 300:
                        res = restaurant['restaurant']['name'] + " in " + restaurant['restaurant']['location'][
                            'address'] + " has been rated " + restaurant['restaurant']['user_rating']['aggregate_rating']
                        if count <= 5:
                            output_5.append(res)
                        res_10 = res + " with the average budget for two people equal to Rs " + str(
                            restaurant['restaurant']['average_cost_for_two'])
                        output_10.append(res_10)
                        count += 1
                    if count == find_restaurant_number:
                        break;
            elif budget == "Rs. 300 to 700":
                for restaurant in results['restaurants']:
    
                    if restaurant['restaurant']['average_cost_for_two'] >= 300 and restaurant['restaurant'][
                        'average_cost_for_two'] <= 700:
                        #print(restaurant['restaurant']['average_cost_for_two'])
                        res = restaurant['restaurant']['name'] + " in " + restaurant['restaurant']['location'][
                            'address'] + " has been rated " + restaurant['restaurant']['user_rating']['aggregate_rating']
                        if count <= 5:
                            output_5.append(res)
                        res_10 = res + " with the average budget for two people equal to Rs " + str(
                            restaurant['restaurant']['average_cost_for_two'])
                        output_10.append(res_10)
                        count += 1
                    if count == find_restaurant_number:
                        break;
            elif budget == "More than 700":
                for restaurant in results['restaurants']:
                    if restaurant['restaurant']['average_cost_for_two'] > 700:
                        #print(restaurant['restaurant']['average_cost_for_two'])
                        res = restaurant['restaurant']['name'] + " in " + restaurant['restaurant']['location'][
                            'address'] + " has been rated " + restaurant['restaurant']['user_rating']['aggregate_rating']
                        if count <= 5:
                            output_5.append(res)
                        res_10 = res + " with the average budget for two people equal to Rs " + str(
                            restaurant['restaurant']['average_cost_for_two'])
                        output_10.append(res_10)
                        count += 1
                    if count == find_restaurant_number:
                        break;
            else:
                return ("input not valid")
    
            # we can get only 20 results at a time
            start += 20
        return output_5

    def run(self, dispatcher, tracker, domain):
        global output_10
        # config = {}
        loc = tracker.get_slot('location')
        cuisine = tracker.get_slot('cuisine')
        budget = tracker.get_slot('budget')
        if not loc or not cuisine or not budget:
            dispatcher.utter_message("Some unknown problem. Please try again")
            return [FollowupAction("utter_ask_location")]
        cuisine = tracker.get_slot('cuisine').lower()
        budget = tracker.get_slot('budget').strip()
        location_detail = xxx.get_location(loc, 1)
        d1 = json.loads(location_detail)
        lat = d1["location_suggestions"][0]["latitude"]
        lon = d1["location_suggestions"][0]["longitude"]
        cuisines_dict = {'chinese': 25, 'mexican': 73, 'italian': 55, 'american': 1, 'north indian': 50,
                         'south indian': 85}

        response_orig = ""
        response_orig = self.find_top_rated_restaurants(lat, lon, str(cuisines_dict.get(cuisine)), budget, xxx,
                                                        find_restaurant_number=10)
        response_10 = ""
        if not response_orig or len(response_orig) == 0:
            response = "no results found"
        else:
            response = "\n".join(response_orig)
            response_10 = "\n".join(output_10)

        dispatcher.utter_message("-----" + response)
        #return [SlotSet('email_content', response_10)]
        return []


class ActionValidateCityTier(Action):
    def name(self):
        self.supported_city = []
        f = open("city_tier.txt", "r")
        file_output = f.readlines()
        f.close()

        for i in range(2):
            tier = file_output[i].split(":")[1].strip()
            tier = tier.replace(" and ", ",")
            tier = [x.strip().lower() for x in tier.split(",")]
            self.supported_city.extend(tier)
        return 'action_validate_city_tier'

    def run(self, dispatcher, tracker, domain):
        loc = tracker.get_slot('location').lower()
        if loc in self.supported_city:
            return [SlotSet('location', loc)]
        else:
            utter_message = "We do not operate in that area yet"
            dispatcher.utter_message(utter_message)
            return [FollowupAction("utter_another_location")]


class ActionValidateEmailId(Action):
    def name(self):
        return 'action_validate_email_id'

    def run(self, dispatcher, tracker, domain):
        regex = '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+([a-zA-Z0-9-.])*(\.[a-z]{2,4})$'
        email = tracker.get_slot('email')
        if (re.search(regex, email)):
            return [SlotSet('email', email)]
        else:
            utter_message = "Invalid email id"
            dispatcher.utter_message(utter_message)
            return [FollowupAction("utter_enter_valid_email_id")]

class ActionValidateCuisine(Action):
    def name(self):
        return 'action_validate_cuisine'

    def run(self, dispatcher, tracker, domain):
        available_cuisines = ["chinese", "mexican", "italian", "american", "south indian", "north indian"]
        cuisine = tracker.get_slot('cuisine')
        if cuisine:
            cuisine = cuisine.lower()
        if (cuisine in available_cuisines):
            return [SlotSet('cuisine', cuisine)]
        else:
            utter_message = "Cuisine not available for search"
            dispatcher.utter_message(utter_message)
            return [FollowupAction("utter_ask_cuisine")]

class ActionSendMail(Action):
    def name(self):
        return 'action_send_mail'

    def run(self, dispatcher, tracker, domain):
        global output_10
        email_content = "\n".join(output_10)
        gmail_user = os.environ.get('EMAIL_USER')
        gmail_password = os.environ.get('EMAIL_PASSWORD')

        # Create a text/plain message
        msg = EmailMessage()
        msg.set_content(email_content)

        # me == the sender's email address
        # you == the recipient's email address
        msg['Subject'] = 'Upgrad chatbot'
        msg['From'] = "abc@gmail.com"
        msg['To'] = gmail_user

        try:
            # Send the message via our own SMTP server.
            s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            try:
                s.login(gmail_user, gmail_password)
                s.sendmail("chatbot@gmail.com", gmail_user, msg.as_string())
                dispatcher.utter_message("Successfully sent email")
                s.close()
            except Exception as e1:
                print(e1)
                dispatcher.utter_message("Error: unable to send email")
                s.close()
        except Exception as e:
            print(e)
            print("Error: SMTP connection not established")
        return []