## test_stories_1
* greet: hello
    - utter_greet
* restaurant_search: restaurant in [bangalore](location)
    - slot{"location": "bangalore"}
    - action_validate_city_tier
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search: [Mexican](cuisine)
    - slot{"cuisine": "Mexican"}
    - action_validate_cuisine
    - slot{"cuisine": "mexican"}
    - utter_ask_avg_budget_2
* restaurant_search: [More than 700](budget)
    - slot{"budget": "More than 700"}
    - action_search_restaurants
    - utter_whether_to_email
* affirm: yes
    - utter_ask_email_id
* send_mail: [abc@gmail.com](email)
    - slot{"email": "abc@gmail.com"}
    - action_validate_email_id
    - slot{"email": "abc@gmail.com"}
    - action_send_mail
    - utter_goodbye


## test_stories_2
* greet: Hola
    - utter_greet
* restaurant_search: I’m hungry. Looking out for some good restaurants
    - utter_ask_location
* restaurant_search: [bengaluru](location:bangalore)
    - slot{"location": "ahmedabad"}
    - action_validate_city_tier
    - slot{"location": "ahmedabad"}
    - utter_ask_cuisine
* restaurant_search: [chinese](cuisine)
    - slot{"cuisine": "chinese"}
    - action_validate_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_avg_budget_2
* restaurant_search: [Rs. 300 to 700](budget)
    - slot{"budget": "Rs. 300 to 700"}
    - action_search_restaurants
    - utter_whether_to_email
* affirm: yes
    - utter_ask_email_id
* send_mail: [fdsfd@gmail.com](email)
    - slot{"email": "fdsfd@gmail.com"}
    - action_validate_email_id
    - slot{"email": "fdsfd@gmail.com"}
    - action_send_mail
    - utter_goodbye

## test_stories_3
* greet: hi
    - utter_greet
* restaurant_search: Can you suggest some good restaurants in [kolkata](location)
    - slot{"location": "bangalore"}
    - action_validate_city_tier
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search: [Mexican](cuisine)
    - slot{"cuisine": "Mexican"}
    - action_validate_cuisine
    - slot{"cuisine": "mexican"}
    - utter_ask_avg_budget_2
* restaurant_search: [More than 700](budget)
    - slot{"budget": "More than 700"}
    - action_search_restaurants
    - utter_whether_to_email
* affirm: yes
    - utter_ask_email_id
* send_mail: [abc@gmail.com](email)
    - slot{"email": "abc@gmail.com"}
    - action_validate_email_id
    - slot{"email": "abc@gmail.com"}
    - action_send_mail
    - utter_goodbye

## test_stories_4
* greet: Hola
    - utter_greet
* restaurant_search:  some good restaurants
    - utter_ask_location
* restaurant_search: [ahmedabad](location)
    - slot{"location": "ahmedabad"}
    - action_validate_city_tier
    - slot{"location": "ahmedabad"}
    - utter_ask_cuisine
* restaurant_search: [chinese](cuisine)
    - slot{"cuisine": "chinese"}
    - action_validate_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_avg_budget_2
* restaurant_search: [More than 700](budget)
    - slot{"budget": "More than 700"}
    - action_search_restaurants
    - utter_whether_to_email
* affirm: yes
    - utter_ask_email_id
* send_mail: [fdsfd@gmail.com](email)
    - slot{"email": "fdsfd@gmail.com"}
    - action_validate_email_id
    - slot{"email": "fdsfd@gmail.com"}
    - action_send_mail
    - utter_goodbye

## test_stories_5
* greet: hey
    - utter_greet
* restaurant_search: Looking out for some good [chinese](cuisine) restaurants in [delhi](location)
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - action_validate_city_tier
    - slot{"location": "delhi"}
    - action_validate_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_avg_budget_2
* restaurant_search: [Lesser than Rs. 300](budget)
    - slot{"budget": "Lesser than Rs. 300"}
    - action_search_restaurants
    - utter_whether_to_email
* deny: no
    - utter_goodbye

## test_story_6
* greet: hey
    - utter_greet
* restaurant_search: Can you suggest some good restaurants in [kanyakumari](location)
    - slot{"location": "kanyakumari"}
    - action_validate_city_tier
    - followup{"name": "utter_another_location"}
    - utter_another_location
* restaurant_search: [bangalore](location)
    - slot{"location": "bangalore"}
    - action_validate_city_tier
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search: [chinese](cuisine)
    - slot{"cuisine": "chinese"}
    - action_validate_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_avg_budget_2
* restaurant_search: [More than 700](budget)
    - slot{"budget": "More than 700"}
    - action_search_restaurants
    - utter_whether_to_email
* affirm: yes
    - utter_ask_email_id
* send_mail: [abc@gmail.com](email)
    - slot{"email": "abc@gmail.com"}
    - action_validate_email_id
    - slot{"email": "abc@gmail.com"}
    - action_send_mail
    - utter_goodbye
