from programy.clients.embed.configfile import EmbeddedConfigFileBot
import test_data


# initialization
config_file = "..\..\config\windows\config.yaml"
logging_file = "..\..\config\windows\logging.yaml"
question = test_data.questions

# bot
bot = EmbeddedConfigFileBot(config_file, logging_file)
client_context = bot.create_client_context("test_user")


def chatbot_testing(questions):
    total_question = len(questions)
    true_counter = 0
    for question in questions:
        # question[0] is the test string, [1] is the expected intent
        to_test = bot.process_question(client_context, question[0])
        print("[test] Question :" + question[0])
        print("[test] Chatbot Reponse :" + to_test)
        print()

        result = input('[bot] Is the output correct (Y/N) : ')
        if result == 'y':
            true_counter += 1
            result =''
        else:
            true_counter += 0
            print('no')
        # if to_test[1] == question[1]: 
        #     
    
    print('[test] Tests Count : ', total_question)
    print('[test] Accuracy : '+ str(true_counter) +'/' + str(total_question) + ", (" + str(( true_counter / total_question ) * 100) + "%)")






### bot interface ###
print("[bot] Napier AIML Tedbot")


while True:
    user_input = input(">>")
    if user_input == "exit" :
        print("[bot] Shutting down bot. Bye Bye ~")
        break
    
    elif user_input == "testing" :
        chatbot_testing(test_data.questions)

    else:
        print(bot.process_question(client_context,user_input))
        # print("[bot]" +  bot.process_question(client_context,user_input))
