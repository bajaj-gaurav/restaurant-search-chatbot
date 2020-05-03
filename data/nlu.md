## intent:affirm
- yes
- yep
- yeah
- indeed
- that's right
- ok
- great
- right, thank you
- correct
- great choice
- sounds really good
- thanks
- thank you
- thank you so much for the help
- thanks!!!
- yes, please
- yes. Please
- Bon Appetit!
- yes, plz
- yup
- yup!!!

## intent:goodbye
- bye
- goodbye
- good bye
- stop
- end
- farewell
- Bye bye
- have a good one

## intent:greet
- hey
- howdy
- hey there
- hello
- hi
- good morning
- good evening
- dear sir
- hola
- Hello!
- hello there!!
- Hola
- Hey
- Hi

## intent:deny
- no
- nope
- maybe next time
- next time
- no thanks
- no. thanks
- negative
- no, thanks
- no, thanks!!!
- no, thank you so much for help!!!

## intent:restaurant_search
- i'm looking for a place to eat
- I want to grab lunch
- I am searching for a dinner spot
- I am looking for some restaurants in [Delhi](location).
- I am looking for some restaurants in [Bangalore](location)
- show me [chinese](cuisine) restaurants
- show me [chines](cuisine:chinese) restaurants in the [New Delhi](location:Delhi)
- show me a [mexican](cuisine) place in the [centre](location)
- i am looking for an [indian](cuisine) spot called olaolaolaolaolaola
- search for restaurants
- anywhere in the [west](location)
- I am looking for [asian fusion](cuisine) food
- I am looking a restaurant in [294328](location)
- in [Gurgaon](location)
- [South Indian](cuisine)
- [North Indian](cuisine)
- [Italian](cuisine)
- [American](cuisine)
- [Mexican](cuisine)
- [Chinese](cuisine:chinese)
- [chinese](cuisine)
- [Lithuania](location)
- Oh, sorry, in [Italy](location)
- in [delhi](location)
- I am looking for some restaurants in [Mumbai](location)
- I am looking for [mexican indian fusion](cuisine)
- [central](location) [indian](cuisine) restaurant
- please help me to find restaurants in [pune](location)
- Please find me a restaurantin [bangalore](location)
- [mumbai](location)
- show me restaurants
- please find me [chinese](cuisine) restaurant in [delhi](location)
- can you find me a [chinese](cuisine) restaurant
- [delhi](location)
- please find me a restaurant in [ahmedabad](location)
- please show me a few [italian](cuisine) restaurants in [bangalore](location)
- Looking out for some good restaurants
- [bengaluru](location)
- [More than 700](budget)
- [Rs. 300 to 700](budget)
- [Lesser than Rs. 300](budget)
- looking out for some good restaurants
- [bengaluru](location:bangalore)
- looking for some good restaurants
- [kolkata](location)
- restaurant in [bangalore](location)
- Can you suggest some good restaurants in [Rishikesh](location)
- okay. Show me some in [Allahabad](location)
- Can you suggest some good restaurants in [kolkata](location)
- [bangalore](location)
- Can you suggest some good restaurants in [chennai](location)
- restaurant in [chennai](location)
- restaurants in [bangalore](location)
- restaurant in [rishikesh](location)
- [allahabad](location)
- Can you suggest some good restaurants in [bangalore](location)
- [mubaim](location)
- in [mumbai](location)
- I’m hungry. Looking out for some good [chinese](cuisine) restaurants in [chandigarh](location)
- restaurant in [mumbai](location)
- restaurant in [Amritsar](location)
- restaurant in [madras](location:chennai)
- restaurant in [bombay](location:mumbai)
- restaurant in [calicut](location:Kozhikode)
- I’m hungry. Looking out for some good restaurants
- [kochi](location)
- Can you suggest some good restaurants in [calcutta](location:Kolkata)
- in [Mumbai](location)
- I’m hungry. Looking out for some good [chinese](cuisine) restaurants in [madras](location:chennai)
- Looking out for some good [mexican](cuisine) restaurants in [mumbai](location)
- good [american](cuisine) restaurants in [chennai](location)
- Looking out for some good [north indian](cuisine) restaurants in [bangalore](location)
- Looking out for some good [south indian](cuisine) restaurants in [pune](location)
- Looking out for some good [north indian](cuisine) restaurants in [chandigarh](location)
- Looking out for some good [south indian](cuisine) restaurants in [ranchi](location)
- [chennai](location)
- [ranchi](location)
- restaurants
- find me some restaurants
- [calcutta](location)
- in [baroda](location:Vadodara)
- good restaurants
- find me good restauratns
- [ahmedabad](location)
- restaurant in [delhi](location) [chinese](cuisine)
- in [bengaluru](location:bangalore)
- restaurant in [indore](location)
- restaurant in [mumbai](location) [lebanese](cuisine)
- [american](cuisine) restaurant in [chennai](location)
- Looking out for some good [mexican](cuisine) restaurants in [chandigarh](location)
- [More than 700](budget)

## intent:send_mail
- [gauravtestbajajg@gmail.com](email)
- [abc@gmail.com](email)
- please send it on [abc@gmail.com](email)
- [abc@.com](email)
- [jddk.2jmd@kdl.co.in](email)
- yes, please email on [fdfrf@gmail.com](email)
- send to [fdfsdj@gmail.com](email)
- yes. Please send it to [ahbcdj@dkj.com](email)
- send to [abc@hotmail.com](email)
- [def@gmail.com](email)
- [def@hotmail.com](email)
- [asdfd@rediff.com](email)
- [fdsfd@gmail.com](email)
- [abc_yahoo.com](email)
- [abc@yahoo.com](email)

## synonym:4
- four

## synonym:Delhi
- New Delhi

## synonym:Kochi
- cochin
- Cochin

## synonym:Kolkata
- calcutta
- Calcutta

## synonym:Kozhikode
- calicut
- Calicut

## synonym:North Indian
- NORTH INDIAN
- north indian

## synonym:Pondicherry
- puducherry
- Puducherry

## synonym:Raipur
- New Raipur
- Atal Nagar
- new raipur
- atal nagar

## synonym:South Indian
- south indian
- SOUTH INDIAN

## synonym:Thiruvananthapuram
- Trivandrum
- trivandrum

## synonym:Vadodara
- baroda
- Baroda

## synonym:bangalore
- bengaluru
- Bengaluru

## synonym:chennai
- madras

## synonym:chinese
- chines
- Chinese
- Chines

## synonym:mid
- moderate

## synonym:mumbai
- bombay
- Bombay

## synonym:vegetarian
- veggie
- vegg

## regex:email
- [a-zA-Z0-9_\.\+-]+@[a-zA-Z0-9-]+[a-zA-Z0-9-\.]{0,}\.[a-z]{2,4}

## regex:greet
- hey[^\s]*

## regex:pincode
- [0-9]{6}

## lookup:location
  data/nlu/lookups/location.txt
