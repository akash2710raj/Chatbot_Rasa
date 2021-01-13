## welcome_path
* welcome
  - utter_welcome

## main path
* greet
  - utter_greet
* tell_name
  - action_tellname
* tell_email
  - action_tellemail
* tell_phonenumber
  - action_tellphonenumber

## greeet1
* greet
  - utter_greet

<!-- ## coding path
* coding
  - action_coding -->

## pbl path
* pbl
  - action_pbl

<!-- ## writing path
* writing
  - utter_writing -->

<!-- ## tbl path1
* tbl
  - action_tbl
* inform
  - action_level
* basiclevel
  - action_basiclogic

## tbl path
* tbl
  - action_tbl
* inform
  - action_level
* advancelevel
  - action_advancelogic

## tbl path3
* tbl
  - action_tbl
* inform
  - action_level
* expertlevel
  - action_expertlogic
  - action_validate -->

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## Search Services Path
* search_service
  - utter_search_service
  
## Coding Platforms
* coding
  - action_coding
* inform
  - action_validate
* deny
  - utter_msgus
  - utter_morehelp
* deny
  - utter_goodbye


## Coding Platforms
* coding
  - action_coding
* inform
  - action_validate
* affirm
  - utter_morehelp
* deny
  - utter_goodbye

## pbl Platforms
* pbl
  - action_pbl
* inform
  - action_validate
* deny
  - utter_msgus
  - utter_morehelp

## writing Platforms
* writing
  - action_writing
* inform
  - action_validate
* deny
  - utter_msgus
  - utter_morehelp

<!-- ## tbl Platform (working basic + language)
* tbl
  - action_level
* basic
  - action_tbl
  - action_basiclogic
* inform
  - action_basictopic -->

## tbl Platform1
* tbl
  - action_tbl
* inform
  - action_level
* basic
  - action_basiclogic
  - action_basictopic
* topic
  - action_topic

## tbl Platform2
* tbl
  - action_tbl
* inform
  - action_level
* advance
  - action_advancelogic
  - action_advancetopic

## tbl Platform3
* tbl
  - action_tbl
* inform
  - action_level
* expert
  - action_expertlogic
  - action_experttopic
  
## Inform Path  
* inform
  - action_validate
  
<!-- ## Name Path  
* tell_name
  - action_tellname
* search_service
  - utter_search_service -->
<!-- 
## Inform Path  + Yes + Yes
* affirm
  - feedback_form
  - form{"name": "feedback_form"}
  - form{"name": null} -->
  
<!-- ## Inform Path  + Yes + No
* inform
  - action_validate
* affirm
  - utter_morehelp


## Inform Path  + Yes + No
* inform
  - action_validate
* affirm
  - utter_morehelp
* affirm
  - utter_noworries -->

  
<!-- ## Inform Path  + No + Yes
* inform
  - action_validate
* deny
  - utter_askagent
* affirm
  - feedback_form
  - form{"name": "feedback_form"}
  - form{"name": null}
  
## Inform Path  + No + No
* inform
  - action_validate
* deny
  - utter_askagent
* deny
  - utter_noworries -->