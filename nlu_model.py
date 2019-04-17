from rasa_nlu.training_data import load_data
from rasa_nlu.config import RasaNLUModelConfig
from rasa_nlu.model import Trainer
from rasa_nlu.model import Metadata, Interpreter
from rasa_nlu import config
from rasa_nlu.components import ComponentBuilder

builder = ComponentBuilder(use_cache=True)

def train_nlu(data, config_file, model_dir):
    training_data = load_data(data)
    trainer = Trainer(config.load(config_file), builder)
    trainer.train(training_data)
    model_directory = trainer.persist(model_dir, fixed_model_name = 'restaurantnlu')
    
def run_nlu():
    interpreter = Interpreter.load('./models/nlu/default/restaurantnlu', builder)
    
    ##First Story
    print(interpreter.parse("Hola"))
    print(interpreter.parse("I’m hungry. Looking out for some good restaurants"))
    print(interpreter.parse("bengaluru"))
    print(interpreter.parse("I’ll prefer chinese"))
    print(interpreter.parse("300-700 range"))
    print(interpreter.parse("yes. Please send it to ahbcdj@dkj.com"))

    ##Second Story
    print(interpreter.parse("Hey"))
    print(interpreter.parse("Can you suggest some good restaurants in Jaipur"))
    print(interpreter.parse("Okay. Show me some in Allahabad"))
    print(interpreter.parse("I’ll prefer chines"))
    print(interpreter.parse(">700"))
    print(interpreter.parse("yes. Please send it to xyz@sth.edu"))
    
    ##Third Story
    print(interpreter.parse("Hi"))
    print(interpreter.parse("Can you suggest some good restaurants in kolkata"))
    print(interpreter.parse("american"))
    print(interpreter.parse("<300"))
    print(interpreter.parse("yes. Please"))
    print(interpreter.parse("jddk.2jmd@kdl.co.in"))
    
    ##Fourth Story
    print(interpreter.parse("Hello!"))
    print(interpreter.parse("I’m hungry. Looking out for some good restaurants"))
    print(interpreter.parse("in mubaim"))
    print(interpreter.parse("in Mumbai"))
    print(interpreter.parse("north indian"))
    print(interpreter.parse("<300"))
    print(interpreter.parse("yes. Please"))
    print(interpreter.parse("mouni.g86@gmail.com"))

    ##Fifth Story
    print(interpreter.parse("Hello!"))
    print(interpreter.parse("I’m hungry. Looking out for some good mexican restaurants in varanasi"))
    print(interpreter.parse("300"))
    print(interpreter.parse("Should I send you details of all the restaurants on email?"))
    print(interpreter.parse("Okay. show me some chinese restaurants"))
    print(interpreter.parse("Rs.300 to 700"))
    print(interpreter.parse("I’m hungry. Looking out for some good chinese restaurants in hyderabad"))
    print(interpreter.parse("Lesser than Rs. 300"))
    print(interpreter.parse("Rs. 300 to 700"))
    print(interpreter.parse("More than 700"))

if __name__ == '__main__':
    train_nlu('./data/data.json', 'config_spacy.json', './models/nlu')
    run_nlu()
