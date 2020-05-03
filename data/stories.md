## postive_story_end_to_end_location_given
* greet
    - utter_greet
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_validate_city_tier
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - action_validate_cuisine
    - slot{"cuisine": "mexican"}
    - utter_ask_avg_budget_2
* restaurant_search{"budget": "More than 700"}
    - slot{"budget": "More than 700"}
    - action_search_restaurants
    - utter_whether_to_email
* affirm
    - utter_ask_email_id
* send_mail{"email": "abc@gmail.com"}
    - slot{"email": "abc@gmail.com"}
    - action_validate_email_id
    - slot{"email": "abc@gmail.com"}
    - action_send_mail
    - utter_goodbye

## postive_story_end_to_end_2_location_given
* greet
    - utter_greet
* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"}
    - action_validate_city_tier
    - slot{"location": "chennai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
    - action_validate_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_avg_budget_2
* restaurant_search{"budget": "More than 700"}
    - slot{"budget": "More than 700"}
    - action_search_restaurants
    - utter_whether_to_email
* affirm
    - utter_ask_email_id
* send_mail{"email": "abc@gmail.com"}
    - slot{"email": "abc@gmail.com"}
    - action_validate_email_id
    - slot{"email": "abc@gmail.com"}
    - action_send_mail
    - utter_goodbye

## postive_story_end_to_end_3_location_given
* greet
    - utter_greet
* restaurant_search{"location": "hyderabad"}
    - slot{"location": "hyderabad"}
    - action_validate_city_tier
    - slot{"location": "hyderabad"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_validate_cuisine
    - slot{"cuisine": "italian"}
    - utter_ask_avg_budget_2
* restaurant_search{"budget": "Rs. 300 to 700"}
    - slot{"budget": "Rs. 300 to 700"}
    - action_search_restaurants
    - utter_whether_to_email
* affirm
    - utter_ask_email_id
* send_mail{"email": "abc@gmail.com"}
    - slot{"email": "abc@gmail.com"}
    - action_validate_email_id
    - slot{"email": "abc@gmail.com"}
    - action_send_mail
    - utter_goodbye

## postive_story_end_to_end_4_location_given
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validate_city_tier
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_validate_cuisine
    - slot{"cuisine": "south indian"}
    - utter_ask_avg_budget_2
* restaurant_search{"budget": "Lesser than Rs. 300"}
    - slot{"budget": "Lesser than Rs. 300"}
    - action_search_restaurants
    - utter_whether_to_email
* affirm
    - utter_ask_email_id
* send_mail{"email": "xyz@gmail.com"}
    - slot{"email": "xyz@gmail.com"}
    - action_validate_email_id
    - slot{"email": "xyz@gmail.com"}
    - action_send_mail
    - utter_goodbye

## postive_story_end_to_end_5_location_given
* greet
    - utter_greet
* restaurant_search{"location": "goa"}
    - slot{"location": "goa"}
    - action_validate_city_tier
    - slot{"location": "goa"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_validate_cuisine
    - slot{"cuisine": "north indian"}
    - utter_ask_avg_budget_2
* restaurant_search{"budget": "Rs. 300 to 700"}
    - slot{"budget": "Rs. 300 to 700"}
    - action_search_restaurants
    - utter_whether_to_email
* affirm
    - utter_ask_email_id
* send_mail{"email": "fdfdxyz@gmail.com"}
    - slot{"email": "fdfdxyz@gmail.com"}
    - action_validate_email_id
    - slot{"email": "fdfdxyz@gmail.com"}
    - action_send_mail
    - utter_goodbye

## postive_story_end_to_end_6_location_given
* greet
    - utter_greet
* restaurant_search{"location": "pune"}
    - slot{"location": "pune"}
    - action_validate_city_tier
    - slot{"location": "pune"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - action_validate_cuisine
    - slot{"cuisine": "american"}
    - utter_ask_avg_budget_2
* restaurant_search{"budget": "More than 700"}
    - slot{"budget": "More than 700"}
    - action_search_restaurants
    - utter_whether_to_email
* affirm
    - utter_ask_email_id
* send_mail{"email": "xyz@gmail.com"}
    - slot{"email": "xyz@gmail.com"}
    - action_validate_email_id
    - slot{"email": "xyz@gmail.com"}
    - action_send_mail
    - utter_goodbye

## city_not_found_location_given
* greet
    - utter_greet
* restaurant_search{"location": "allahabad"}
    - slot{"location": "allahabad"}
    - action_validate_city_tier
    - followup{"name": "utter_another_location"}
    - utter_another_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_validate_city_tier
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_validate_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_avg_budget_2
* restaurant_search{"budget": "More than 700"}
    - slot{"budget": "More than 700"}
    - action_search_restaurants
    - utter_whether_to_email
* affirm
    - utter_ask_email_id
* send_mail{"email": "abc@gmail.com"}
    - slot{"email": "abc@gmail.com"}
    - action_validate_email_id
    - slot{"email": "abc@gmail.com"}
    - action_send_mail
    - utter_goodbye

## deny_to_mail_1_location_given
* greet
    - utter_greet
* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - action_validate_city_tier
    - slot{"location": "kolkata"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_validate_cuisine
    - slot{"cuisine": "south indian"}
    - utter_ask_avg_budget_2
* restaurant_search{"budget": "More than 700"}
    - slot{"budget": "More than 700"}
    - action_search_restaurants
    - utter_whether_to_email
* deny
    - utter_goodbye

## deny_to_mail_2_location_given
* greet
    - utter_greet
* restaurant_search{"location": "lucknow"}
    - slot{"location": "lucknow"}
    - action_validate_city_tier
    - slot{"location": "lucknow"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_validate_cuisine
    - slot{"cuisine": "north indian"}
    - utter_ask_avg_budget_2
* restaurant_search{"budget": "Rs. 300 to 700"}
    - slot{"budget": "Rs. 300 to 700"}
    - action_search_restaurants
    - utter_whether_to_email
* deny
    - utter_goodbye

## deny_to_mail_3_location_given
* greet
    - utter_greet
* restaurant_search{"location": "pondicherry"}
    - slot{"location": "pondicherry"}
    - action_validate_city_tier
    - slot{"location": "pondicherry"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - action_validate_cuisine
    - slot{"cuisine": "mexican"}
    - utter_ask_avg_budget_2
* restaurant_search{"budget": "More than 700"}
    - slot{"budget": "More than 700"}
    - action_search_restaurants
    - utter_whether_to_email
* deny
    - utter_goodbye

## deny_to_mail_4_location_given
* greet
    - utter_greet
* restaurant_search{"location": "ranchi"}
    - slot{"location": "ranchi"}
    - action_validate_city_tier
    - slot{"location": "ranchi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - action_validate_cuisine
    - slot{"cuisine": "american"}
    - utter_ask_avg_budget_2
* restaurant_search{"budget": "More than 700"}
    - slot{"budget": "More than 700"}
    - action_search_restaurants
    - utter_whether_to_email
* deny
    - utter_goodbye

## deny_to_mail_5_location_given
* greet
    - utter_greet
* restaurant_search{"location": "surat"}
    - slot{"location": "surat"}
    - action_validate_city_tier
    - slot{"location": "surat"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
    - action_validate_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_avg_budget_2
* restaurant_search{"budget": "Rs. 300 to 700"}
    - slot{"budget": "Rs. 300 to 700"}
    - action_search_restaurants
    - utter_whether_to_email
* deny
    - utter_goodbye

## deny_to_mail_6_location_given
* greet
    - utter_greet
* restaurant_search{"location": "raipur"}
    - slot{"location": "raipur"}
    - action_validate_city_tier
    - slot{"location": "raipur"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_validate_cuisine
    - slot{"cuisine": "italian"}
    - utter_ask_avg_budget_2
* restaurant_search{"budget": "Lesser than Rs. 300"}
    - slot{"budget": "Lesser than Rs. 300"}
    - action_search_restaurants
    - utter_whether_to_email
* deny
    - utter_goodbye

## invalid_mail_id_1_location_given
* greet
    - utter_greet
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_validate_city_tier
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - action_validate_cuisine
    - slot{"cuisine": "american"}
    - utter_ask_avg_budget_2
* restaurant_search{"budget": "Lesser than Rs. 300"}
    - slot{"budget": "Lesser than Rs. 300"}
    - action_search_restaurants
    - utter_whether_to_email
* affirm
    - utter_ask_email_id
* send_mail{"email": "abc@.com"}
    - slot{"email": "abc@.com"}
    - action_validate_email_id
    - followup{"name": "utter_enter_valid_email_id"}
    - utter_enter_valid_email_id
* send_mail{"email": "abc@gmail.com"}
    - slot{"email": "abc@gmail.com"}
    - action_send_mail
    - utter_goodbye

## invalid_mail_id_2_location_given
* greet
    - utter_greet
* restaurant_search{"location": "kochi"}
    - slot{"location": "kochi"}
    - action_validate_city_tier
    - slot{"location": "kochi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - action_validate_cuisine
    - slot{"cuisine": "mexican"}
    - utter_ask_avg_budget_2
* restaurant_search{"budget": "Rs. 300 to 700"}
    - slot{"budget": "Rs. 300 to 700"}
    - action_search_restaurants
    - utter_whether_to_email
* affirm
    - utter_ask_email_id
* send_mail{"email": "gadd@.com"}
    - slot{"email": "gadd@.com"}
    - action_validate_email_id
    - followup{"name": "utter_enter_valid_email_id"}
    - utter_enter_valid_email_id
* send_mail{"email": "abc@gmail.com"}
    - slot{"email": "abc@gmail.com"}
    - action_send_mail
    - utter_goodbye

## invalid_mail_id_3_location_given
* greet
    - utter_greet
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_validate_city_tier
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
    - action_validate_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_avg_budget_2
* restaurant_search{"budget": "Rs. 300 to 700"}
    - slot{"budget": "Rs. 300 to 700"}
    - action_search_restaurants
    - utter_whether_to_email
* affirm
    - utter_ask_email_id
* send_mail{"email": "gadd@.c"}
    - slot{"email": "gadd@.c"}
    - action_validate_email_id
    - followup{"name": "utter_enter_valid_email_id"}
    - utter_enter_valid_email_id
* send_mail{"email": "abc@gmail.com"}
    - slot{"email": "abc@gmail.com"}
    - action_send_mail
    - utter_goodbye

## story_17
* greet
    - utter_greet
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_validate_city_tier
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_validate_cuisine
    - slot{"cuisine": "italian"}
    - utter_ask_avg_budget_2
* restaurant_search{"budget": "Rs. 300 to 700"}
    - slot{"budget": "Rs. 300 to 700"}
    - action_search_restaurants
    - utter_whether_to_email
* deny
    - utter_goodbye

## story_18
* greet
    - utter_greet
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_validate_city_tier
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_validate_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_avg_budget_2
* restaurant_search{"budget": "Lesser than Rs. 300"}
    - slot{"budget": "Lesser than Rs. 300"}
    - action_search_restaurants
    - utter_whether_to_email
* deny
    - utter_goodbye

## story_19
* greet
    - utter_greet
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_validate_city_tier
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_validate_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_avg_budget_2
* restaurant_search{"budget": "More than 700"}
    - slot{"budget": "More than 700"}
    - action_search_restaurants
    - utter_whether_to_email
* affirm
    - utter_ask_email_id
* send_mail{"email": "abc@gmail.com"}
    - slot{"email": "abc@gmail.com"}
    - action_validate_email_id
    - slot{"email": "abc@gmail.com"}
    - action_send_mail
    - utter_goodbye

## story_20
* greet
    - utter_greet
* restaurant_search{"location": "Amritsar"}
    - slot{"location": "Amritsar"}
    - action_validate_city_tier
    - slot{"location": "amritsar"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - action_validate_cuisine
    - slot{"cuisine": "mexican"}
    - utter_ask_avg_budget_2
* restaurant_search{"budget": "Rs. 300 to 700"}
    - slot{"budget": "Rs. 300 to 700"}
    - action_search_restaurants
    - utter_whether_to_email
* send_mail{"email": "fdfrf@gmail.com"}
    - slot{"email": "fdfrf@gmail.com"}
    - action_send_mail
    - utter_goodbye

## story_21
* greet
    - utter_greet
* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"}
    - action_validate_city_tier
    - slot{"location": "chennai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - action_validate_cuisine
    - slot{"cuisine": "mexican"}
    - utter_ask_avg_budget_2
* restaurant_search{"budget": "Rs. 300 to 700"}
    - slot{"budget": "Rs. 300 to 700"}
    - action_search_restaurants
    - utter_whether_to_email
* deny
    - utter_goodbye

## story_22
* greet
    - utter_greet
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_validate_city_tier
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - action_validate_cuisine
    - slot{"cuisine": "mexican"}
    - utter_ask_avg_budget_2
* restaurant_search{"budget": "Rs. 300 to 700"}
    - slot{"budget": "Rs. 300 to 700"}
    - action_search_restaurants
    - utter_whether_to_email
* affirm
    - utter_ask_email_id
* send_mail{"email": "fdfsdj@gmail.com"}
    - slot{"email": "fdfsdj@gmail.com"}
    - action_validate_email_id
    - slot{"email": "fdfsdj@gmail.com"}
    - action_send_mail
    - utter_goodbye

## story_23
* greet
    - utter_greet
* restaurant_search{"location": "Kozhikode"}
    - slot{"location": "Kozhikode"}
    - action_validate_city_tier
    - slot{"location": "kozhikode"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_validate_cuisine
    - slot{"cuisine": "north indian"}
    - utter_ask_avg_budget_2
* restaurant_search{"budget": "More than 700"}
    - slot{"budget": "More than 700"}
    - action_search_restaurants
    - utter_whether_to_email
* deny
    - utter_goodbye

## story_24
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_validate_city_tier
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_validate_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_avg_budget_2
* restaurant_search{"budget": "Rs. 300 to 700"}
    - slot{"budget": "Rs. 300 to 700"}
    - action_search_restaurants
    - utter_whether_to_email
* send_mail{"email": "ahbcdj@dkj.com"}
    - slot{"email": "ahbcdj@dkj.com"}
    - action_validate_email_id
    - slot{"email": "ahbcdj@dkj.com"}
    - action_send_mail
    - utter_goodbye

## story_25
* greet
    - utter_greet
* restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
    - action_validate_city_tier
    - slot{"location": "kolkata"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - action_validate_cuisine
    - slot{"cuisine": "american"}
    - utter_ask_avg_budget_2
* restaurant_search{"budget": "Lesser than Rs. 300"}
    - slot{"budget": "Lesser than Rs. 300"}
    - action_search_restaurants
    - utter_whether_to_email
* affirm
    - utter_ask_email_id
* send_mail{"email": "jddk.2jmd@kdl.co.in"}
    - slot{"email": "jddk.2jmd@kdl.co.in"}
    - action_validate_email_id
    - slot{"email": "jddk.2jmd@kdl.co.in"}
    - action_send_mail
    - utter_goodbye

## story_26
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "chennai"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chennai"}
    - action_validate_city_tier
    - slot{"location": "chennai"}
    - action_validate_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_avg_budget_2
* restaurant_search{"budget": "Lesser than Rs. 300"}
    - slot{"budget": "Lesser than Rs. 300"}
    - action_search_restaurants
    - utter_whether_to_email
* deny
    - utter_goodbye

## location_cuisine_given_end_to_end_deny_mail
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chandigarh"}
    - action_validate_city_tier
    - slot{"location": "chandigarh"}
    - action_validate_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_avg_budget_2
* restaurant_search{"budget": "Lesser than Rs. 300"}
    - slot{"budget": "Lesser than Rs. 300"}
    - action_search_restaurants
    - utter_whether_to_email
* deny
    - utter_goodbye

## location_cuisine_given_end_to_end_deny_mail_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "location": "mumbai"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "mumbai"}
    - action_validate_city_tier
    - slot{"location": "mumbai"}
    - action_validate_cuisine
    - slot{"cuisine": "mexican"}
    - utter_ask_avg_budget_2
* restaurant_search{"budget": "Rs. 300 to 700"}
    - slot{"budget": "Rs. 300 to 700"}
    - action_search_restaurants
    - utter_whether_to_email
* deny
    - utter_goodbye

## location_cuisine_given_end_to_end_deny_mail_2
* greet
    - utter_greet
* restaurant_search{"cuisine": "american", "location": "chennai"}
    - slot{"cuisine": "american"}
    - slot{"location": "chennai"}
    - action_validate_city_tier
    - slot{"location": "chennai"}
    - action_validate_cuisine
    - slot{"cuisine": "american"}
    - utter_ask_avg_budget_2
* restaurant_search{"budget": "More than 700"}
    - slot{"budget": "More than 700"}
    - action_search_restaurants
    - utter_whether_to_email
* deny
    - utter_goodbye

## location_cuisine_given_end_to_end_deny_mail_3
* greet
    - utter_greet
* restaurant_search{"cuisine": "north indian", "location": "bangalore"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "bangalore"}
    - action_validate_city_tier
    - slot{"location": "bangalore"}
    - action_validate_cuisine
    - slot{"cuisine": "north indian"}
    - utter_ask_avg_budget_2
* restaurant_search{"budget": "More than 700"}
    - slot{"budget": "More than 700"}
    - action_search_restaurants
    - utter_whether_to_email
* deny
    - utter_goodbye

## location_cuisine_given_end_to_end_deny_mail_4
* greet
    - utter_greet
* restaurant_search{"cuisine": "south indian", "location": "pune"}
    - slot{"cuisine": "south indian"}
    - slot{"location": "pune"}
    - action_validate_city_tier
    - slot{"location": "pune"}
    - action_validate_cuisine
    - slot{"cuisine": "south indian"}
    - utter_ask_avg_budget_2
* restaurant_search{"budget": "Lesser than Rs. 300"}
    - slot{"budget": "Lesser than Rs. 300"}
    - action_search_restaurants
    - utter_whether_to_email
* deny
    - utter_goodbye

## location_cuisine_given_end_to_end_deny_mail_5
* greet
    - utter_greet
* restaurant_search{"cuisine": "north indian", "location": "chandigarh"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "chandigarh"}
    - action_validate_city_tier
    - slot{"location": "chandigarh"}
    - action_validate_cuisine
    - slot{"cuisine": "north indian"}
    - utter_ask_avg_budget_2
* restaurant_search{"budget": "Rs. 300 to 700"}
    - slot{"budget": "Rs. 300 to 700"}
    - action_search_restaurants
    - utter_whether_to_email
* deny
    - utter_goodbye

## location_cuisine_given_end_to_end_deny_mail_6
* greet
    - utter_greet
* restaurant_search{"cuisine": "south indian", "location": "ranchi"}
    - slot{"cuisine": "south indian"}
    - slot{"location": "ranchi"}
    - action_validate_city_tier
    - slot{"location": "ranchi"}
    - action_validate_cuisine
    - slot{"cuisine": "south indian"}
    - utter_ask_avg_budget_2
* restaurant_search{"budget": "More than 700"}
    - slot{"budget": "More than 700"}
    - action_search_restaurants
    - utter_whether_to_email
* deny
    - utter_goodbye

## end_to_end_deny_mail_all_user_input_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_validate_city_tier
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_validate_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_avg_budget_2
* restaurant_search{"budget": "Lesser than Rs. 300"}
    - slot{"budget": "Lesser than Rs. 300"}
    - action_search_restaurants
    - utter_whether_to_email
* deny
    - utter_goodbye

## end_to_end_deny_mail_all_user_input_2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"}
    - action_validate_city_tier
    - slot{"location": "chennai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - action_validate_cuisine
    - slot{"cuisine": "mexican"}
    - utter_ask_avg_budget_2
* restaurant_search{"budget": "Rs. 300 to 700"}
    - slot{"budget": "Rs. 300 to 700"}
    - action_search_restaurants
    - utter_whether_to_email
* deny
    - utter_goodbye

## end_to_end_deny_mail_all_user_input_3
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "ranchi"}
    - slot{"location": "ranchi"}
    - action_validate_city_tier
    - slot{"location": "ranchi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_validate_cuisine
    - slot{"cuisine": "italian"}
    - utter_ask_avg_budget_2
* restaurant_search{"budget": "More than 700"}
    - slot{"budget": "More than 700"}
    - action_search_restaurants
    - utter_whether_to_email
* deny
    - utter_goodbye

## end_to_end_deny_mail_all_user_input_4
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "kochi"}
    - slot{"location": "kochi"}
    - action_validate_city_tier
    - slot{"location": "kochi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - action_validate_cuisine
    - slot{"cuisine": "american"}
    - utter_ask_avg_budget_2
* restaurant_search{"budget": "Lesser than Rs. 300"}
    - slot{"budget": "Lesser than Rs. 300"}
    - action_search_restaurants
    - utter_whether_to_email
* deny
    - utter_goodbye

## end_to_end_deny_mail_all_user_input_5
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_validate_city_tier
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_validate_cuisine
    - slot{"cuisine": "south indian"}
    - utter_ask_avg_budget_2
* restaurant_search{"budget": "Rs. 300 to 700"}
    - slot{"budget": "Rs. 300 to 700"}
    - action_search_restaurants
    - utter_whether_to_email
* deny
    - utter_goodbye

## end_to_end_deny_mail_all_user_input_6
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Vadodara"}
    - slot{"location": "Vadodara"}
    - action_validate_city_tier
    - slot{"location": "vadodara"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_validate_cuisine
    - slot{"cuisine": "north indian"}
    - utter_ask_avg_budget_2
* restaurant_search{"budget": "More than 700"}
    - slot{"budget": "More than 700"}
    - action_search_restaurants
    - utter_whether_to_email
* deny
    - utter_goodbye

## end_to_end_affirm_mail_all_user_input
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_validate_city_tier
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - action_validate_cuisine
    - slot{"cuisine": "american"}
    - utter_ask_avg_budget_2
* restaurant_search{"budget": "Lesser than Rs. 300"}
    - slot{"budget": "Lesser than Rs. 300"}
    - action_search_restaurants
    - utter_whether_to_email
* affirm
    - utter_ask_email_id
* send_mail{"email": "abc@hotmail.com"}
    - slot{"email": "abc@hotmail.com"}
    - action_validate_email_id
    - slot{"email": "abc@hotmail.com"}
    - action_send_mail
    - utter_goodbye

## end_to_end_affirm_mail_all_user_input_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_validate_city_tier
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_validate_cuisine
    - slot{"cuisine": "north indian"}
    - utter_ask_avg_budget_2
* restaurant_search{"budget": "More than 700"}
    - slot{"budget": "More than 700"}
    - action_search_restaurants
    - utter_whether_to_email
* affirm
    - utter_ask_email_id
* send_mail{"email": "abc@gmail.com"}
    - slot{"email": "abc@gmail.com"}
    - action_validate_email_id
    - slot{"email": "abc@gmail.com"}
    - action_send_mail
    - utter_goodbye

## end_to_end_affirm_mail_all_user_input_2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"}
    - action_validate_city_tier
    - slot{"location": "chennai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_validate_cuisine
    - slot{"cuisine": "south indian"}
    - utter_ask_avg_budget_2
* restaurant_search{"budget": "More than 700"}
    - slot{"budget": "More than 700"}
    - action_search_restaurants
    - utter_whether_to_email
* affirm
    - utter_ask_email_id
* send_mail{"email": "def@gmail.com"}
    - slot{"email": "def@gmail.com"}
    - action_validate_email_id
    - slot{"email": "def@gmail.com"}
    - action_send_mail
    - utter_goodbye

## end_to_end_affirm_mail_all_user_input_3
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "ranchi"}
    - slot{"location": "ranchi"}
    - action_validate_city_tier
    - slot{"location": "ranchi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_validate_cuisine
    - slot{"cuisine": "north indian"}
    - utter_ask_avg_budget_2
* restaurant_search{"budget": "Lesser than Rs. 300"}
    - slot{"budget": "Lesser than Rs. 300"}
    - action_search_restaurants
    - utter_whether_to_email
* affirm
    - utter_ask_email_id
* send_mail{"email": "def@hotmail.com"}
    - slot{"email": "def@hotmail.com"}
    - action_validate_email_id
    - slot{"email": "def@hotmail.com"}
    - action_send_mail
    - utter_goodbye

## end_to_end_affirm_mail_all_user_input_4_story_44
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - action_validate_city_tier
    - slot{"location": "kolkata"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_validate_cuisine
    - slot{"cuisine": "south indian"}
    - utter_ask_avg_budget_2
* restaurant_search{"budget": "More than 700"}
    - slot{"budget": "More than 700"}
    - action_search_restaurants
    - utter_whether_to_email
* affirm
    - utter_ask_email_id
* send_mail{"email": "asdfd@rediff.com"}
    - slot{"email": "asdfd@rediff.com"}
    - action_validate_email_id
    - slot{"email": "asdfd@rediff.com"}
    - action_send_mail
    - utter_goodbye

## end_to_end_affirm_mail_all_user_input_5_story_45
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "ahmedabad"}
    - slot{"location": "ahmedabad"}
    - action_validate_city_tier
    - slot{"location": "ahmedabad"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_validate_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_avg_budget_2
* restaurant_search{"budget": "Rs. 300 to 700"}
    - slot{"budget": "Rs. 300 to 700"}
    - action_search_restaurants
    - utter_whether_to_email
* affirm
    - utter_ask_email_id
* send_mail{"email": "fdsfd@gmail.com"}
    - slot{"email": "fdsfd@gmail.com"}
    - action_validate_email_id
    - slot{"email": "fdsfd@gmail.com"}
    - action_send_mail
    - utter_goodbye

## story_46
* greet
    - utter_greet
* restaurant_search{"location": "delhi", "cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - action_validate_city_tier
    - slot{"location": "delhi"}
    - action_validate_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_avg_budget_2
* restaurant_search{"budget": "Lesser than Rs. 300"}
    - slot{"budget": "Lesser than Rs. 300"}
    - action_search_restaurants
    - utter_whether_to_email
* deny
    - utter_goodbye

## story_47
* greet
    - utter_greet
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_validate_city_tier
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - action_validate_cuisine
    - slot{"cuisine": "mexican"}
    - utter_ask_avg_budget_2
* restaurant_search{"budget": "Rs. 300 to 700"}
    - slot{"budget": "Rs. 300 to 700"}
    - action_search_restaurants
    - utter_whether_to_email
* deny
    - utter_goodbye

## end_to_end_ask_all_param_deny_mail_story_48
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_validate_city_tier
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - action_validate_cuisine
    - slot{"cuisine": "mexican"}
    - utter_ask_avg_budget_2
* restaurant_search{"budget": "Rs. 300 to 700"}
    - slot{"budget": "Rs. 300 to 700"}
    - action_search_restaurants
    - utter_whether_to_email
* deny
    - utter_goodbye

## end_to_end_ask_all_param_deny_mail_story_49
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_validate_city_tier
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - action_validate_cuisine
    - slot{"cuisine": "mexican"}
    - utter_ask_avg_budget_2
* restaurant_search{"budget": "Rs. 300 to 700"}
    - slot{"budget": "Rs. 300 to 700"}
    - action_search_restaurants
    - utter_whether_to_email
* deny
    - utter_goodbye

## end_to_end_ask_cuisine_budget_param_deny_mail_story_50
* greet
    - utter_greet
* restaurant_search{"location": "indore"}
    - slot{"location": "indore"}
    - action_validate_city_tier
    - slot{"location": "indore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - action_validate_cuisine
    - slot{"cuisine": "mexican"}
    - utter_ask_avg_budget_2
* restaurant_search{"budget": "More than 700"}
    - slot{"budget": "More than 700"}
    - action_search_restaurants
    - utter_whether_to_email
* deny
    - utter_goodbye

## end_to_end_ask_budget_param_send_mail_story_51
* greet
    - utter_greet
* restaurant_search{"cuisine": "american", "location": "chennai"}
    - slot{"cuisine": "american"}
    - slot{"location": "chennai"}
    - action_validate_city_tier
    - slot{"location": "chennai"}
    - action_validate_cuisine
    - slot{"cuisine": "american"}
    - utter_ask_avg_budget_2
* restaurant_search{"budget": "Rs. 300 to 700"}
    - slot{"budget": "Rs. 300 to 700"}
    - action_search_restaurants
    - utter_whether_to_email
* deny
    - utter_goodbye

## end_to_end_ask_budget_param_send_mail_story_52
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "location": "chandigarh"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "chandigarh"}
    - action_validate_city_tier
    - slot{"location": "chandigarh"}
    - action_validate_cuisine
    - slot{"cuisine": "mexican"}
    - utter_ask_avg_budget_2
* restaurant_search{"budget": "More than 700"}
    - slot{"budget": "More than 700"}
    - action_search_restaurants
    - utter_whether_to_email
* deny
    - utter_goodbye
