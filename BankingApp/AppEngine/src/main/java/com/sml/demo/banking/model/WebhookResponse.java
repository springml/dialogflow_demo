package com.sml.demo.banking.model;

import java.util.ArrayList;

/**
 * Created by kaarthikraaj on 10/8/17.
 */
public class WebhookResponse {
    private  String speech;
    private  String displayText;

    public ArrayList<ContextOut> getContextOut() {
        return contextOut;
    }

    private  ArrayList<ContextOut> contextOut = null;
    private FollowupEvent followupEvent;
    private  String source ;

    public void setContextOut(ArrayList<ContextOut> contextOut) {
        this.contextOut = contextOut;
    }

    public FollowupEvent getFollowUpEvent() {
        return followupEvent;
    }

    public void setFollowUpEvent(FollowupEvent followUpEvent) {
        this.followupEvent = followUpEvent;
    }

    public WebhookResponse(String speech, String displayText,String source) {
        this.speech = speech;
        this.displayText = displayText;
    }

    public WebhookResponse(){

    }

    public String getSpeech() {
        return speech;
    }

    public String getDisplayText() {
        return displayText;
    }

    public String getSource() {
        return source;
    }
}