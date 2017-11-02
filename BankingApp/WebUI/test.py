from detect_intent import _detect_text_intent
from detect_intent_test import DetectIntentTest

if __name__ == '__main__':
    print _detect_text_intent("dialogflow-enterprise-demo", "NewAgent", "b83b2284-7a36-46f7-b220-e3322", "balance", "en-US").fulfillment.text
